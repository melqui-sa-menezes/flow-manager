import semver
from django.db import models

from apps.workflows.enums import ExecutionTimingEnum, StepTypeEnum
from commons.django_framework import BaseModel, AuditMixin

__all__ = ["Workflow", "StepWorkflow"]


class Workflow(BaseModel, AuditMixin):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(null=True, blank=True)
    version = models.CharField(
        max_length=10, unique=True, help_text="Semantic versioning (0.0.0)"
    )
    rollback_version = models.CharField(max_length=10, null=True, blank=True)
    is_beta = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    flow_json = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.version})"

    def save(self, *args, **kwargs):
        if not self.rollback_version:
            self.version = "1.0.0"
        elif self.is_beta:
            current_version = semver.VersionInfo.parse(self.version)
            new_version = current_version.bump_prerelease()
            self.version = str(new_version)
        else:
            current_version = semver.VersionInfo.parse(self.version)
            new_version = current_version.bump_patch()
            self.version = str(new_version)

        super().save(*args, **kwargs)


class StepWorkflow(BaseModel, AuditMixin):
    workflow = models.ForeignKey(
        Workflow, on_delete=models.CASCADE, related_name="steps"
    )
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(null=True, blank=True)
    step_data = models.JSONField(null=True, blank=True)
    conditions = models.JSONField(null=True, blank=True)
    step_type = models.CharField(
        max_length=StepTypeEnum.get_max_length(),
        choices=StepTypeEnum.get_database_choices(),
    )
    timing = models.CharField(
        max_length=ExecutionTimingEnum.get_max_length(),
        choices=ExecutionTimingEnum.get_database_choices(),
    )

    def __str__(self):
        return f"{self.name} ({self.step_type})"

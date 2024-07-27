import semver
from django.db import models

from commons.django_framework import BaseModel, AuditMixin


class Workflow(BaseModel, AuditMixin):
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    version = models.CharField(max_length=10, unique=True)
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

from django.contrib import admin

from apps.workflows.models import Workflow, StepWorkflow


@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "version", "is_active")
    search_fields = (
        "name",
        "version",
    )
    list_filter = (
        "id",
        "name",
        "version",
    )
    ordering = ["-version"]
    readonly_fields = ["created_at", "updated_at"]
    raw_id_fields = ["created_by"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "version",
                    "description",
                    "is_beta",
                    "is_active",
                )
            },
        ),
        (
            "Advanced options",
            {
                "fields": (
                    "created_by",
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        obj.save()


@admin.register(StepWorkflow)
class StepWorkflowAdmin(admin.ModelAdmin):
    list_display = ("name", "step_type", "timing", "id")
    search_fields = (
        "workflow__name",
        "name",
    )
    list_filter = (
        "step_type",
        "timing",
    )
    ordering = ["name"]
    readonly_fields = ["created_at", "updated_at"]
    raw_id_fields = ["workflow", "created_by"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "workflow",
                    "name",
                    "description",
                    "step_type",
                    "timing",
                    "step_data",
                    "conditions",
                )
            },
        ),
        (
            "Advanced options",
            {
                "fields": (
                    "created_by",
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        obj.save()

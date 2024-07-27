from django.contrib import admin

from apps.workflows.models import Workflow


@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "version", "is_active")
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
                    "description",
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

from typing import Any

from pydantic import Field

from commons.helpers.schemas.base import BaseSchema

__all__ = [
    "IntegrationStepDataSchema",
    "StepDataSchema",
    "ExpressionsConditionsSchema",
    "StepConditionsSchema",
    "StepWorkflowSchema",
    "WorkflowSchema",
]


class IntegrationStepDataSchema(BaseSchema):
    gateway: str
    fields: dict[str, Any] = Field(default_factory=dict)


class StepDataSchema(BaseSchema):
    integration: IntegrationStepDataSchema


class ExpressionsConditionsSchema(BaseSchema):
    value_1: str
    operator: str
    value_2: Any
    expected_type: str


class StepConditionsSchema(BaseSchema):
    target_step: str
    expressions: list[ExpressionsConditionsSchema]


class StepWorkflowSchema(BaseSchema):
    name: str
    step_type: str
    timing: str
    step_data: StepDataSchema
    conditions: list[StepConditionsSchema]


class WorkflowSchema(BaseSchema):
    workflow: str
    steps: list[StepWorkflowSchema]

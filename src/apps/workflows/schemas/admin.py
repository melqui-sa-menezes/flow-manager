from typing import Any
from pydantic import computed_field

from apps.workflows.enums import OperatorsEnum
from commons.helpers.schemas.base import BaseSchema


class ExpressionParserSchema(BaseSchema):
    field: str
    operator: OperatorsEnum
    value: Any
    value_type: str

    @computed_field
    def expression(self) -> dict[str, Any]:
        if self.value_type not in self.operator.accepted_values_type:
            raise ValueError(
                f"Invalid value type for operator {self.operator.name}. "
                f"Expected: {self.operator.accepted_values_type}."
            )
        return {
            "value_1": self.field,
            "operator": self.operator.name,
            "value_2": self.value,
            "expected_type": self.value_type,
        }

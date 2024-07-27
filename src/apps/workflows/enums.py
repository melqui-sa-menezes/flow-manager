from commons.helpers.enums import BaseEnum


class ExecutionTimingEnum(BaseEnum):
    SYNC = "sync"
    ASYNC = "async"


class StepTypeEnum(BaseEnum):
    DISPATCHER = "dispatcher"
    ENHANCEMENT = "enhancement"
    LOGIC = "logic"
    DECISION = "decision"
    WAITING = "waiting"


class OperatorsEnum(BaseEnum):
    eq = ("=", ["str", "int", "float", "bool"])
    gt = (">", ["int", "float"])
    gte = (">=", ["int", "float"])
    lt = ("<", ["int", "float"])
    lte = ("<=", ["int", "float"])
    neq = ("!=", ["str", "int", "float", "bool"])

    accepted_values_type: list[str]

    def __new__(cls, operator: str, accepted_values_type: list[str]) -> "OperatorsEnum":
        obj = object.__new__(cls)
        obj._value_ = operator
        obj.operator = operator
        obj.accepted_values_type = accepted_values_type
        return obj

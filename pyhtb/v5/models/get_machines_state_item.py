from enum import Enum


class GetMachinesStateItem(str, Enum):
    ACTIVE = "active"
    RETIRED = "retired"
    UNRELEASED = "unreleased"

    def __str__(self) -> str:
        return str(self.value)

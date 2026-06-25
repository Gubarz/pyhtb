from enum import Enum


class GetSherlocksStatus(str, Enum):
    COMPLETE = "complete"
    INCOMPLETED = "incompleted"

    def __str__(self) -> str:
        return str(self.value)

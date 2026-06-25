from enum import Enum


class GetChallengesStatus(str, Enum):
    COMPLETE = "complete"
    INCOMPLETED = "incompleted"

    def __str__(self) -> str:
        return str(self.value)

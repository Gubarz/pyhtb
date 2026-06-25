from enum import Enum


class GetMachinesDifficultyItem(str, Enum):
    EASY = "easy"
    HARD = "hard"
    INSANE = "insane"
    MEDIUM = "medium"

    def __str__(self) -> str:
        return str(self.value)

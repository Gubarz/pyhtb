from enum import Enum


class GetChallengesDifficultyItem(str, Enum):
    EASY = "easy"
    HARD = "hard"
    INSANE = "insane"
    MEDIUM = "medium"
    VERY_EASY = "very-easy"

    def __str__(self) -> str:
        return str(self.value)

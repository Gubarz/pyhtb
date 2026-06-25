from enum import Enum


class GetChallengesSortBy(str, Enum):
    NAME = "name"
    RATING = "rating"
    RELEASE_DATE = "release-date"
    SYSTEM_OWNS = "system-owns"
    USER_DIFFICULTY = "user-difficulty"
    USER_OWNS = "user-owns"

    def __str__(self) -> str:
        return str(self.value)

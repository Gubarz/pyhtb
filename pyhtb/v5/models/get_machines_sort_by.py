from enum import Enum


class GetMachinesSortBy(str, Enum):
    NAME = "name"
    RATING = "rating"
    RELEASE_DATE = "release_date"
    SYSTEM_OWNS = "system_owns"
    USER_DIFFICULTY = "user_difficulty"
    USER_OWNS = "user_owns"

    def __str__(self) -> str:
        return str(self.value)

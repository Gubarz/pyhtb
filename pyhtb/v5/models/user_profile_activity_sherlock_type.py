from enum import Enum


class UserProfileActivitySherlockType(str, Enum):
    SHERLOCK = "sherlock"

    def __str__(self) -> str:
        return str(self.value)

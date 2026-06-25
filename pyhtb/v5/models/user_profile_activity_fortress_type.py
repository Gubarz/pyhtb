from enum import Enum


class UserProfileActivityFortressType(str, Enum):
    FORTRESS = "fortress"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class UserProfileActivityProlabType(str, Enum):
    PROLAB = "prolab"

    def __str__(self) -> str:
        return str(self.value)

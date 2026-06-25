from enum import Enum


class ConnectionLabEntryType(str, Enum):
    FORTRESSES = "fortresses"
    LABS = "labs"
    STARTING_POINT = "starting_point"

    def __str__(self) -> str:
        return str(self.value)

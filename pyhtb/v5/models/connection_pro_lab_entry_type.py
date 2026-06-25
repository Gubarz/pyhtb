from enum import Enum


class ConnectionProLabEntryType(str, Enum):
    PROLAB = "prolab"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class GetMachinesOsItem(str, Enum):
    FREEBSD = "freebsd"
    LINUX = "linux"
    OPENBSD = "openbsd"
    OTHER = "other"
    WINDOWS = "windows"

    def __str__(self) -> str:
        return str(self.value)

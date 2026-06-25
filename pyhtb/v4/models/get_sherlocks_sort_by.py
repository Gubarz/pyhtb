from enum import Enum


class GetSherlocksSortBy(str, Enum):
    CATEGORY = "category"
    NAME = "name"
    RATING = "rating"
    SOLVES = "solves"

    def __str__(self) -> str:
        return str(self.value)

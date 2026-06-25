from enum import Enum


class GetSearchFetchTagsItem(str, Enum):
    CHALLENGES = "challenges"
    MACHINES = "machines"
    TEAMS = "teams"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class GetSeasonLeaderboardLeaderboard(str, Enum):
    PLAYERS = "players"
    TEAMS = "teams"

    def __str__(self) -> str:
        return str(self.value)

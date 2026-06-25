from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_season_leaderboard_leaderboard import GetSeasonLeaderboardLeaderboard
from ...models.message import Message
from ...models.season_players_leaderboard_response import (
    SeasonPlayersLeaderboardResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    leaderboard: GetSeasonLeaderboardLeaderboard,
    *,
    season: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["season"] = season

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/season/{leaderboard}/leaderboard".format(
            leaderboard=quote(str(leaderboard), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | SeasonPlayersLeaderboardResponse | None:
    if response.status_code == 200:
        response_200 = SeasonPlayersLeaderboardResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Message.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Message | SeasonPlayersLeaderboardResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    leaderboard: GetSeasonLeaderboardLeaderboard,
    *,
    client: AuthenticatedClient | Client,
    season: str | Unset = UNSET,
) -> Response[Message | SeasonPlayersLeaderboardResponse]:
    """Season Leaderboar

     Get /season/players/leaderboard

    Args:
        leaderboard (GetSeasonLeaderboardLeaderboard):
        season (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SeasonPlayersLeaderboardResponse]
    """

    kwargs = _get_kwargs(
        leaderboard=leaderboard,
        season=season,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    leaderboard: GetSeasonLeaderboardLeaderboard,
    *,
    client: AuthenticatedClient | Client,
    season: str | Unset = UNSET,
) -> Message | SeasonPlayersLeaderboardResponse | None:
    """Season Leaderboar

     Get /season/players/leaderboard

    Args:
        leaderboard (GetSeasonLeaderboardLeaderboard):
        season (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SeasonPlayersLeaderboardResponse
    """

    return sync_detailed(
        leaderboard=leaderboard,
        client=client,
        season=season,
    ).parsed


async def asyncio_detailed(
    leaderboard: GetSeasonLeaderboardLeaderboard,
    *,
    client: AuthenticatedClient | Client,
    season: str | Unset = UNSET,
) -> Response[Message | SeasonPlayersLeaderboardResponse]:
    """Season Leaderboar

     Get /season/players/leaderboard

    Args:
        leaderboard (GetSeasonLeaderboardLeaderboard):
        season (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SeasonPlayersLeaderboardResponse]
    """

    kwargs = _get_kwargs(
        leaderboard=leaderboard,
        season=season,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    leaderboard: GetSeasonLeaderboardLeaderboard,
    *,
    client: AuthenticatedClient | Client,
    season: str | Unset = UNSET,
) -> Message | SeasonPlayersLeaderboardResponse | None:
    """Season Leaderboar

     Get /season/players/leaderboard

    Args:
        leaderboard (GetSeasonLeaderboardLeaderboard):
        season (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SeasonPlayersLeaderboardResponse
    """

    return (
        await asyncio_detailed(
            leaderboard=leaderboard,
            client=client,
            season=season,
        )
    ).parsed

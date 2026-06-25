from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_season_leaderboard_top_leaderboard import (
    GetSeasonLeaderboardTopLeaderboard,
)
from ...models.get_season_leaderboard_top_period import GetSeasonLeaderboardTopPeriod
from ...models.message import Message
from ...models.season_players_leaderboard_top_response import (
    SeasonPlayersLeaderboardTopResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    leaderboard: GetSeasonLeaderboardTopLeaderboard,
    season_id: int,
    *,
    period: GetSeasonLeaderboardTopPeriod = GetSeasonLeaderboardTopPeriod.VALUE_4,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_period = period.value
    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/season/{leaderboard}/leaderboard/top/{season_id}".format(
            leaderboard=quote(str(leaderboard), safe=""),
            season_id=quote(str(season_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | SeasonPlayersLeaderboardTopResponse | None:
    if response.status_code == 200:
        response_200 = SeasonPlayersLeaderboardTopResponse.from_dict(response.json())

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
) -> Response[Message | SeasonPlayersLeaderboardTopResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    leaderboard: GetSeasonLeaderboardTopLeaderboard,
    season_id: int,
    *,
    client: AuthenticatedClient | Client,
    period: GetSeasonLeaderboardTopPeriod = GetSeasonLeaderboardTopPeriod.VALUE_4,
) -> Response[Message | SeasonPlayersLeaderboardTopResponse]:
    """Season Leaderboard Top

     Season Top Leaderboard

    Args:
        leaderboard (GetSeasonLeaderboardTopLeaderboard):
        season_id (int):
        period (GetSeasonLeaderboardTopPeriod):  Default: GetSeasonLeaderboardTopPeriod.VALUE_4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SeasonPlayersLeaderboardTopResponse]
    """

    kwargs = _get_kwargs(
        leaderboard=leaderboard,
        season_id=season_id,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    leaderboard: GetSeasonLeaderboardTopLeaderboard,
    season_id: int,
    *,
    client: AuthenticatedClient | Client,
    period: GetSeasonLeaderboardTopPeriod = GetSeasonLeaderboardTopPeriod.VALUE_4,
) -> Message | SeasonPlayersLeaderboardTopResponse | None:
    """Season Leaderboard Top

     Season Top Leaderboard

    Args:
        leaderboard (GetSeasonLeaderboardTopLeaderboard):
        season_id (int):
        period (GetSeasonLeaderboardTopPeriod):  Default: GetSeasonLeaderboardTopPeriod.VALUE_4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SeasonPlayersLeaderboardTopResponse
    """

    return sync_detailed(
        leaderboard=leaderboard,
        season_id=season_id,
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    leaderboard: GetSeasonLeaderboardTopLeaderboard,
    season_id: int,
    *,
    client: AuthenticatedClient | Client,
    period: GetSeasonLeaderboardTopPeriod = GetSeasonLeaderboardTopPeriod.VALUE_4,
) -> Response[Message | SeasonPlayersLeaderboardTopResponse]:
    """Season Leaderboard Top

     Season Top Leaderboard

    Args:
        leaderboard (GetSeasonLeaderboardTopLeaderboard):
        season_id (int):
        period (GetSeasonLeaderboardTopPeriod):  Default: GetSeasonLeaderboardTopPeriod.VALUE_4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SeasonPlayersLeaderboardTopResponse]
    """

    kwargs = _get_kwargs(
        leaderboard=leaderboard,
        season_id=season_id,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    leaderboard: GetSeasonLeaderboardTopLeaderboard,
    season_id: int,
    *,
    client: AuthenticatedClient | Client,
    period: GetSeasonLeaderboardTopPeriod = GetSeasonLeaderboardTopPeriod.VALUE_4,
) -> Message | SeasonPlayersLeaderboardTopResponse | None:
    """Season Leaderboard Top

     Season Top Leaderboard

    Args:
        leaderboard (GetSeasonLeaderboardTopLeaderboard):
        season_id (int):
        period (GetSeasonLeaderboardTopPeriod):  Default: GetSeasonLeaderboardTopPeriod.VALUE_4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SeasonPlayersLeaderboardTopResponse
    """

    return (
        await asyncio_detailed(
            leaderboard=leaderboard,
            season_id=season_id,
            client=client,
            period=period,
        )
    ).parsed

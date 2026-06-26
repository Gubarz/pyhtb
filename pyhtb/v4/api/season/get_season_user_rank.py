from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.season_user_rank import SeasonUserRank
from ...types import Response


def _get_kwargs(
    season_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/season/user/rank/{season_id}".format(
            season_id=quote(str(season_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | SeasonUserRank | None:
    if response.status_code == 200:
        response_200 = SeasonUserRank.from_dict(response.json())

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
) -> Response[Message | SeasonUserRank]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    season_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | SeasonUserRank]:
    """Get user's rank for the current season

     Retrieve user rank for a specific season.

    Args:
        season_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SeasonUserRank]
    """

    kwargs = _get_kwargs(
        season_id=season_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    season_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | SeasonUserRank | None:
    """Get user's rank for the current season

     Retrieve user rank for a specific season.

    Args:
        season_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SeasonUserRank
    """

    return sync_detailed(
        season_id=season_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    season_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | SeasonUserRank]:
    """Get user's rank for the current season

     Retrieve user rank for a specific season.

    Args:
        season_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SeasonUserRank]
    """

    kwargs = _get_kwargs(
        season_id=season_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    season_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | SeasonUserRank | None:
    """Get user's rank for the current season

     Retrieve user rank for a specific season.

    Args:
        season_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SeasonUserRank
    """

    return (
        await asyncio_detailed(
            season_id=season_id,
            client=client,
        )
    ).parsed

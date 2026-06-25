from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.challenge_activity_response import ChallengeActivityResponse
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    challenge_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/challenge/activity/{challenge_id}".format(
            challenge_id=quote(str(challenge_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChallengeActivityResponse | Message | None:
    if response.status_code == 200:
        response_200 = ChallengeActivityResponse.from_dict(response.json())

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
) -> Response[ChallengeActivityResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    challenge_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ChallengeActivityResponse | Message]:
    """List of owns related to a specific challenge

     Provides a list of users that have completed the challenge

    Args:
        challenge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeActivityResponse | Message]
    """

    kwargs = _get_kwargs(
        challenge_id=challenge_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    challenge_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ChallengeActivityResponse | Message | None:
    """List of owns related to a specific challenge

     Provides a list of users that have completed the challenge

    Args:
        challenge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeActivityResponse | Message
    """

    return sync_detailed(
        challenge_id=challenge_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    challenge_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ChallengeActivityResponse | Message]:
    """List of owns related to a specific challenge

     Provides a list of users that have completed the challenge

    Args:
        challenge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeActivityResponse | Message]
    """

    kwargs = _get_kwargs(
        challenge_id=challenge_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    challenge_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ChallengeActivityResponse | Message | None:
    """List of owns related to a specific challenge

     Provides a list of users that have completed the challenge

    Args:
        challenge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeActivityResponse | Message
    """

    return (
        await asyncio_detailed(
            challenge_id=challenge_id,
            client=client,
        )
    ).parsed

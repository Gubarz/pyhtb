from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.challenge_id_response import ChallengeIdResponse
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    challenge_slug: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/challenge/info/{challenge_slug}".format(
            challenge_slug=quote(str(challenge_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChallengeIdResponse | Message | None:
    if response.status_code == 200:
        response_200 = ChallengeIdResponse.from_dict(response.json())

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
) -> Response[ChallengeIdResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    challenge_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ChallengeIdResponse | Message]:
    """Info details of the specific challenge

     Provides a list of the challege details by id or name

    Args:
        challenge_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeIdResponse | Message]
    """

    kwargs = _get_kwargs(
        challenge_slug=challenge_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    challenge_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> ChallengeIdResponse | Message | None:
    """Info details of the specific challenge

     Provides a list of the challege details by id or name

    Args:
        challenge_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeIdResponse | Message
    """

    return sync_detailed(
        challenge_slug=challenge_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    challenge_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ChallengeIdResponse | Message]:
    """Info details of the specific challenge

     Provides a list of the challege details by id or name

    Args:
        challenge_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeIdResponse | Message]
    """

    kwargs = _get_kwargs(
        challenge_slug=challenge_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    challenge_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> ChallengeIdResponse | Message | None:
    """Info details of the specific challenge

     Provides a list of the challege details by id or name

    Args:
        challenge_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeIdResponse | Message
    """

    return (
        await asyncio_detailed(
            challenge_slug=challenge_slug,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.tracks_like_response import TracksLikeResponse
from ...types import Response


def _get_kwargs(
    track_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tracks/like/{track_id}".format(
            track_id=quote(str(track_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | TracksLikeResponse | None:
    if response.status_code == 200:
        response_200 = TracksLikeResponse.from_dict(response.json())

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
) -> Response[Message | TracksLikeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    track_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | TracksLikeResponse]:
    """Like a track

     Like a track

    Args:
        track_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | TracksLikeResponse]
    """

    kwargs = _get_kwargs(
        track_id=track_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    track_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Message | TracksLikeResponse | None:
    """Like a track

     Like a track

    Args:
        track_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | TracksLikeResponse
    """

    return sync_detailed(
        track_id=track_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    track_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | TracksLikeResponse]:
    """Like a track

     Like a track

    Args:
        track_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | TracksLikeResponse]
    """

    kwargs = _get_kwargs(
        track_id=track_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    track_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Message | TracksLikeResponse | None:
    """Like a track

     Like a track

    Args:
        track_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | TracksLikeResponse
    """

    return (
        await asyncio_detailed(
            track_id=track_id,
            client=client,
        )
    ).parsed

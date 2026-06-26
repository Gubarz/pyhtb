from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.track_error_response import TrackErrorResponse
from ...models.tracks_id_response import TracksIdResponse
from ...types import Response


def _get_kwargs(
    track_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tracks/{track_id}".format(
            track_id=quote(str(track_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | TrackErrorResponse | TracksIdResponse | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> TrackErrorResponse | TracksIdResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tracks_id_response_type_0 = (
                    TracksIdResponse.from_dict(data)
                )

                return componentsschemas_tracks_id_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_tracks_id_response_type_1 = TrackErrorResponse.from_dict(
                data
            )

            return componentsschemas_tracks_id_response_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Message | TrackErrorResponse | TracksIdResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    track_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | TrackErrorResponse | TracksIdResponse]:
    """Get Track Details

     Retrieves information related to /tracks/{id}

    Args:
        track_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | TrackErrorResponse | TracksIdResponse]
    """

    kwargs = _get_kwargs(
        track_id=track_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    track_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | TrackErrorResponse | TracksIdResponse | None:
    """Get Track Details

     Retrieves information related to /tracks/{id}

    Args:
        track_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | TrackErrorResponse | TracksIdResponse
    """

    return sync_detailed(
        track_id=track_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    track_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | TrackErrorResponse | TracksIdResponse]:
    """Get Track Details

     Retrieves information related to /tracks/{id}

    Args:
        track_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | TrackErrorResponse | TracksIdResponse]
    """

    kwargs = _get_kwargs(
        track_id=track_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    track_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | TrackErrorResponse | TracksIdResponse | None:
    """Get Track Details

     Retrieves information related to /tracks/{id}

    Args:
        track_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | TrackErrorResponse | TracksIdResponse
    """

    return (
        await asyncio_detailed(
            track_id=track_id,
            client=client,
        )
    ).parsed

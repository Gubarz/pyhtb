from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_prolab_changelogs_response_200 import GetProlabChangelogsResponse200
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    prolab_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/prolab/{prolab_id}/changelogs".format(
            prolab_id=quote(str(prolab_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetProlabChangelogsResponse200 | Message | None:
    if response.status_code == 200:
        response_200 = GetProlabChangelogsResponse200.from_dict(response.json())

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
) -> Response[GetProlabChangelogsResponse200 | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    prolab_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetProlabChangelogsResponse200 | Message]:
    """Changelogs

     Get Prolab Changelog

    Args:
        prolab_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProlabChangelogsResponse200 | Message]
    """

    kwargs = _get_kwargs(
        prolab_id=prolab_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    prolab_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetProlabChangelogsResponse200 | Message | None:
    """Changelogs

     Get Prolab Changelog

    Args:
        prolab_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProlabChangelogsResponse200 | Message
    """

    return sync_detailed(
        prolab_id=prolab_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    prolab_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetProlabChangelogsResponse200 | Message]:
    """Changelogs

     Get Prolab Changelog

    Args:
        prolab_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProlabChangelogsResponse200 | Message]
    """

    kwargs = _get_kwargs(
        prolab_id=prolab_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    prolab_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetProlabChangelogsResponse200 | Message | None:
    """Changelogs

     Get Prolab Changelog

    Args:
        prolab_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProlabChangelogsResponse200 | Message
    """

    return (
        await asyncio_detailed(
            prolab_id=prolab_id,
            client=client,
        )
    ).parsed

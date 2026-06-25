from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fortress_id_response import FortressIdResponse
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    fortress_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fortress/{fortress_id}".format(
            fortress_id=quote(str(fortress_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FortressIdResponse | Message | None:
    if response.status_code == 200:
        response_200 = FortressIdResponse.from_dict(response.json())

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
) -> Response[FortressIdResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fortress_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FortressIdResponse | Message]:
    """Get fortress profile

     Retrieves information related to /fortress/{fortress id}

    Args:
        fortress_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FortressIdResponse | Message]
    """

    kwargs = _get_kwargs(
        fortress_id=fortress_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fortress_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> FortressIdResponse | Message | None:
    """Get fortress profile

     Retrieves information related to /fortress/{fortress id}

    Args:
        fortress_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FortressIdResponse | Message
    """

    return sync_detailed(
        fortress_id=fortress_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    fortress_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FortressIdResponse | Message]:
    """Get fortress profile

     Retrieves information related to /fortress/{fortress id}

    Args:
        fortress_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FortressIdResponse | Message]
    """

    kwargs = _get_kwargs(
        fortress_id=fortress_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fortress_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> FortressIdResponse | Message | None:
    """Get fortress profile

     Retrieves information related to /fortress/{fortress id}

    Args:
        fortress_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FortressIdResponse | Message
    """

    return (
        await asyncio_detailed(
            fortress_id=fortress_id,
            client=client,
        )
    ).parsed

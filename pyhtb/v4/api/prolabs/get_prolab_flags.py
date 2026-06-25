from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.product_flags_response import ProductFlagsResponse
from ...types import Response


def _get_kwargs(
    prolab_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/prolab/{prolab_id}/flags".format(
            prolab_id=quote(str(prolab_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | ProductFlagsResponse | None:
    if response.status_code == 200:
        response_200 = ProductFlagsResponse.from_dict(response.json())

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
) -> Response[Message | ProductFlagsResponse]:
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
) -> Response[Message | ProductFlagsResponse]:
    """Get list of flags

     Retrieve flags for a specific prolab.

    Args:
        prolab_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | ProductFlagsResponse]
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
) -> Message | ProductFlagsResponse | None:
    """Get list of flags

     Retrieve flags for a specific prolab.

    Args:
        prolab_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | ProductFlagsResponse
    """

    return sync_detailed(
        prolab_id=prolab_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    prolab_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | ProductFlagsResponse]:
    """Get list of flags

     Retrieve flags for a specific prolab.

    Args:
        prolab_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | ProductFlagsResponse]
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
) -> Message | ProductFlagsResponse | None:
    """Get list of flags

     Retrieve flags for a specific prolab.

    Args:
        prolab_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | ProductFlagsResponse
    """

    return (
        await asyncio_detailed(
            prolab_id=prolab_id,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connections_server_response import ConnectionsServerResponse
from ...models.get_connections_servers_product import GetConnectionsServersProduct
from ...models.message import Message
from ...types import UNSET, Response


def _get_kwargs(
    *,
    product: GetConnectionsServersProduct,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/connections/servers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectionsServerResponse | Message | None:
    if response.status_code == 200:
        response_200 = ConnectionsServerResponse.from_dict(response.json())

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
) -> Response[ConnectionsServerResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: GetConnectionsServersProduct,
) -> Response[ConnectionsServerResponse | Message]:
    """list VPN servers

     Retrieve a list of connection servers.

    Args:
        product (GetConnectionsServersProduct):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionsServerResponse | Message]
    """

    kwargs = _get_kwargs(
        product=product,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product: GetConnectionsServersProduct,
) -> ConnectionsServerResponse | Message | None:
    """list VPN servers

     Retrieve a list of connection servers.

    Args:
        product (GetConnectionsServersProduct):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionsServerResponse | Message
    """

    return sync_detailed(
        client=client,
        product=product,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: GetConnectionsServersProduct,
) -> Response[ConnectionsServerResponse | Message]:
    """list VPN servers

     Retrieve a list of connection servers.

    Args:
        product (GetConnectionsServersProduct):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionsServerResponse | Message]
    """

    kwargs = _get_kwargs(
        product=product,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product: GetConnectionsServersProduct,
) -> ConnectionsServerResponse | Message | None:
    """list VPN servers

     Retrieve a list of connection servers.

    Args:
        product (GetConnectionsServersProduct):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionsServerResponse | Message
    """

    return (
        await asyncio_detailed(
            client=client,
            product=product,
        )
    ).parsed

from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...types import File, Response


def _get_kwargs(
    vpn_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/access/ovpnfile/{vpn_id}/0/1".format(
            vpn_id=quote(str(vpn_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> File | Message | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[File | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vpn_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[File | Message]:
    """Download TCP VPN config

     Fetches the TCP OpenVPN configuration file for the specified VPN ID, allowing the user to establish
    a VPN connection

    Args:
        vpn_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | Message]
    """

    kwargs = _get_kwargs(
        vpn_id=vpn_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vpn_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> File | Message | None:
    """Download TCP VPN config

     Fetches the TCP OpenVPN configuration file for the specified VPN ID, allowing the user to establish
    a VPN connection

    Args:
        vpn_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | Message
    """

    return sync_detailed(
        vpn_id=vpn_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vpn_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[File | Message]:
    """Download TCP VPN config

     Fetches the TCP OpenVPN configuration file for the specified VPN ID, allowing the user to establish
    a VPN connection

    Args:
        vpn_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | Message]
    """

    kwargs = _get_kwargs(
        vpn_id=vpn_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vpn_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> File | Message | None:
    """Download TCP VPN config

     Fetches the TCP OpenVPN configuration file for the specified VPN ID, allowing the user to establish
    a VPN connection

    Args:
        vpn_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | Message
    """

    return (
        await asyncio_detailed(
            vpn_id=vpn_id,
            client=client,
        )
    ).parsed

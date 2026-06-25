from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.machine_profile_response import MachineProfileResponse
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    machine_slug: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/machine/profile/{machine_slug}".format(
            machine_slug=quote(str(machine_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MachineProfileResponse | Message | None:
    if response.status_code == 200:
        response_200 = MachineProfileResponse.from_dict(response.json())

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
) -> Response[MachineProfileResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    machine_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MachineProfileResponse | Message]:
    """Get machine profile by id or name

     Retrieves profile information by id or name

    Args:
        machine_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MachineProfileResponse | Message]
    """

    kwargs = _get_kwargs(
        machine_slug=machine_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    machine_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> MachineProfileResponse | Message | None:
    """Get machine profile by id or name

     Retrieves profile information by id or name

    Args:
        machine_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MachineProfileResponse | Message
    """

    return sync_detailed(
        machine_slug=machine_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    machine_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MachineProfileResponse | Message]:
    """Get machine profile by id or name

     Retrieves profile information by id or name

    Args:
        machine_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MachineProfileResponse | Message]
    """

    kwargs = _get_kwargs(
        machine_slug=machine_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    machine_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> MachineProfileResponse | Message | None:
    """Get machine profile by id or name

     Retrieves profile information by id or name

    Args:
        machine_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MachineProfileResponse | Message
    """

    return (
        await asyncio_detailed(
            machine_slug=machine_slug,
            client=client,
        )
    ).parsed

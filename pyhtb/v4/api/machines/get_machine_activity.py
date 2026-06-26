from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.machine_activity_id_response import MachineActivityIdResponse
from ...models.message import Message
from ...types import Response


def _get_kwargs(
    machine_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/machine/activity/{machine_id}".format(
            machine_id=quote(str(machine_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MachineActivityIdResponse | Message | None:
    if response.status_code == 200:
        response_200 = MachineActivityIdResponse.from_dict(response.json())

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
) -> Response[MachineActivityIdResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    machine_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MachineActivityIdResponse | Message]:
    """machine: Activity

     Retrieves information related to /machine/activity/{machine id}

    Args:
        machine_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MachineActivityIdResponse | Message]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    machine_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> MachineActivityIdResponse | Message | None:
    """machine: Activity

     Retrieves information related to /machine/activity/{machine id}

    Args:
        machine_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MachineActivityIdResponse | Message
    """

    return sync_detailed(
        machine_id=machine_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    machine_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MachineActivityIdResponse | Message]:
    """machine: Activity

     Retrieves information related to /machine/activity/{machine id}

    Args:
        machine_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MachineActivityIdResponse | Message]
    """

    kwargs = _get_kwargs(
        machine_id=machine_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    machine_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> MachineActivityIdResponse | Message | None:
    """machine: Activity

     Retrieves information related to /machine/activity/{machine id}

    Args:
        machine_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MachineActivityIdResponse | Message
    """

    return (
        await asyncio_detailed(
            machine_id=machine_id,
            client=client,
        )
    ).parsed

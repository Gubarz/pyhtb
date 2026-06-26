from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.machine_walkthroughs_language_list_response import (
    MachineWalkthroughsLanguageListResponse,
)
from ...models.message import Message
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/machine/walkthroughs/language/list",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MachineWalkthroughsLanguageListResponse | Message | None:
    if response.status_code == 200:
        response_200 = MachineWalkthroughsLanguageListResponse.from_dict(
            response.json()
        )

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
) -> Response[MachineWalkthroughsLanguageListResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[MachineWalkthroughsLanguageListResponse | Message]:
    """machine: list Walkthrough Language options

     Retrieves information related to /machine/walkthroughs/language/list

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MachineWalkthroughsLanguageListResponse | Message]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> MachineWalkthroughsLanguageListResponse | Message | None:
    """machine: list Walkthrough Language options

     Retrieves information related to /machine/walkthroughs/language/list

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MachineWalkthroughsLanguageListResponse | Message
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[MachineWalkthroughsLanguageListResponse | Message]:
    """machine: list Walkthrough Language options

     Retrieves information related to /machine/walkthroughs/language/list

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MachineWalkthroughsLanguageListResponse | Message]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> MachineWalkthroughsLanguageListResponse | Message | None:
    """machine: list Walkthrough Language options

     Retrieves information related to /machine/walkthroughs/language/list

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MachineWalkthroughsLanguageListResponse | Message
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

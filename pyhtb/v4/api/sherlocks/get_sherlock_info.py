from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sherlock_info import SherlockInfo
from ...types import Response


def _get_kwargs(
    sherlock_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sherlocks/{sherlock_id}/info".format(
            sherlock_id=quote(str(sherlock_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SherlockInfo | None:
    if response.status_code == 200:
        response_200 = SherlockInfo.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SherlockInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sherlock_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SherlockInfo]:
    """Get info of Sherlock by ID

     Retrieve detailed information for a specific Sherlock instance.

    Args:
        sherlock_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SherlockInfo]
    """

    kwargs = _get_kwargs(
        sherlock_id=sherlock_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sherlock_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SherlockInfo | None:
    """Get info of Sherlock by ID

     Retrieve detailed information for a specific Sherlock instance.

    Args:
        sherlock_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SherlockInfo
    """

    return sync_detailed(
        sherlock_id=sherlock_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sherlock_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SherlockInfo]:
    """Get info of Sherlock by ID

     Retrieve detailed information for a specific Sherlock instance.

    Args:
        sherlock_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SherlockInfo]
    """

    kwargs = _get_kwargs(
        sherlock_id=sherlock_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sherlock_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SherlockInfo | None:
    """Get info of Sherlock by ID

     Retrieve detailed information for a specific Sherlock instance.

    Args:
        sherlock_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SherlockInfo
    """

    return (
        await asyncio_detailed(
            sherlock_id=sherlock_id,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sherlock_named_item import SherlockNamedItem
from ...types import Response


def _get_kwargs(
    sherlock_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sherlocks/{sherlock_slug}".format(
            sherlock_slug=quote(str(sherlock_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SherlockNamedItem | None:
    if response.status_code == 200:
        response_200 = SherlockNamedItem.from_dict(response.json())

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
) -> Response[Any | SherlockNamedItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sherlock_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SherlockNamedItem]:
    """Get Sherlock by Id

     Retrieve information for a specific Sherlock instance.

    Args:
        sherlock_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SherlockNamedItem]
    """

    kwargs = _get_kwargs(
        sherlock_slug=sherlock_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sherlock_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SherlockNamedItem | None:
    """Get Sherlock by Id

     Retrieve information for a specific Sherlock instance.

    Args:
        sherlock_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SherlockNamedItem
    """

    return sync_detailed(
        sherlock_slug=sherlock_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    sherlock_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | SherlockNamedItem]:
    """Get Sherlock by Id

     Retrieve information for a specific Sherlock instance.

    Args:
        sherlock_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SherlockNamedItem]
    """

    kwargs = _get_kwargs(
        sherlock_slug=sherlock_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sherlock_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | SherlockNamedItem | None:
    """Get Sherlock by Id

     Retrieve information for a specific Sherlock instance.

    Args:
        sherlock_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SherlockNamedItem
    """

    return (
        await asyncio_detailed(
            sherlock_slug=sherlock_slug,
            client=client,
        )
    ).parsed

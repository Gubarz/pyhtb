from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.rankings_country_members_response import RankingsCountryMembersResponse
from ...types import Response


def _get_kwargs(
    country_short_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rankings/country/{country_short_name}/members".format(
            country_short_name=quote(str(country_short_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | RankingsCountryMembersResponse | None:
    if response.status_code == 200:
        response_200 = RankingsCountryMembersResponse.from_dict(response.json())

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
) -> Response[Message | RankingsCountryMembersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    country_short_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | RankingsCountryMembersResponse]:
    """Get Rankings Country Members

     Get Rankings Country Members

    Args:
        country_short_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | RankingsCountryMembersResponse]
    """

    kwargs = _get_kwargs(
        country_short_name=country_short_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    country_short_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Message | RankingsCountryMembersResponse | None:
    """Get Rankings Country Members

     Get Rankings Country Members

    Args:
        country_short_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | RankingsCountryMembersResponse
    """

    return sync_detailed(
        country_short_name=country_short_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    country_short_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | RankingsCountryMembersResponse]:
    """Get Rankings Country Members

     Get Rankings Country Members

    Args:
        country_short_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | RankingsCountryMembersResponse]
    """

    kwargs = _get_kwargs(
        country_short_name=country_short_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    country_short_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Message | RankingsCountryMembersResponse | None:
    """Get Rankings Country Members

     Get Rankings Country Members

    Args:
        country_short_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | RankingsCountryMembersResponse
    """

    return (
        await asyncio_detailed(
            country_short_name=country_short_name,
            client=client,
        )
    ).parsed

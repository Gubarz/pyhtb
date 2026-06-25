from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_search_fetch_tags_item import GetSearchFetchTagsItem
from ...models.message import Message
from ...models.search_fetch_response import SearchFetchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    tags: list[GetSearchFetchTagsItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = []
        for tags_item_data in tags:
            tags_item = tags_item_data.value
            json_tags.append(tags_item)

    params["tags"] = json_tags

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search/fetch",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | SearchFetchResponse | None:
    if response.status_code == 200:
        response_200 = SearchFetchResponse.from_dict(response.json())

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
) -> Response[Message | SearchFetchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    tags: list[GetSearchFetchTagsItem] | Unset = UNSET,
) -> Response[Message | SearchFetchResponse]:
    """Fetch search results

     Fetch search results.

    Args:
        query (str):  Example: hack.
        tags (list[GetSearchFetchTagsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SearchFetchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        tags=tags,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    tags: list[GetSearchFetchTagsItem] | Unset = UNSET,
) -> Message | SearchFetchResponse | None:
    """Fetch search results

     Fetch search results.

    Args:
        query (str):  Example: hack.
        tags (list[GetSearchFetchTagsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SearchFetchResponse
    """

    return sync_detailed(
        client=client,
        query=query,
        tags=tags,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    tags: list[GetSearchFetchTagsItem] | Unset = UNSET,
) -> Response[Message | SearchFetchResponse]:
    """Fetch search results

     Fetch search results.

    Args:
        query (str):  Example: hack.
        tags (list[GetSearchFetchTagsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SearchFetchResponse]
    """

    kwargs = _get_kwargs(
        query=query,
        tags=tags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    tags: list[GetSearchFetchTagsItem] | Unset = UNSET,
) -> Message | SearchFetchResponse | None:
    """Fetch search results

     Fetch search results.

    Args:
        query (str):  Example: hack.
        tags (list[GetSearchFetchTagsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SearchFetchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            tags=tags,
        )
    ).parsed

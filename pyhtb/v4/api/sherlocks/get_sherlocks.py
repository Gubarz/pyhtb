from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sherlocks_difficulty_item import GetSherlocksDifficultyItem
from ...models.get_sherlocks_sort_by import GetSherlocksSortBy
from ...models.get_sherlocks_sort_type import GetSherlocksSortType
from ...models.get_sherlocks_state_item import GetSherlocksStateItem
from ...models.get_sherlocks_status import GetSherlocksStatus
from ...models.message import Message
from ...models.sherlock_item_list import SherlockItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sort_type: GetSherlocksSortType | Unset = UNSET,
    difficulty: list[GetSherlocksDifficultyItem] | Unset = UNSET,
    state: list[GetSherlocksStateItem] | Unset = UNSET,
    sort_by: GetSherlocksSortBy | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    status: GetSherlocksStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sort_type: str | Unset = UNSET
    if not isinstance(sort_type, Unset):
        json_sort_type = sort_type.value

    params["sort_type"] = json_sort_type

    json_difficulty: list[str] | Unset = UNSET
    if not isinstance(difficulty, Unset):
        json_difficulty = []
        for difficulty_item_data in difficulty:
            difficulty_item = difficulty_item_data.value
            json_difficulty.append(difficulty_item)

    params["difficulty[]"] = json_difficulty

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    json_category: list[int] | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category[]"] = json_category

    params["keyword"] = keyword

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sherlocks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | SherlockItemList | None:
    if response.status_code == 200:
        response_200 = SherlockItemList.from_dict(response.json())

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
) -> Response[Message | SherlockItemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    sort_type: GetSherlocksSortType | Unset = UNSET,
    difficulty: list[GetSherlocksDifficultyItem] | Unset = UNSET,
    state: list[GetSherlocksStateItem] | Unset = UNSET,
    sort_by: GetSherlocksSortBy | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    status: GetSherlocksStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Message | SherlockItemList]:
    """Get list of Sherlocks

     Retrieve a list of Sherlock instances.

    Args:
        sort_type (GetSherlocksSortType | Unset):
        difficulty (list[GetSherlocksDifficultyItem] | Unset):
        state (list[GetSherlocksStateItem] | Unset):
        sort_by (GetSherlocksSortBy | Unset):
        category (list[int] | Unset):
        keyword (str | Unset):  Example: hack.
        status (GetSherlocksStatus | Unset):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SherlockItemList]
    """

    kwargs = _get_kwargs(
        sort_type=sort_type,
        difficulty=difficulty,
        state=state,
        sort_by=sort_by,
        category=category,
        keyword=keyword,
        status=status,
        per_page=per_page,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    sort_type: GetSherlocksSortType | Unset = UNSET,
    difficulty: list[GetSherlocksDifficultyItem] | Unset = UNSET,
    state: list[GetSherlocksStateItem] | Unset = UNSET,
    sort_by: GetSherlocksSortBy | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    status: GetSherlocksStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Message | SherlockItemList | None:
    """Get list of Sherlocks

     Retrieve a list of Sherlock instances.

    Args:
        sort_type (GetSherlocksSortType | Unset):
        difficulty (list[GetSherlocksDifficultyItem] | Unset):
        state (list[GetSherlocksStateItem] | Unset):
        sort_by (GetSherlocksSortBy | Unset):
        category (list[int] | Unset):
        keyword (str | Unset):  Example: hack.
        status (GetSherlocksStatus | Unset):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SherlockItemList
    """

    return sync_detailed(
        client=client,
        sort_type=sort_type,
        difficulty=difficulty,
        state=state,
        sort_by=sort_by,
        category=category,
        keyword=keyword,
        status=status,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    sort_type: GetSherlocksSortType | Unset = UNSET,
    difficulty: list[GetSherlocksDifficultyItem] | Unset = UNSET,
    state: list[GetSherlocksStateItem] | Unset = UNSET,
    sort_by: GetSherlocksSortBy | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    status: GetSherlocksStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Message | SherlockItemList]:
    """Get list of Sherlocks

     Retrieve a list of Sherlock instances.

    Args:
        sort_type (GetSherlocksSortType | Unset):
        difficulty (list[GetSherlocksDifficultyItem] | Unset):
        state (list[GetSherlocksStateItem] | Unset):
        sort_by (GetSherlocksSortBy | Unset):
        category (list[int] | Unset):
        keyword (str | Unset):  Example: hack.
        status (GetSherlocksStatus | Unset):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | SherlockItemList]
    """

    kwargs = _get_kwargs(
        sort_type=sort_type,
        difficulty=difficulty,
        state=state,
        sort_by=sort_by,
        category=category,
        keyword=keyword,
        status=status,
        per_page=per_page,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    sort_type: GetSherlocksSortType | Unset = UNSET,
    difficulty: list[GetSherlocksDifficultyItem] | Unset = UNSET,
    state: list[GetSherlocksStateItem] | Unset = UNSET,
    sort_by: GetSherlocksSortBy | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    status: GetSherlocksStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Message | SherlockItemList | None:
    """Get list of Sherlocks

     Retrieve a list of Sherlock instances.

    Args:
        sort_type (GetSherlocksSortType | Unset):
        difficulty (list[GetSherlocksDifficultyItem] | Unset):
        state (list[GetSherlocksStateItem] | Unset):
        sort_by (GetSherlocksSortBy | Unset):
        category (list[int] | Unset):
        keyword (str | Unset):  Example: hack.
        status (GetSherlocksStatus | Unset):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | SherlockItemList
    """

    return (
        await asyncio_detailed(
            client=client,
            sort_type=sort_type,
            difficulty=difficulty,
            state=state,
            sort_by=sort_by,
            category=category,
            keyword=keyword,
            status=status,
            per_page=per_page,
            page=page,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.challenge_list_response import ChallengeListResponse
from ...models.get_challenges_difficulty_item import GetChallengesDifficultyItem
from ...models.get_challenges_sort_by import GetChallengesSortBy
from ...models.get_challenges_sort_type import GetChallengesSortType
from ...models.get_challenges_state_item import GetChallengesStateItem
from ...models.get_challenges_status import GetChallengesStatus
from ...models.get_challenges_todo import GetChallengesTodo
from ...models.message import Message
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetChallengesStatus | Unset = UNSET,
    state: list[GetChallengesStateItem] | Unset = UNSET,
    sort_by: GetChallengesSortBy | Unset = UNSET,
    sort_type: GetChallengesSortType | Unset = UNSET,
    difficulty: list[GetChallengesDifficultyItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    todo: GetChallengesTodo | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

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

    params["keyword"] = keyword

    json_category: list[int] | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category[]"] = json_category

    json_todo: int | Unset = UNSET
    if not isinstance(todo, Unset):
        json_todo = todo.value

    params["todo"] = json_todo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/challenges",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChallengeListResponse | Message | None:
    if response.status_code == 200:
        response_200 = ChallengeListResponse.from_dict(response.json())

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
) -> Response[ChallengeListResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetChallengesStatus | Unset = UNSET,
    state: list[GetChallengesStateItem] | Unset = UNSET,
    sort_by: GetChallengesSortBy | Unset = UNSET,
    sort_type: GetChallengesSortType | Unset = UNSET,
    difficulty: list[GetChallengesDifficultyItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    todo: GetChallengesTodo | Unset = UNSET,
) -> Response[ChallengeListResponse | Message]:
    """Get list of challenges

     Porivdes a list of challenges with limited challenge info

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetChallengesStatus | Unset):
        state (list[GetChallengesStateItem] | Unset):
        sort_by (GetChallengesSortBy | Unset):
        sort_type (GetChallengesSortType | Unset):
        difficulty (list[GetChallengesDifficultyItem] | Unset):
        keyword (str | Unset):  Example: hack.
        category (list[int] | Unset):
        todo (GetChallengesTodo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeListResponse | Message]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        status=status,
        state=state,
        sort_by=sort_by,
        sort_type=sort_type,
        difficulty=difficulty,
        keyword=keyword,
        category=category,
        todo=todo,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetChallengesStatus | Unset = UNSET,
    state: list[GetChallengesStateItem] | Unset = UNSET,
    sort_by: GetChallengesSortBy | Unset = UNSET,
    sort_type: GetChallengesSortType | Unset = UNSET,
    difficulty: list[GetChallengesDifficultyItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    todo: GetChallengesTodo | Unset = UNSET,
) -> ChallengeListResponse | Message | None:
    """Get list of challenges

     Porivdes a list of challenges with limited challenge info

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetChallengesStatus | Unset):
        state (list[GetChallengesStateItem] | Unset):
        sort_by (GetChallengesSortBy | Unset):
        sort_type (GetChallengesSortType | Unset):
        difficulty (list[GetChallengesDifficultyItem] | Unset):
        keyword (str | Unset):  Example: hack.
        category (list[int] | Unset):
        todo (GetChallengesTodo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeListResponse | Message
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        status=status,
        state=state,
        sort_by=sort_by,
        sort_type=sort_type,
        difficulty=difficulty,
        keyword=keyword,
        category=category,
        todo=todo,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetChallengesStatus | Unset = UNSET,
    state: list[GetChallengesStateItem] | Unset = UNSET,
    sort_by: GetChallengesSortBy | Unset = UNSET,
    sort_type: GetChallengesSortType | Unset = UNSET,
    difficulty: list[GetChallengesDifficultyItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    todo: GetChallengesTodo | Unset = UNSET,
) -> Response[ChallengeListResponse | Message]:
    """Get list of challenges

     Porivdes a list of challenges with limited challenge info

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetChallengesStatus | Unset):
        state (list[GetChallengesStateItem] | Unset):
        sort_by (GetChallengesSortBy | Unset):
        sort_type (GetChallengesSortType | Unset):
        difficulty (list[GetChallengesDifficultyItem] | Unset):
        keyword (str | Unset):  Example: hack.
        category (list[int] | Unset):
        todo (GetChallengesTodo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeListResponse | Message]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        status=status,
        state=state,
        sort_by=sort_by,
        sort_type=sort_type,
        difficulty=difficulty,
        keyword=keyword,
        category=category,
        todo=todo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetChallengesStatus | Unset = UNSET,
    state: list[GetChallengesStateItem] | Unset = UNSET,
    sort_by: GetChallengesSortBy | Unset = UNSET,
    sort_type: GetChallengesSortType | Unset = UNSET,
    difficulty: list[GetChallengesDifficultyItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category: list[int] | Unset = UNSET,
    todo: GetChallengesTodo | Unset = UNSET,
) -> ChallengeListResponse | Message | None:
    """Get list of challenges

     Porivdes a list of challenges with limited challenge info

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetChallengesStatus | Unset):
        state (list[GetChallengesStateItem] | Unset):
        sort_by (GetChallengesSortBy | Unset):
        sort_type (GetChallengesSortType | Unset):
        difficulty (list[GetChallengesDifficultyItem] | Unset):
        keyword (str | Unset):  Example: hack.
        category (list[int] | Unset):
        todo (GetChallengesTodo | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeListResponse | Message
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            status=status,
            state=state,
            sort_by=sort_by,
            sort_type=sort_type,
            difficulty=difficulty,
            keyword=keyword,
            category=category,
            todo=todo,
        )
    ).parsed

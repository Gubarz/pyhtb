from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generic_error_response import GenericErrorResponse
from ...models.get_machines_difficulty_item import GetMachinesDifficultyItem
from ...models.get_machines_free import GetMachinesFree
from ...models.get_machines_os_item import GetMachinesOsItem
from ...models.get_machines_show_completed import GetMachinesShowCompleted
from ...models.get_machines_sort_by import GetMachinesSortBy
from ...models.get_machines_sort_type import GetMachinesSortType
from ...models.get_machines_sp_tier import GetMachinesSpTier
from ...models.get_machines_state_item import GetMachinesStateItem
from ...models.get_machines_todo import GetMachinesTodo
from ...models.machines_response import MachinesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    state: list[GetMachinesStateItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    difficulty: list[GetMachinesDifficultyItem] | Unset = UNSET,
    os: list[GetMachinesOsItem] | Unset = UNSET,
    show_completed: GetMachinesShowCompleted | Unset = UNSET,
    sort_by: GetMachinesSortBy | Unset = UNSET,
    sort_type: GetMachinesSortType | Unset = UNSET,
    free: GetMachinesFree | Unset = UNSET,
    todo: GetMachinesTodo | Unset = UNSET,
    sp_tier: GetMachinesSpTier | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item = state_item_data.value
            json_state.append(state_item)

    params["state"] = json_state

    params["keyword"] = keyword

    json_difficulty: list[str] | Unset = UNSET
    if not isinstance(difficulty, Unset):
        json_difficulty = []
        for difficulty_item_data in difficulty:
            difficulty_item = difficulty_item_data.value
            json_difficulty.append(difficulty_item)

    params["difficulty[]"] = json_difficulty

    json_os: list[str] | Unset = UNSET
    if not isinstance(os, Unset):
        json_os = []
        for os_item_data in os:
            os_item = os_item_data.value
            json_os.append(os_item)

    params["os[]"] = json_os

    json_show_completed: str | Unset = UNSET
    if not isinstance(show_completed, Unset):
        json_show_completed = show_completed.value

    params["show_completed"] = json_show_completed

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    json_sort_type: str | Unset = UNSET
    if not isinstance(sort_type, Unset):
        json_sort_type = sort_type.value

    params["sort_type"] = json_sort_type

    json_free: int | Unset = UNSET
    if not isinstance(free, Unset):
        json_free = free.value

    params["free"] = json_free

    json_todo: int | Unset = UNSET
    if not isinstance(todo, Unset):
        json_todo = todo.value

    params["todo"] = json_todo

    json_sp_tier: int | Unset = UNSET
    if not isinstance(sp_tier, Unset):
        json_sp_tier = sp_tier.value

    params["spTier"] = json_sp_tier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/machines",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenericErrorResponse | MachinesResponse | None:
    if response.status_code == 200:
        response_200 = MachinesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GenericErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GenericErrorResponse | MachinesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    state: list[GetMachinesStateItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    difficulty: list[GetMachinesDifficultyItem] | Unset = UNSET,
    os: list[GetMachinesOsItem] | Unset = UNSET,
    show_completed: GetMachinesShowCompleted | Unset = UNSET,
    sort_by: GetMachinesSortBy | Unset = UNSET,
    sort_type: GetMachinesSortType | Unset = UNSET,
    free: GetMachinesFree | Unset = UNSET,
    todo: GetMachinesTodo | Unset = UNSET,
    sp_tier: GetMachinesSpTier | Unset = UNSET,
) -> Response[GenericErrorResponse | MachinesResponse]:
    """Get Machines

     Machines

    Args:
        per_page (int | Unset):
        page (int | Unset):
        state (list[GetMachinesStateItem] | Unset):
        keyword (str | Unset):  Example: hack.
        difficulty (list[GetMachinesDifficultyItem] | Unset):
        os (list[GetMachinesOsItem] | Unset):
        show_completed (GetMachinesShowCompleted | Unset):
        sort_by (GetMachinesSortBy | Unset):
        sort_type (GetMachinesSortType | Unset):
        free (GetMachinesFree | Unset):
        todo (GetMachinesTodo | Unset):
        sp_tier (GetMachinesSpTier | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericErrorResponse | MachinesResponse]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        state=state,
        keyword=keyword,
        difficulty=difficulty,
        os=os,
        show_completed=show_completed,
        sort_by=sort_by,
        sort_type=sort_type,
        free=free,
        todo=todo,
        sp_tier=sp_tier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    state: list[GetMachinesStateItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    difficulty: list[GetMachinesDifficultyItem] | Unset = UNSET,
    os: list[GetMachinesOsItem] | Unset = UNSET,
    show_completed: GetMachinesShowCompleted | Unset = UNSET,
    sort_by: GetMachinesSortBy | Unset = UNSET,
    sort_type: GetMachinesSortType | Unset = UNSET,
    free: GetMachinesFree | Unset = UNSET,
    todo: GetMachinesTodo | Unset = UNSET,
    sp_tier: GetMachinesSpTier | Unset = UNSET,
) -> GenericErrorResponse | MachinesResponse | None:
    """Get Machines

     Machines

    Args:
        per_page (int | Unset):
        page (int | Unset):
        state (list[GetMachinesStateItem] | Unset):
        keyword (str | Unset):  Example: hack.
        difficulty (list[GetMachinesDifficultyItem] | Unset):
        os (list[GetMachinesOsItem] | Unset):
        show_completed (GetMachinesShowCompleted | Unset):
        sort_by (GetMachinesSortBy | Unset):
        sort_type (GetMachinesSortType | Unset):
        free (GetMachinesFree | Unset):
        todo (GetMachinesTodo | Unset):
        sp_tier (GetMachinesSpTier | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericErrorResponse | MachinesResponse
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        state=state,
        keyword=keyword,
        difficulty=difficulty,
        os=os,
        show_completed=show_completed,
        sort_by=sort_by,
        sort_type=sort_type,
        free=free,
        todo=todo,
        sp_tier=sp_tier,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    state: list[GetMachinesStateItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    difficulty: list[GetMachinesDifficultyItem] | Unset = UNSET,
    os: list[GetMachinesOsItem] | Unset = UNSET,
    show_completed: GetMachinesShowCompleted | Unset = UNSET,
    sort_by: GetMachinesSortBy | Unset = UNSET,
    sort_type: GetMachinesSortType | Unset = UNSET,
    free: GetMachinesFree | Unset = UNSET,
    todo: GetMachinesTodo | Unset = UNSET,
    sp_tier: GetMachinesSpTier | Unset = UNSET,
) -> Response[GenericErrorResponse | MachinesResponse]:
    """Get Machines

     Machines

    Args:
        per_page (int | Unset):
        page (int | Unset):
        state (list[GetMachinesStateItem] | Unset):
        keyword (str | Unset):  Example: hack.
        difficulty (list[GetMachinesDifficultyItem] | Unset):
        os (list[GetMachinesOsItem] | Unset):
        show_completed (GetMachinesShowCompleted | Unset):
        sort_by (GetMachinesSortBy | Unset):
        sort_type (GetMachinesSortType | Unset):
        free (GetMachinesFree | Unset):
        todo (GetMachinesTodo | Unset):
        sp_tier (GetMachinesSpTier | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericErrorResponse | MachinesResponse]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        state=state,
        keyword=keyword,
        difficulty=difficulty,
        os=os,
        show_completed=show_completed,
        sort_by=sort_by,
        sort_type=sort_type,
        free=free,
        todo=todo,
        sp_tier=sp_tier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    state: list[GetMachinesStateItem] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    difficulty: list[GetMachinesDifficultyItem] | Unset = UNSET,
    os: list[GetMachinesOsItem] | Unset = UNSET,
    show_completed: GetMachinesShowCompleted | Unset = UNSET,
    sort_by: GetMachinesSortBy | Unset = UNSET,
    sort_type: GetMachinesSortType | Unset = UNSET,
    free: GetMachinesFree | Unset = UNSET,
    todo: GetMachinesTodo | Unset = UNSET,
    sp_tier: GetMachinesSpTier | Unset = UNSET,
) -> GenericErrorResponse | MachinesResponse | None:
    """Get Machines

     Machines

    Args:
        per_page (int | Unset):
        page (int | Unset):
        state (list[GetMachinesStateItem] | Unset):
        keyword (str | Unset):  Example: hack.
        difficulty (list[GetMachinesDifficultyItem] | Unset):
        os (list[GetMachinesOsItem] | Unset):
        show_completed (GetMachinesShowCompleted | Unset):
        sort_by (GetMachinesSortBy | Unset):
        sort_type (GetMachinesSortType | Unset):
        free (GetMachinesFree | Unset):
        todo (GetMachinesTodo | Unset):
        sp_tier (GetMachinesSpTier | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericErrorResponse | MachinesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            state=state,
            keyword=keyword,
            difficulty=difficulty,
            os=os,
            show_completed=show_completed,
            sort_by=sort_by,
            sort_type=sort_type,
            free=free,
            todo=todo,
            sp_tier=sp_tier,
        )
    ).parsed

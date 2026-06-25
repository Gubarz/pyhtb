from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.team_activity_item import TeamActivityItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: int,
    *,
    n_past_days: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["n_past_days"] = n_past_days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team/activity/{team_id}".format(
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | list[TeamActivityItem] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_team_activity_id_response_item_data in _response_200:
            componentsschemas_team_activity_id_response_item = (
                TeamActivityItem.from_dict(
                    componentsschemas_team_activity_id_response_item_data
                )
            )

            response_200.append(componentsschemas_team_activity_id_response_item)

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
) -> Response[Message | list[TeamActivityItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
    n_past_days: int | Unset = UNSET,
) -> Response[Message | list[TeamActivityItem]]:
    """Get Recent team Activity

     Retrieve a handful of recent team owns. (Does not indicate which member achieved each item)

    Args:
        team_id (int):
        n_past_days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | list[TeamActivityItem]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        n_past_days=n_past_days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
    n_past_days: int | Unset = UNSET,
) -> Message | list[TeamActivityItem] | None:
    """Get Recent team Activity

     Retrieve a handful of recent team owns. (Does not indicate which member achieved each item)

    Args:
        team_id (int):
        n_past_days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | list[TeamActivityItem]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        n_past_days=n_past_days,
    ).parsed


async def asyncio_detailed(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
    n_past_days: int | Unset = UNSET,
) -> Response[Message | list[TeamActivityItem]]:
    """Get Recent team Activity

     Retrieve a handful of recent team owns. (Does not indicate which member achieved each item)

    Args:
        team_id (int):
        n_past_days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | list[TeamActivityItem]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        n_past_days=n_past_days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: int,
    *,
    client: AuthenticatedClient | Client,
    n_past_days: int | Unset = UNSET,
) -> Message | list[TeamActivityItem] | None:
    """Get Recent team Activity

     Retrieve a handful of recent team owns. (Does not indicate which member achieved each item)

    Args:
        team_id (int):
        n_past_days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | list[TeamActivityItem]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            n_past_days=n_past_days,
        )
    ).parsed

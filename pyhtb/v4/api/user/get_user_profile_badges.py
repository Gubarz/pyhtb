from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.profile_badges_id_repsonse import ProfileBadgesIdRepsonse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    rare: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["rare"] = rare

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user/profile/badges/{user_id}".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | ProfileBadgesIdRepsonse | None:
    if response.status_code == 200:
        response_200 = ProfileBadgesIdRepsonse.from_dict(response.json())

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
) -> Response[Message | ProfileBadgesIdRepsonse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient | Client,
    rare: int | Unset = UNSET,
) -> Response[Message | ProfileBadgesIdRepsonse]:
    """User profile: badges

     Retrieves information related to /user/profile/badges/{user id}

    Args:
        user_id (int):
        rare (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | ProfileBadgesIdRepsonse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        rare=rare,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient | Client,
    rare: int | Unset = UNSET,
) -> Message | ProfileBadgesIdRepsonse | None:
    """User profile: badges

     Retrieves information related to /user/profile/badges/{user id}

    Args:
        user_id (int):
        rare (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | ProfileBadgesIdRepsonse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        rare=rare,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient | Client,
    rare: int | Unset = UNSET,
) -> Response[Message | ProfileBadgesIdRepsonse]:
    """User profile: badges

     Retrieves information related to /user/profile/badges/{user id}

    Args:
        user_id (int):
        rare (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | ProfileBadgesIdRepsonse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        rare=rare,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient | Client,
    rare: int | Unset = UNSET,
) -> Message | ProfileBadgesIdRepsonse | None:
    """User profile: badges

     Retrieves information related to /user/profile/badges/{user id}

    Args:
        user_id (int):
        rare (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | ProfileBadgesIdRepsonse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            rare=rare,
        )
    ).parsed

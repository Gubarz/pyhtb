from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generic_error_response import GenericErrorResponse
from ...models.get_user_profile_content_type import GetUserProfileContentType
from ...models.user_profile_content_response import UserProfileContentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    type_: GetUserProfileContentType,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_ = type_.value
    params["type"] = json_type_

    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user/profile/content/{user_id}".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenericErrorResponse | UserProfileContentResponse | None:
    if response.status_code == 200:
        response_200 = UserProfileContentResponse.from_dict(response.json())

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
) -> Response[GenericErrorResponse | UserProfileContentResponse]:
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
    type_: GetUserProfileContentType,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[GenericErrorResponse | UserProfileContentResponse]:
    """User Profile Content

     User Profile Content

    Args:
        user_id (int):
        type_ (GetUserProfileContentType):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericErrorResponse | UserProfileContentResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        type_=type_,
        per_page=per_page,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient | Client,
    type_: GetUserProfileContentType,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> GenericErrorResponse | UserProfileContentResponse | None:
    """User Profile Content

     User Profile Content

    Args:
        user_id (int):
        type_ (GetUserProfileContentType):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericErrorResponse | UserProfileContentResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        type_=type_,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient | Client,
    type_: GetUserProfileContentType,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[GenericErrorResponse | UserProfileContentResponse]:
    """User Profile Content

     User Profile Content

    Args:
        user_id (int):
        type_ (GetUserProfileContentType):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericErrorResponse | UserProfileContentResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        type_=type_,
        per_page=per_page,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient | Client,
    type_: GetUserProfileContentType,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
) -> GenericErrorResponse | UserProfileContentResponse | None:
    """User Profile Content

     User Profile Content

    Args:
        user_id (int):
        type_ (GetUserProfileContentType):
        per_page (int | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericErrorResponse | UserProfileContentResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            type_=type_,
            per_page=per_page,
            page=page,
        )
    ).parsed

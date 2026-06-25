from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.university_members_response import UniversityMembersResponse
from ...types import Response


def _get_kwargs(
    university_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/university/members/{university_id}".format(
            university_id=quote(str(university_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | list[UniversityMembersResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UniversityMembersResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[Message | list[UniversityMembersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    university_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | list[UniversityMembersResponse]]:
    """Get team members

     Retrieve the list of members of a team, including both active and pending/invited members

    Args:
        university_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | list[UniversityMembersResponse]]
    """

    kwargs = _get_kwargs(
        university_id=university_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    university_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | list[UniversityMembersResponse] | None:
    """Get team members

     Retrieve the list of members of a team, including both active and pending/invited members

    Args:
        university_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | list[UniversityMembersResponse]
    """

    return sync_detailed(
        university_id=university_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    university_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | list[UniversityMembersResponse]]:
    """Get team members

     Retrieve the list of members of a team, including both active and pending/invited members

    Args:
        university_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | list[UniversityMembersResponse]]
    """

    kwargs = _get_kwargs(
        university_id=university_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    university_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | list[UniversityMembersResponse] | None:
    """Get team members

     Retrieve the list of members of a team, including both active and pending/invited members

    Args:
        university_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | list[UniversityMembersResponse]
    """

    return (
        await asyncio_detailed(
            university_id=university_id,
            client=client,
        )
    ).parsed

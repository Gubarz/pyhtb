from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generic_error_response import GenericErrorResponse
from ...models.university_stats_response import UniversityStatsResponse
from ...types import Response


def _get_kwargs(
    university_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/universities/{university_id}/stats".format(
            university_id=quote(str(university_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenericErrorResponse | UniversityStatsResponse | None:
    if response.status_code == 200:
        response_200 = UniversityStatsResponse.from_dict(response.json())

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
) -> Response[GenericErrorResponse | UniversityStatsResponse]:
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
) -> Response[GenericErrorResponse | UniversityStatsResponse]:
    """Get University Stats

     University Stats

    Args:
        university_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericErrorResponse | UniversityStatsResponse]
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
) -> GenericErrorResponse | UniversityStatsResponse | None:
    """Get University Stats

     University Stats

    Args:
        university_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericErrorResponse | UniversityStatsResponse
    """

    return sync_detailed(
        university_id=university_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    university_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GenericErrorResponse | UniversityStatsResponse]:
    """Get University Stats

     University Stats

    Args:
        university_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenericErrorResponse | UniversityStatsResponse]
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
) -> GenericErrorResponse | UniversityStatsResponse | None:
    """Get University Stats

     University Stats

    Args:
        university_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenericErrorResponse | UniversityStatsResponse
    """

    return (
        await asyncio_detailed(
            university_id=university_id,
            client=client,
        )
    ).parsed

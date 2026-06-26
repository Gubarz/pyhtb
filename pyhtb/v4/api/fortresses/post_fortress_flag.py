from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.own_machine_error_response import OwnMachineErrorResponse
from ...models.post_fortress_flag_data_body import PostFortressFlagDataBody
from ...models.post_fortress_flag_json_body import PostFortressFlagJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fortress_id: int,
    *,
    body: PostFortressFlagJsonBody | PostFortressFlagDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fortress/{fortress_id}/flag".format(
            fortress_id=quote(str(fortress_id), safe=""),
        ),
    }

    if isinstance(body, PostFortressFlagJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostFortressFlagDataBody):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OwnMachineErrorResponse | None:
    if response.status_code == 200:
        response_200 = OwnMachineErrorResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OwnMachineErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OwnMachineErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fortress_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFortressFlagJsonBody | PostFortressFlagDataBody | Unset = UNSET,
) -> Response[OwnMachineErrorResponse]:
    """Submit flag

     Submit flag

    Args:
        fortress_id (int):
        body (PostFortressFlagJsonBody):
        body (PostFortressFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OwnMachineErrorResponse]
    """

    kwargs = _get_kwargs(
        fortress_id=fortress_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fortress_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFortressFlagJsonBody | PostFortressFlagDataBody | Unset = UNSET,
) -> OwnMachineErrorResponse | None:
    """Submit flag

     Submit flag

    Args:
        fortress_id (int):
        body (PostFortressFlagJsonBody):
        body (PostFortressFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OwnMachineErrorResponse
    """

    return sync_detailed(
        fortress_id=fortress_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    fortress_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFortressFlagJsonBody | PostFortressFlagDataBody | Unset = UNSET,
) -> Response[OwnMachineErrorResponse]:
    """Submit flag

     Submit flag

    Args:
        fortress_id (int):
        body (PostFortressFlagJsonBody):
        body (PostFortressFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OwnMachineErrorResponse]
    """

    kwargs = _get_kwargs(
        fortress_id=fortress_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fortress_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostFortressFlagJsonBody | PostFortressFlagDataBody | Unset = UNSET,
) -> OwnMachineErrorResponse | None:
    """Submit flag

     Submit flag

    Args:
        fortress_id (int):
        body (PostFortressFlagJsonBody):
        body (PostFortressFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OwnMachineErrorResponse
    """

    return (
        await asyncio_detailed(
            fortress_id=fortress_id,
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.own_machine_error_response import OwnMachineErrorResponse
from ...models.post_prolab_flag_data_body import PostProlabFlagDataBody
from ...models.post_prolab_flag_json_body import PostProlabFlagJsonBody
from ...types import UNSET, Response


def _get_kwargs(
    prolab_id: int,
    *,
    body: PostProlabFlagJsonBody | PostProlabFlagDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/prolab/{prolab_id}/flag".format(
            prolab_id=quote(str(prolab_id), safe=""),
        ),
    }

    if isinstance(body, PostProlabFlagJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostProlabFlagDataBody):
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
    prolab_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostProlabFlagJsonBody | PostProlabFlagDataBody | Unset = UNSET,
) -> Response[OwnMachineErrorResponse]:
    """Submit flag

     Submit flag

    Args:
        prolab_id (int):
        body (PostProlabFlagJsonBody):
        body (PostProlabFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OwnMachineErrorResponse]
    """

    kwargs = _get_kwargs(
        prolab_id=prolab_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    prolab_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostProlabFlagJsonBody | PostProlabFlagDataBody | Unset = UNSET,
) -> OwnMachineErrorResponse | None:
    """Submit flag

     Submit flag

    Args:
        prolab_id (int):
        body (PostProlabFlagJsonBody):
        body (PostProlabFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OwnMachineErrorResponse
    """

    return sync_detailed(
        prolab_id=prolab_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    prolab_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostProlabFlagJsonBody | PostProlabFlagDataBody | Unset = UNSET,
) -> Response[OwnMachineErrorResponse]:
    """Submit flag

     Submit flag

    Args:
        prolab_id (int):
        body (PostProlabFlagJsonBody):
        body (PostProlabFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OwnMachineErrorResponse]
    """

    kwargs = _get_kwargs(
        prolab_id=prolab_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    prolab_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostProlabFlagJsonBody | PostProlabFlagDataBody | Unset = UNSET,
) -> OwnMachineErrorResponse | None:
    """Submit flag

     Submit flag

    Args:
        prolab_id (int):
        body (PostProlabFlagJsonBody):
        body (PostProlabFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OwnMachineErrorResponse
    """

    return (
        await asyncio_detailed(
            prolab_id=prolab_id,
            client=client,
            body=body,
        )
    ).parsed

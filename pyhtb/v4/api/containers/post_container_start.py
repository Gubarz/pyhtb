from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.container_start_response import ContainerStartResponse
from ...models.message import Message
from ...models.post_container_start_data_body import PostContainerStartDataBody
from ...models.post_container_start_json_body import PostContainerStartJsonBody
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: PostContainerStartDataBody | PostContainerStartJsonBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/container/start",
    }

    if isinstance(body, PostContainerStartDataBody):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PostContainerStartJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContainerStartResponse | Message | None:
    if response.status_code == 200:
        response_200 = ContainerStartResponse.from_dict(response.json())

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
) -> Response[ContainerStartResponse | Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostContainerStartDataBody | PostContainerStartJsonBody | Unset = UNSET,
) -> Response[ContainerStartResponse | Message]:
    """Starts a Container

     Starts a container with container_id

    Args:
        body (PostContainerStartDataBody):
        body (PostContainerStartJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerStartResponse | Message]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostContainerStartDataBody | PostContainerStartJsonBody | Unset = UNSET,
) -> ContainerStartResponse | Message | None:
    """Starts a Container

     Starts a container with container_id

    Args:
        body (PostContainerStartDataBody):
        body (PostContainerStartJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerStartResponse | Message
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostContainerStartDataBody | PostContainerStartJsonBody | Unset = UNSET,
) -> Response[ContainerStartResponse | Message]:
    """Starts a Container

     Starts a container with container_id

    Args:
        body (PostContainerStartDataBody):
        body (PostContainerStartJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerStartResponse | Message]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostContainerStartDataBody | PostContainerStartJsonBody | Unset = UNSET,
) -> ContainerStartResponse | Message | None:
    """Starts a Container

     Starts a container with container_id

    Args:
        body (PostContainerStartDataBody):
        body (PostContainerStartJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerStartResponse | Message
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

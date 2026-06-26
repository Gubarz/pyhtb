from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.post_todo_update_product import PostTodoUpdateProduct
from ...models.update_response import UpdateResponse
from ...types import Response


def _get_kwargs(
    product: PostTodoUpdateProduct,
    product_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{product}/todo/update/{product_id}".format(
            product=quote(str(product), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | UpdateResponse | None:
    if response.status_code == 200:
        response_200 = UpdateResponse.from_dict(response.json())

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
) -> Response[Message | UpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product: PostTodoUpdateProduct,
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | UpdateResponse]:
    """Update Todo list

     Update Todo list

    Args:
        product (PostTodoUpdateProduct):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | UpdateResponse]
    """

    kwargs = _get_kwargs(
        product=product,
        product_id=product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product: PostTodoUpdateProduct,
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | UpdateResponse | None:
    """Update Todo list

     Update Todo list

    Args:
        product (PostTodoUpdateProduct):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | UpdateResponse
    """

    return sync_detailed(
        product=product,
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product: PostTodoUpdateProduct,
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | UpdateResponse]:
    """Update Todo list

     Update Todo list

    Args:
        product (PostTodoUpdateProduct):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | UpdateResponse]
    """

    kwargs = _get_kwargs(
        product=product,
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product: PostTodoUpdateProduct,
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | UpdateResponse | None:
    """Update Todo list

     Update Todo list

    Args:
        product (PostTodoUpdateProduct):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | UpdateResponse
    """

    return (
        await asyncio_detailed(
            product=product,
            product_id=product_id,
            client=client,
        )
    ).parsed

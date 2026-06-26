from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_review_paginated_product import GetReviewPaginatedProduct
from ...models.message import Message
from ...models.reviews import Reviews
from ...types import Response


def _get_kwargs(
    product: GetReviewPaginatedProduct,
    product_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/review/{product}/{product_id}/paginated".format(
            product=quote(str(product), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Message | Reviews | None:
    if response.status_code == 200:
        response_200 = Reviews.from_dict(response.json())

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
) -> Response[Message | Reviews]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product: GetReviewPaginatedProduct,
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | Reviews]:
    """Retrieves reviews

     Retrieves reviews

    Args:
        product (GetReviewPaginatedProduct):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | Reviews]
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
    product: GetReviewPaginatedProduct,
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | Reviews | None:
    """Retrieves reviews

     Retrieves reviews

    Args:
        product (GetReviewPaginatedProduct):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | Reviews
    """

    return sync_detailed(
        product=product,
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product: GetReviewPaginatedProduct,
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Message | Reviews]:
    """Retrieves reviews

     Retrieves reviews

    Args:
        product (GetReviewPaginatedProduct):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message | Reviews]
    """

    kwargs = _get_kwargs(
        product=product,
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product: GetReviewPaginatedProduct,
    product_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Message | Reviews | None:
    """Retrieves reviews

     Retrieves reviews

    Args:
        product (GetReviewPaginatedProduct):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message | Reviews
    """

    return (
        await asyncio_detailed(
            product=product,
            product_id=product_id,
            client=client,
        )
    ).parsed

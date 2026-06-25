from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_error import BadRequestError
from ...models.post_sherlock_tasks_flag_data_body import PostSherlockTasksFlagDataBody
from ...models.post_sherlock_tasks_flag_json_body import PostSherlockTasksFlagJsonBody
from ...models.task_flag_response import TaskFlagResponse
from ...types import UNSET, Response


def _get_kwargs(
    sherlock_id: int,
    task_id: int,
    *,
    body: PostSherlockTasksFlagJsonBody | PostSherlockTasksFlagDataBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sherlocks/{sherlock_id}/tasks/{task_id}/flag".format(
            sherlock_id=quote(str(sherlock_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
    }

    if isinstance(body, PostSherlockTasksFlagJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostSherlockTasksFlagDataBody):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BadRequestError | TaskFlagResponse | None:
    if response.status_code == 201:
        response_201 = TaskFlagResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = BadRequestError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BadRequestError | TaskFlagResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sherlock_id: int,
    task_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostSherlockTasksFlagJsonBody | PostSherlockTasksFlagDataBody | Unset = UNSET,
) -> Response[Any | BadRequestError | TaskFlagResponse]:
    """Submit flag for a specific Sherlock task

     Submit a flag for a specific task in a Sherlock instance.

    Args:
        sherlock_id (int):
        task_id (int):
        body (PostSherlockTasksFlagJsonBody):
        body (PostSherlockTasksFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequestError | TaskFlagResponse]
    """

    kwargs = _get_kwargs(
        sherlock_id=sherlock_id,
        task_id=task_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sherlock_id: int,
    task_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostSherlockTasksFlagJsonBody | PostSherlockTasksFlagDataBody | Unset = UNSET,
) -> Any | BadRequestError | TaskFlagResponse | None:
    """Submit flag for a specific Sherlock task

     Submit a flag for a specific task in a Sherlock instance.

    Args:
        sherlock_id (int):
        task_id (int):
        body (PostSherlockTasksFlagJsonBody):
        body (PostSherlockTasksFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequestError | TaskFlagResponse
    """

    return sync_detailed(
        sherlock_id=sherlock_id,
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    sherlock_id: int,
    task_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostSherlockTasksFlagJsonBody | PostSherlockTasksFlagDataBody | Unset = UNSET,
) -> Response[Any | BadRequestError | TaskFlagResponse]:
    """Submit flag for a specific Sherlock task

     Submit a flag for a specific task in a Sherlock instance.

    Args:
        sherlock_id (int):
        task_id (int):
        body (PostSherlockTasksFlagJsonBody):
        body (PostSherlockTasksFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequestError | TaskFlagResponse]
    """

    kwargs = _get_kwargs(
        sherlock_id=sherlock_id,
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sherlock_id: int,
    task_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostSherlockTasksFlagJsonBody | PostSherlockTasksFlagDataBody | Unset = UNSET,
) -> Any | BadRequestError | TaskFlagResponse | None:
    """Submit flag for a specific Sherlock task

     Submit a flag for a specific task in a Sherlock instance.

    Args:
        sherlock_id (int):
        task_id (int):
        body (PostSherlockTasksFlagJsonBody):
        body (PostSherlockTasksFlagDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequestError | TaskFlagResponse
    """

    return (
        await asyncio_detailed(
            sherlock_id=sherlock_id,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed

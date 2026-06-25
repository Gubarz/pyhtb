from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_invitations_id_response_headers import (
        TeamInvitationsIdResponseHeaders,
    )
    from ..models.user_entry import UserEntry


T = TypeVar("T", bound="TeamInvitationsIdResponse")


@_attrs_define
class TeamInvitationsIdResponse:
    """Schema definition for Team Invitations Id Response

    Attributes:
        exception (None | str | Unset):
        headers (TeamInvitationsIdResponseHeaders | Unset):
        original (list[UserEntry] | Unset):
    """

    exception: None | str | Unset = UNSET
    headers: TeamInvitationsIdResponseHeaders | Unset = UNSET
    original: list[UserEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exception: None | str | Unset
        if isinstance(self.exception, Unset):
            exception = UNSET
        else:
            exception = self.exception

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        original: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.original, Unset):
            original = []
            for original_item_data in self.original:
                original_item = original_item_data.to_dict()
                original.append(original_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exception is not UNSET:
            field_dict["exception"] = exception
        if headers is not UNSET:
            field_dict["headers"] = headers
        if original is not UNSET:
            field_dict["original"] = original

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_invitations_id_response_headers import (
            TeamInvitationsIdResponseHeaders,
        )
        from ..models.user_entry import UserEntry

        d = dict(src_dict)

        def _parse_exception(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exception = _parse_exception(d.pop("exception", UNSET))

        _headers = d.pop("headers", UNSET)
        headers: TeamInvitationsIdResponseHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = TeamInvitationsIdResponseHeaders.from_dict(_headers)

        _original = d.pop("original", UNSET)
        original: list[UserEntry] | Unset = UNSET
        if _original is not UNSET:
            original = []
            for original_item_data in _original:
                original_item = UserEntry.from_dict(original_item_data)

                original.append(original_item)

        team_invitations_id_response = cls(
            exception=exception,
            headers=headers,
            original=original,
        )

        team_invitations_id_response.additional_properties = d
        return team_invitations_id_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

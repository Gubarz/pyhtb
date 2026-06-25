from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_rank import UserRank


T = TypeVar("T", bound="OwnResponse")


@_attrs_define
class OwnResponse:
    """Schema definition for Own Response

    Attributes:
        message (str | Unset):  Example: machine owned successfully!.
        user_rank (UserRank | Unset):
    """

    message: str | Unset = UNSET
    user_rank: UserRank | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        user_rank: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_rank, Unset):
            user_rank = self.user_rank.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if user_rank is not UNSET:
            field_dict["user_rank"] = user_rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_rank import UserRank

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _user_rank = d.pop("user_rank", UNSET)
        user_rank: UserRank | Unset
        if isinstance(_user_rank, Unset):
            user_rank = UNSET
        else:
            user_rank = UserRank.from_dict(_user_rank)

        own_response = cls(
            message=message,
            user_rank=user_rank,
        )

        own_response.additional_properties = d
        return own_response

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

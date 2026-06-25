from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_user_stats import ProfileUserStats


T = TypeVar("T", bound="ProfileIdRepsonse")


@_attrs_define
class ProfileIdRepsonse:
    """Schema definition for Profile Id Repsonse

    Attributes:
        user_stats (ProfileUserStats | Unset):
    """

    user_stats: ProfileUserStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_stats, Unset):
            user_stats = self.user_stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_stats is not UNSET:
            field_dict["userStats"] = user_stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_user_stats import ProfileUserStats

        d = dict(src_dict)
        _user_stats = d.pop("userStats", UNSET)
        user_stats: ProfileUserStats | Unset
        if isinstance(_user_stats, Unset):
            user_stats = UNSET
        else:
            user_stats = ProfileUserStats.from_dict(_user_stats)

        profile_id_repsonse = cls(
            user_stats=user_stats,
        )

        profile_id_repsonse.additional_properties = d
        return profile_id_repsonse

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

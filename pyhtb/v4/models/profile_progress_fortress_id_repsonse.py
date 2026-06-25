from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_progress_fortress_profile import (
        ProfileProgressFortressProfile,
    )


T = TypeVar("T", bound="ProfileProgressFortressIdRepsonse")


@_attrs_define
class ProfileProgressFortressIdRepsonse:
    """Schema definition for Profile Progress Fortress Id Repsonse

    Attributes:
        profile (ProfileProgressFortressProfile | Unset):
    """

    profile: ProfileProgressFortressProfile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_progress_fortress_profile import (
            ProfileProgressFortressProfile,
        )

        d = dict(src_dict)
        _profile = d.pop("profile", UNSET)
        profile: ProfileProgressFortressProfile | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = ProfileProgressFortressProfile.from_dict(_profile)

        profile_progress_fortress_id_repsonse = cls(
            profile=profile,
        )

        profile_progress_fortress_id_repsonse.additional_properties = d
        return profile_progress_fortress_id_repsonse

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

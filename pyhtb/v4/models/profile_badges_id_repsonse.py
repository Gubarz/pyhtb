from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_badges_item import ProfileBadgesItem


T = TypeVar("T", bound="ProfileBadgesIdRepsonse")


@_attrs_define
class ProfileBadgesIdRepsonse:
    """Schema definition for Profile Badges Id Repsonse

    Attributes:
        badges (list[ProfileBadgesItem] | Unset):
    """

    badges: list[ProfileBadgesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        badges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.badges, Unset):
            badges = []
            for componentsschemas_profile_badges_items_item_data in self.badges:
                componentsschemas_profile_badges_items_item = (
                    componentsschemas_profile_badges_items_item_data.to_dict()
                )
                badges.append(componentsschemas_profile_badges_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if badges is not UNSET:
            field_dict["badges"] = badges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_badges_item import ProfileBadgesItem

        d = dict(src_dict)
        _badges = d.pop("badges", UNSET)
        badges: list[ProfileBadgesItem] | Unset = UNSET
        if _badges is not UNSET:
            badges = []
            for componentsschemas_profile_badges_items_item_data in _badges:
                componentsschemas_profile_badges_items_item = (
                    ProfileBadgesItem.from_dict(
                        componentsschemas_profile_badges_items_item_data
                    )
                )

                badges.append(componentsschemas_profile_badges_items_item)

        profile_badges_id_repsonse = cls(
            badges=badges,
        )

        profile_badges_id_repsonse.additional_properties = d
        return profile_badges_id_repsonse

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

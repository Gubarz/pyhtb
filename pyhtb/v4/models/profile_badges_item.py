from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_badges_item_pivot import ProfileBadgesItemPivot


T = TypeVar("T", bound="ProfileBadgesItem")


@_attrs_define
class ProfileBadgesItem:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        icon (str | Unset):
        description (str | Unset):
        pivot (ProfileBadgesItemPivot | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    icon: str | Unset = UNSET
    description: str | Unset = UNSET
    pivot: ProfileBadgesItemPivot | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        icon = self.icon

        description = self.description

        pivot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pivot, Unset):
            pivot = self.pivot.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if description is not UNSET:
            field_dict["description"] = description
        if pivot is not UNSET:
            field_dict["pivot"] = pivot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_badges_item_pivot import ProfileBadgesItemPivot

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        icon = d.pop("icon", UNSET)

        description = d.pop("description", UNSET)

        _pivot = d.pop("pivot", UNSET)
        pivot: ProfileBadgesItemPivot | Unset
        if isinstance(_pivot, Unset):
            pivot = UNSET
        else:
            pivot = ProfileBadgesItemPivot.from_dict(_pivot)

        profile_badges_item = cls(
            id=id,
            name=name,
            icon=icon,
            description=description,
            pivot=pivot,
        )

        profile_badges_item.additional_properties = d
        return profile_badges_item

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

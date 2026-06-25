from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Badge")


@_attrs_define
class Badge:
    """Schema definition for Badge

    Attributes:
        badge_category_id (int | Unset):  Example: 1.
        color (None | str | Unset):  Example: gold.
        description_en (str | Unset):  Example: Has been in the Top 10 of the Hall of Fame..
        icon (str | Unset):  Example: far fa-list-ol.
        id (int | Unset):  Example: 2.
        name (str | Unset):  Example: Top 10.
        rarity (float | Unset):
        users_count (int | Unset):  Example: 326.
    """

    badge_category_id: int | Unset = UNSET
    color: None | str | Unset = UNSET
    description_en: str | Unset = UNSET
    icon: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    rarity: float | Unset = UNSET
    users_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        badge_category_id = self.badge_category_id

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        description_en = self.description_en

        icon = self.icon

        id = self.id

        name = self.name

        rarity = self.rarity

        users_count = self.users_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if badge_category_id is not UNSET:
            field_dict["badge_category_id"] = badge_category_id
        if color is not UNSET:
            field_dict["color"] = color
        if description_en is not UNSET:
            field_dict["description_en"] = description_en
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rarity is not UNSET:
            field_dict["rarity"] = rarity
        if users_count is not UNSET:
            field_dict["users_count"] = users_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        badge_category_id = d.pop("badge_category_id", UNSET)

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        description_en = d.pop("description_en", UNSET)

        icon = d.pop("icon", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rarity = d.pop("rarity", UNSET)

        users_count = d.pop("users_count", UNSET)

        badge = cls(
            badge_category_id=badge_category_id,
            color=color,
            description_en=description_en,
            icon=icon,
            id=id,
            name=name,
            rarity=rarity,
            users_count=users_count,
        )

        badge.additional_properties = d
        return badge

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

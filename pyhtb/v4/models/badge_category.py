from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.badge import Badge


T = TypeVar("T", bound="BadgeCategory")


@_attrs_define
class BadgeCategory:
    """
    Attributes:
        badges (list[Badge] | Unset):
        description (str | Unset):
        id (int | Unset):
        name (str | Unset):
    """

    badges: list[Badge] | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        badges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.badges, Unset):
            badges = []
            for componentsschemas_badge_category_items_item_data in self.badges:
                componentsschemas_badge_category_items_item = (
                    componentsschemas_badge_category_items_item_data.to_dict()
                )
                badges.append(componentsschemas_badge_category_items_item)

        description = self.description

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if badges is not UNSET:
            field_dict["badges"] = badges
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.badge import Badge

        d = dict(src_dict)
        _badges = d.pop("badges", UNSET)
        badges: list[Badge] | Unset = UNSET
        if _badges is not UNSET:
            badges = []
            for componentsschemas_badge_category_items_item_data in _badges:
                componentsschemas_badge_category_items_item = Badge.from_dict(
                    componentsschemas_badge_category_items_item_data
                )

                badges.append(componentsschemas_badge_category_items_item)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        badge_category = cls(
            badges=badges,
            description=description,
            id=id,
            name=name,
        )

        badge_category.additional_properties = d
        return badge_category

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

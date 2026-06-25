from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.badge_category import BadgeCategory


T = TypeVar("T", bound="BadgesResponse")


@_attrs_define
class BadgesResponse:
    """Schema definition for Badges Response

    Attributes:
        categories (list[BadgeCategory] | Unset):
    """

    categories: list[BadgeCategory] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for componentsschemas_badge_categories_item_data in self.categories:
                componentsschemas_badge_categories_item = (
                    componentsschemas_badge_categories_item_data.to_dict()
                )
                categories.append(componentsschemas_badge_categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.badge_category import BadgeCategory

        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: list[BadgeCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for componentsschemas_badge_categories_item_data in _categories:
                componentsschemas_badge_categories_item = BadgeCategory.from_dict(
                    componentsschemas_badge_categories_item_data
                )

                categories.append(componentsschemas_badge_categories_item)

        badges_response = cls(
            categories=categories,
        )

        badges_response.additional_properties = d
        return badges_response

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

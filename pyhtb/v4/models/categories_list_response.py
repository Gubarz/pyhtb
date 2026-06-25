from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.categories_item import CategoriesItem


T = TypeVar("T", bound="CategoriesListResponse")


@_attrs_define
class CategoriesListResponse:
    """Schema definition for Categories List Response

    Attributes:
        info (list[CategoriesItem] | Unset):
    """

    info: list[CategoriesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = []
            for componentsschemas_categories_list_info_item_data in self.info:
                componentsschemas_categories_list_info_item = (
                    componentsschemas_categories_list_info_item_data.to_dict()
                )
                info.append(componentsschemas_categories_list_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.categories_item import CategoriesItem

        d = dict(src_dict)
        _info = d.pop("info", UNSET)
        info: list[CategoriesItem] | Unset = UNSET
        if _info is not UNSET:
            info = []
            for componentsschemas_categories_list_info_item_data in _info:
                componentsschemas_categories_list_info_item = CategoriesItem.from_dict(
                    componentsschemas_categories_list_info_item_data
                )

                info.append(componentsschemas_categories_list_info_item)

        categories_list_response = cls(
            info=info,
        )

        categories_list_response.additional_properties = d
        return categories_list_response

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

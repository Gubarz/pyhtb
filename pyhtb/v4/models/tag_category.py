from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag import Tag


T = TypeVar("T", bound="TagCategory")


@_attrs_define
class TagCategory:
    """Schema definition for Tag Category

    Attributes:
        id (int | Unset):
        name (str | Unset):
        tags (list[Tag] | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for componentsschemas_tag_category_tags_items_item_data in self.tags:
                componentsschemas_tag_category_tags_items_item = (
                    componentsschemas_tag_category_tags_items_item_data.to_dict()
                )
                tags.append(componentsschemas_tag_category_tags_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag import Tag

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for componentsschemas_tag_category_tags_items_item_data in _tags:
                componentsschemas_tag_category_tags_items_item = Tag.from_dict(
                    componentsschemas_tag_category_tags_items_item_data
                )

                tags.append(componentsschemas_tag_category_tags_items_item)

        tag_category = cls(
            id=id,
            name=name,
            tags=tags,
        )

        tag_category.additional_properties = d
        return tag_category

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

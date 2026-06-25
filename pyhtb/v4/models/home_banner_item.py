from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HomeBannerItem")


@_attrs_define
class HomeBannerItem:
    """
    Attributes:
        image (str | Unset):
        link (str | Unset):
        new_window (bool | Unset):
    """

    image: str | Unset = UNSET
    link: str | Unset = UNSET
    new_window: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        link = self.link

        new_window = self.new_window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if link is not UNSET:
            field_dict["link"] = link
        if new_window is not UNSET:
            field_dict["new_window"] = new_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = d.pop("image", UNSET)

        link = d.pop("link", UNSET)

        new_window = d.pop("new_window", UNSET)

        home_banner_item = cls(
            image=image,
            link=link,
            new_window=new_window,
        )

        home_banner_item.additional_properties = d
        return home_banner_item

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

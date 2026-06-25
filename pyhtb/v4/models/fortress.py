from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Fortress")


@_attrs_define
class Fortress:
    """Schema definition for Fortress

    Attributes:
        cover_image_url (str | Unset):  Example:
            https://labs.hackthebox.com/storage/fortresses/c4ca4238a0b923820dcc509a6f75849b_cover_small.png.
        id (int | Unset):  Example: 1.
        image (str | Unset):  Example:
            https://labs.hackthebox.com/storage/fortresses/c4ca4238a0b923820dcc509a6f75849b_logo.svg.
        name (str | Unset):  Example: Jet.
        new (bool | Unset):
        number_of_flags (int | Unset):  Example: 11.
        owned_flags (int | Unset):
        ownership (float | Unset):
    """

    cover_image_url: str | Unset = UNSET
    id: int | Unset = UNSET
    image: str | Unset = UNSET
    name: str | Unset = UNSET
    new: bool | Unset = UNSET
    number_of_flags: int | Unset = UNSET
    owned_flags: int | Unset = UNSET
    ownership: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cover_image_url = self.cover_image_url

        id = self.id

        image = self.image

        name = self.name

        new = self.new

        number_of_flags = self.number_of_flags

        owned_flags = self.owned_flags

        ownership = self.ownership

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if name is not UNSET:
            field_dict["name"] = name
        if new is not UNSET:
            field_dict["new"] = new
        if number_of_flags is not UNSET:
            field_dict["number_of_flags"] = number_of_flags
        if owned_flags is not UNSET:
            field_dict["owned_flags"] = owned_flags
        if ownership is not UNSET:
            field_dict["ownership"] = ownership

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cover_image_url = d.pop("cover_image_url", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        name = d.pop("name", UNSET)

        new = d.pop("new", UNSET)

        number_of_flags = d.pop("number_of_flags", UNSET)

        owned_flags = d.pop("owned_flags", UNSET)

        ownership = d.pop("ownership", UNSET)

        fortress = cls(
            cover_image_url=cover_image_url,
            id=id,
            image=image,
            name=name,
            new=new,
            number_of_flags=number_of_flags,
            owned_flags=owned_flags,
            ownership=ownership,
        )

        fortress.additional_properties = d
        return fortress

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

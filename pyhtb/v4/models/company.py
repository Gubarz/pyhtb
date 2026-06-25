from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Company")


@_attrs_define
class Company:
    """Schema definition for Company

    Attributes:
        description (str | Unset):  Example: <p>Jet.com is currently looking for Security Engineers in the USA.</p>....
        id (int | Unset):  Example: 3.
        image (str | Unset):  Example: https://labs.hackthebox.com/storage/companies/3.png.
        name (str | Unset):  Example: Jet.com.
        url (str | Unset):  Example: https://jet.com/careers.
    """

    description: str | Unset = UNSET
    id: int | Unset = UNSET
    image: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        image = self.image

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        company = cls(
            description=description,
            id=id,
            image=image,
            name=name,
            url=url,
        )

        company.additional_properties = d
        return company

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

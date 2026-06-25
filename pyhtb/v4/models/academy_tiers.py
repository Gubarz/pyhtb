from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcademyTiers")


@_attrs_define
class AcademyTiers:
    """
    Attributes:
        color (str | Unset):  Example: success.
        name (str | Unset):  Example: Tier I.
        number (int | Unset):  Example: 1.
        id (int | Unset):
    """

    color: str | Unset = UNSET
    name: str | Unset = UNSET
    number: int | Unset = UNSET
    id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color

        name = self.name

        number = self.number

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        id = d.pop("id", UNSET)

        academy_tiers = cls(
            color=color,
            name=name,
            number=number,
            id=id,
        )

        academy_tiers.additional_properties = d
        return academy_tiers

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

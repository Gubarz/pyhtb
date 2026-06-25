from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Flag")


@_attrs_define
class Flag:
    """Schema definition for Flag

    Attributes:
        id (int | Unset):  Example: 1.
        owned (bool | Unset):
        points (int | Unset):  Example: 5.
        title (str | Unset):  Example: Connect.
    """

    id: int | Unset = UNSET
    owned: bool | Unset = UNSET
    points: int | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owned = self.owned

        points = self.points

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if owned is not UNSET:
            field_dict["owned"] = owned
        if points is not UNSET:
            field_dict["points"] = points
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        owned = d.pop("owned", UNSET)

        points = d.pop("points", UNSET)

        title = d.pop("title", UNSET)

        flag = cls(
            id=id,
            owned=owned,
            points=points,
            title=title,
        )

        flag.additional_properties = d
        return flag

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

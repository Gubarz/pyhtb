from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TracksCreator")


@_attrs_define
class TracksCreator:
    """
    Attributes:
        type_ (str):  Example: company.
        id (int):  Example: 1.
        name (str):  Example: Hack The Box.
        avatar (str):  Example: /storage/companies/1.png.
    """

    type_: str
    id: int
    name: str
    avatar: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        name = self.name

        avatar = self.avatar

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "avatar": avatar,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id")

        name = d.pop("name")

        avatar = d.pop("avatar")

        tracks_creator = cls(
            type_=type_,
            id=id,
            name=name,
            avatar=avatar,
        )

        tracks_creator.additional_properties = d
        return tracks_creator

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

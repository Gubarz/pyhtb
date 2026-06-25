from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DesignatedLevel")


@_attrs_define
class DesignatedLevel:
    """Schema definition for Designated Level

    Attributes:
        category (str | Unset):  Example: Red team_ Operator.
        description (str | Unset):  Example: Hone your offensive tradecraft with a Red team_ Operator Level I lab. From
            gaining a foothold and establishing situational awareness, to exploiting interactive users and "living off the
            land", this will put your skills to the test..
        level (int | Unset):  Example: 1.
        team (str | Unset):  Example: red.
    """

    category: str | Unset = UNSET
    description: str | Unset = UNSET
    level: int | Unset = UNSET
    team: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        description = self.description

        level = self.level

        team = self.team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if level is not UNSET:
            field_dict["level"] = level
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        level = d.pop("level", UNSET)

        team = d.pop("team", UNSET)

        designated_level = cls(
            category=category,
            description=description,
            level=level,
            team=team,
        )

        designated_level.additional_properties = d
        return designated_level

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

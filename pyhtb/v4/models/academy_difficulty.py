from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcademyDifficulty")


@_attrs_define
class AcademyDifficulty:
    """
    Attributes:
        color (str | Unset):  Example: success.
        id (int | Unset):  Example: 3.
        level (int | Unset):  Example: 3.
        text (str | Unset):  Example: Easy.
        title (str | Unset):  Example: Easy.
    """

    color: str | Unset = UNSET
    id: int | Unset = UNSET
    level: int | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color

        id = self.id

        level = self.level

        text = self.text

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if id is not UNSET:
            field_dict["id"] = id
        if level is not UNSET:
            field_dict["level"] = level
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        id = d.pop("id", UNSET)

        level = d.pop("level", UNSET)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        academy_difficulty = cls(
            color=color,
            id=id,
            level=level,
            text=text,
            title=title,
        )

        academy_difficulty.additional_properties = d
        return academy_difficulty

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

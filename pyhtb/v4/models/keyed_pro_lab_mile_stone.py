from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyedProLabMileStone")


@_attrs_define
class KeyedProLabMileStone:
    """
    Attributes:
        description (str | Unset):
        icon (str | Unset):
        is_milestone_reached (bool | Unset):
        percent (float | Unset):
        rarity (float | Unset):
        text (str | Unset):
    """

    description: str | Unset = UNSET
    icon: str | Unset = UNSET
    is_milestone_reached: bool | Unset = UNSET
    percent: float | Unset = UNSET
    rarity: float | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        icon = self.icon

        is_milestone_reached = self.is_milestone_reached

        percent = self.percent

        rarity = self.rarity

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if is_milestone_reached is not UNSET:
            field_dict["isMilestoneReached"] = is_milestone_reached
        if percent is not UNSET:
            field_dict["percent"] = percent
        if rarity is not UNSET:
            field_dict["rarity"] = rarity
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        is_milestone_reached = d.pop("isMilestoneReached", UNSET)

        percent = d.pop("percent", UNSET)

        rarity = d.pop("rarity", UNSET)

        text = d.pop("text", UNSET)

        keyed_pro_lab_mile_stone = cls(
            description=description,
            icon=icon,
            is_milestone_reached=is_milestone_reached,
            percent=percent,
            rarity=rarity,
            text=text,
        )

        keyed_pro_lab_mile_stone.additional_properties = d
        return keyed_pro_lab_mile_stone

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

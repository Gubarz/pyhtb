from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialLinks")


@_attrs_define
class SocialLinks:
    """Schema definition for Social Links

    Attributes:
        discord (str | Unset):  Example: https://discord.gg/RnFKvTPYer.
        forum (str | Unset):  Example: https://forum.hackthebox.com/c/content/prolabs/18.
    """

    discord: str | Unset = UNSET
    forum: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discord = self.discord

        forum = self.forum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discord is not UNSET:
            field_dict["discord"] = discord
        if forum is not UNSET:
            field_dict["forum"] = forum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discord = d.pop("discord", UNSET)

        forum = d.pop("forum", UNSET)

        social_links = cls(
            discord=discord,
            forum=forum,
        )

        social_links.additional_properties = d
        return social_links

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

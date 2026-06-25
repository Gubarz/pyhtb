from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUserApptokenCreateBody")


@_attrs_define
class PostUserApptokenCreateBody:
    """
    Attributes:
        expire_after (float | Unset):
        name (str | Unset):
    """

    expire_after: float | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expire_after = self.expire_after

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expire_after is not UNSET:
            field_dict["expire_after"] = expire_after
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expire_after = d.pop("expire_after", UNSET)

        name = d.pop("name", UNSET)

        post_user_apptoken_create_body = cls(
            expire_after=expire_after,
            name=name,
        )

        post_user_apptoken_create_body.additional_properties = d
        return post_user_apptoken_create_body

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

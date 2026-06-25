from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchChallengeItem")


@_attrs_define
class SearchChallengeItem:
    """
    Attributes:
        challenge_category_id (int | Unset):  Example: 10.
        category_name (str | Unset):  Example: Pwn.
        avatar_url (str | Unset):
        id (int | Unset):  Example: 217.
        value (str | Unset):  Example: Walkie Hackie.
    """

    challenge_category_id: int | Unset = UNSET
    category_name: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    id: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_category_id = self.challenge_category_id

        category_name = self.category_name

        avatar_url = self.avatar_url

        id = self.id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge_category_id is not UNSET:
            field_dict["challenge_category_id"] = challenge_category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge_category_id = d.pop("challenge_category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        search_challenge_item = cls(
            challenge_category_id=challenge_category_id,
            category_name=category_name,
            avatar_url=avatar_url,
            id=id,
            value=value,
        )

        search_challenge_item.additional_properties = d
        return search_challenge_item

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

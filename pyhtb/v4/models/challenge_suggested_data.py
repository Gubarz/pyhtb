from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChallengeSuggestedData")


@_attrs_define
class ChallengeSuggestedData:
    """
    Attributes:
        challenge_category_name (str | Unset):
        id (int | Unset):
        name (str | Unset):
        url_name (str | Unset):
        avatar_url (str | Unset):
    """

    challenge_category_name: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    url_name: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_category_name = self.challenge_category_name

        id = self.id

        name = self.name

        url_name = self.url_name

        avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge_category_name is not UNSET:
            field_dict["challenge_category_name"] = challenge_category_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url_name is not UNSET:
            field_dict["url_name"] = url_name
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge_category_name = d.pop("challenge_category_name", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url_name = d.pop("url_name", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        challenge_suggested_data = cls(
            challenge_category_name=challenge_category_name,
            id=id,
            name=name,
            url_name=url_name,
            avatar_url=avatar_url,
        )

        challenge_suggested_data.additional_properties = d
        return challenge_suggested_data

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

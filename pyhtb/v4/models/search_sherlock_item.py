from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSherlockItem")


@_attrs_define
class SearchSherlockItem:
    """
    Attributes:
        avatar (str | Unset):  Example: https://htb-mp-prod-public-storage.s3.eu-
            central-1.amazonaws.com/challenges/9246444d94f081e3549803b928260f56.png.
        challenge_category_id (int | Unset):  Example: 16.
        category_name (str | Unset):  Example: Malware Analysis.
        description (None | str | Unset):  Example: In this Sherlock, players will investigate the Demodex rootkit
            attributed to Salt Typhoon..
        id (int | Unset):  Example: 1006.
        value (str | Unset):  Example: SalineBreeze-2.
    """

    avatar: str | Unset = UNSET
    challenge_category_id: int | Unset = UNSET
    category_name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    id: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        challenge_category_id = self.challenge_category_id

        category_name = self.category_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id = self.id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if challenge_category_id is not UNSET:
            field_dict["challenge_category_id"] = challenge_category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        challenge_category_id = d.pop("challenge_category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        search_sherlock_item = cls(
            avatar=avatar,
            challenge_category_id=challenge_category_id,
            category_name=category_name,
            description=description,
            id=id,
            value=value,
        )

        search_sherlock_item.additional_properties = d
        return search_sherlock_item

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

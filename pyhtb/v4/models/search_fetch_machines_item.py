from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchFetchMachinesItem")


@_attrs_define
class SearchFetchMachinesItem:
    """
    Attributes:
        avatar (str | Unset):  Example: b99c956ef89135920805452930f99f71.png.
        id (int | Unset):  Example: 176.
        is_sp (bool | Unset):
        tier_id (int | None | Unset):
        value (str | Unset):  Example: Hackback.
    """

    avatar: str | Unset = UNSET
    id: int | Unset = UNSET
    is_sp: bool | Unset = UNSET
    tier_id: int | None | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        id = self.id

        is_sp = self.is_sp

        tier_id: int | None | Unset
        if isinstance(self.tier_id, Unset):
            tier_id = UNSET
        else:
            tier_id = self.tier_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if id is not UNSET:
            field_dict["id"] = id
        if is_sp is not UNSET:
            field_dict["isSp"] = is_sp
        if tier_id is not UNSET:
            field_dict["tierId"] = tier_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        id = d.pop("id", UNSET)

        is_sp = d.pop("isSp", UNSET)

        def _parse_tier_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tier_id = _parse_tier_id(d.pop("tierId", UNSET))

        value = d.pop("value", UNSET)

        search_fetch_machines_item = cls(
            avatar=avatar,
            id=id,
            is_sp=is_sp,
            tier_id=tier_id,
            value=value,
        )

        search_fetch_machines_item.additional_properties = d
        return search_fetch_machines_item

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

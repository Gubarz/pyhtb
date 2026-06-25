from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchTeamItem")


@_attrs_define
class SearchTeamItem:
    """
    Attributes:
        avatar (str | Unset):  Example: 45c166d697d65080d54501403b433256.jpg.
        id (int | Unset):  Example: 3174.
        motto (None | str | Unset):  Example: Be sure, be secure!.
        value (str | Unset):  Example: HACK.
    """

    avatar: str | Unset = UNSET
    id: int | Unset = UNSET
    motto: None | str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        id = self.id

        motto: None | str | Unset
        if isinstance(self.motto, Unset):
            motto = UNSET
        else:
            motto = self.motto

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if id is not UNSET:
            field_dict["id"] = id
        if motto is not UNSET:
            field_dict["motto"] = motto
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        id = d.pop("id", UNSET)

        def _parse_motto(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        motto = _parse_motto(d.pop("motto", UNSET))

        value = d.pop("value", UNSET)

        search_team_item = cls(
            avatar=avatar,
            id=id,
            motto=motto,
            value=value,
        )

        search_team_item.additional_properties = d
        return search_team_item

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

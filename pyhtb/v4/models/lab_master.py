from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LabMaster")


@_attrs_define
class LabMaster:
    """Schema definition for Lab Master

    Attributes:
        avatar_thumb (None | str | Unset):  Example: /storage/avatars/2b44f5ca5458931c49e1fa57da6705c1_thumb.png.
        id (int | Unset):  Example: 11649.
        name (str | Unset):  Example: RastaMouse.
        account_id (str | Unset):
    """

    avatar_thumb: None | str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_thumb: None | str | Unset
        if isinstance(self.avatar_thumb, Unset):
            avatar_thumb = UNSET
        else:
            avatar_thumb = self.avatar_thumb

        id = self.id

        name = self.name

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_thumb is not UNSET:
            field_dict["avatar_thumb"] = avatar_thumb
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_avatar_thumb(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_thumb = _parse_avatar_thumb(d.pop("avatar_thumb", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        account_id = d.pop("account_id", UNSET)

        lab_master = cls(
            avatar_thumb=avatar_thumb,
            id=id,
            name=name,
            account_id=account_id,
        )

        lab_master.additional_properties = d
        return lab_master

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBasicInfoWithRespect")


@_attrs_define
class UserBasicInfoWithRespect:
    """
    Attributes:
        avatar (None | str | Unset):  Example: /storage/avatars/3453459704ee924e218ba13453453453.png.
        id (int | Unset):  Example: 234234.
        name (str | Unset):  Example: aname.
        is_respected (bool | Unset):
    """

    avatar: None | str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    is_respected: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        id = self.id

        name = self.name

        is_respected = self.is_respected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_respected is not UNSET:
            field_dict["isRespected"] = is_respected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_respected = d.pop("isRespected", UNSET)

        user_basic_info_with_respect = cls(
            avatar=avatar,
            id=id,
            name=name,
            is_respected=is_respected,
        )

        user_basic_info_with_respect.additional_properties = d
        return user_basic_info_with_respect

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewUser")


@_attrs_define
class ReviewUser:
    """
    Attributes:
        avatar (None | str | Unset):  Example: /storage/avatars/3453459704ee924e218ba13453453453.png.
        avatar_url (None | str | Unset):  Example:
            https://cdn.services-k8s.prod.aws.htb.systems/content/machines/avatar/9e4d90d0-845d-476d-bf65-4d861b5e5314.png.
        avatar_thumb_url (None | str | Unset):  Example: https://cdn.services-
            k8s.prod.aws.htb.systems/content/machines/avatar/9e4d90d0-845d-476d-bf65-4d861b5e5314_thumb_64.png.
        id (int | Unset):  Example: 234234.
        name (str | Unset):  Example: aname.
    """

    avatar: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    avatar_thumb_url: None | str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        avatar_thumb_url: None | str | Unset
        if isinstance(self.avatar_thumb_url, Unset):
            avatar_thumb_url = UNSET
        else:
            avatar_thumb_url = self.avatar_thumb_url

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if avatar_thumb_url is not UNSET:
            field_dict["avatar_thumb_url"] = avatar_thumb_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

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

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        def _parse_avatar_thumb_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_thumb_url = _parse_avatar_thumb_url(d.pop("avatar_thumb_url", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        review_user = cls(
            avatar=avatar,
            avatar_url=avatar_url,
            avatar_thumb_url=avatar_thumb_url,
            id=id,
            name=name,
        )

        review_user.additional_properties = d
        return review_user

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

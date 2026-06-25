from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfileTeam")


@_attrs_define
class UserProfileTeam:
    """
    Attributes:
        avatar (str | Unset):
        id (int | Unset):
        name (str | Unset):
        ranking (int | Unset):
        logo_thumb_url (str | Unset):
        member_count (int | Unset):
    """

    avatar: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    ranking: int | Unset = UNSET
    logo_thumb_url: str | Unset = UNSET
    member_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        id = self.id

        name = self.name

        ranking = self.ranking

        logo_thumb_url = self.logo_thumb_url

        member_count = self.member_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ranking is not UNSET:
            field_dict["ranking"] = ranking
        if logo_thumb_url is not UNSET:
            field_dict["logo_thumb_url"] = logo_thumb_url
        if member_count is not UNSET:
            field_dict["member_count"] = member_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ranking = d.pop("ranking", UNSET)

        logo_thumb_url = d.pop("logo_thumb_url", UNSET)

        member_count = d.pop("member_count", UNSET)

        user_profile_team = cls(
            avatar=avatar,
            id=id,
            name=name,
            ranking=ranking,
            logo_thumb_url=logo_thumb_url,
            member_count=member_count,
        )

        user_profile_team.additional_properties = d
        return user_profile_team

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

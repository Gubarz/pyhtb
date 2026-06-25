from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamActivityUser")


@_attrs_define
class TeamActivityUser:
    """
    Attributes:
        id (int):  Example: 1234.
        name (str):  Example: ABC123.
        public (int):
        avatar_thumb (None | str | Unset):  Example: /storage/avatars/sdfgs45345edrgsdfsd374fb23452d_thumb.png.
    """

    id: int
    name: str
    public: int
    avatar_thumb: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        public = self.public

        avatar_thumb: None | str | Unset
        if isinstance(self.avatar_thumb, Unset):
            avatar_thumb = UNSET
        else:
            avatar_thumb = self.avatar_thumb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "public": public,
            }
        )
        if avatar_thumb is not UNSET:
            field_dict["avatar_thumb"] = avatar_thumb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        public = d.pop("public")

        def _parse_avatar_thumb(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_thumb = _parse_avatar_thumb(d.pop("avatar_thumb", UNSET))

        team_activity_user = cls(
            id=id,
            name=name,
            public=public,
            avatar_thumb=avatar_thumb,
        )

        team_activity_user.additional_properties = d
        return team_activity_user

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

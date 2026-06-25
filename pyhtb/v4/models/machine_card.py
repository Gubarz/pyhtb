from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_user import ReviewUser


T = TypeVar("T", bound="MachineCard")


@_attrs_define
class MachineCard:
    """Schema definition for Machine Card

    Attributes:
        avatar (None | str | Unset):  Example: /storage/avatars/a2c2bd7b4e98ff8b782ed590896305a1.png.
        difficulty_text (str | Unset):  Example: Medium.
        id (int | Unset):  Example: 601.
        is_todo (bool | Unset):
        maker (None | ReviewUser | Unset):
        maker2 (None | ReviewUser | Unset):
        name (str | Unset):  Example: SolarLab.
        os (str | Unset):  Example: Windows.
        points (int | Unset):  Example: 30.
        release (datetime.datetime | Unset):  Example: 2024-05-11T16:00:00.000000Z.
        retired (int | Unset):
        retired_id (int | Unset):
        type_card (str | Unset):  Example: seasonal.
    """

    avatar: None | str | Unset = UNSET
    difficulty_text: str | Unset = UNSET
    id: int | Unset = UNSET
    is_todo: bool | Unset = UNSET
    maker: None | ReviewUser | Unset = UNSET
    maker2: None | ReviewUser | Unset = UNSET
    name: str | Unset = UNSET
    os: str | Unset = UNSET
    points: int | Unset = UNSET
    release: datetime.datetime | Unset = UNSET
    retired: int | Unset = UNSET
    retired_id: int | Unset = UNSET
    type_card: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.review_user import ReviewUser

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        difficulty_text = self.difficulty_text

        id = self.id

        is_todo = self.is_todo

        maker: dict[str, Any] | None | Unset
        if isinstance(self.maker, Unset):
            maker = UNSET
        elif isinstance(self.maker, ReviewUser):
            maker = self.maker.to_dict()
        else:
            maker = self.maker

        maker2: dict[str, Any] | None | Unset
        if isinstance(self.maker2, Unset):
            maker2 = UNSET
        elif isinstance(self.maker2, ReviewUser):
            maker2 = self.maker2.to_dict()
        else:
            maker2 = self.maker2

        name = self.name

        os = self.os

        points = self.points

        release: str | Unset = UNSET
        if not isinstance(self.release, Unset):
            release = self.release.isoformat()

        retired = self.retired

        retired_id = self.retired_id

        type_card = self.type_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if difficulty_text is not UNSET:
            field_dict["difficultyText"] = difficulty_text
        if id is not UNSET:
            field_dict["id"] = id
        if is_todo is not UNSET:
            field_dict["isTodo"] = is_todo
        if maker is not UNSET:
            field_dict["maker"] = maker
        if maker2 is not UNSET:
            field_dict["maker2"] = maker2
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if points is not UNSET:
            field_dict["points"] = points
        if release is not UNSET:
            field_dict["release"] = release
        if retired is not UNSET:
            field_dict["retired"] = retired
        if retired_id is not UNSET:
            field_dict["retired_id"] = retired_id
        if type_card is not UNSET:
            field_dict["typeCard"] = type_card

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_user import ReviewUser

        d = dict(src_dict)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        difficulty_text = d.pop("difficultyText", UNSET)

        id = d.pop("id", UNSET)

        is_todo = d.pop("isTodo", UNSET)

        def _parse_maker(data: object) -> None | ReviewUser | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_basic_info_type_0 = ReviewUser.from_dict(data)

                return componentsschemas_user_basic_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewUser | Unset, data)

        maker = _parse_maker(d.pop("maker", UNSET))

        def _parse_maker2(data: object) -> None | ReviewUser | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_basic_info_type_0 = ReviewUser.from_dict(data)

                return componentsschemas_user_basic_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewUser | Unset, data)

        maker2 = _parse_maker2(d.pop("maker2", UNSET))

        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        points = d.pop("points", UNSET)

        _release = d.pop("release", UNSET)
        release: datetime.datetime | Unset
        if isinstance(_release, Unset):
            release = UNSET
        else:
            release = datetime.datetime.fromisoformat(_release)

        retired = d.pop("retired", UNSET)

        retired_id = d.pop("retired_id", UNSET)

        type_card = d.pop("typeCard", UNSET)

        machine_card = cls(
            avatar=avatar,
            difficulty_text=difficulty_text,
            id=id,
            is_todo=is_todo,
            maker=maker,
            maker2=maker2,
            name=name,
            os=os,
            points=points,
            release=release,
            retired=retired,
            retired_id=retired_id,
            type_card=type_card,
        )

        machine_card.additional_properties = d
        return machine_card

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_activity_user import TeamActivityUser


T = TypeVar("T", bound="TeamActivityItem")


@_attrs_define
class TeamActivityItem:
    """
    Attributes:
        date (datetime.datetime):  Example: 2024-11-20T22:36:18.000000Z.
        date_diff (str):  Example: 10 hours ago.
        first_blood (bool):
        id (int):  Example: 9.
        name (str):  Example: Arctic.
        object_type (str):  Example: machine.
        points (int):
        type_ (str):  Example: user.
        user (TeamActivityUser):
        challenge_category (str | Unset):
        flag_title (str | Unset):
        machine_avatar (str | Unset):  Example: /storage/avatars/0d6275efbd5e48fcdc96e61b9724ae5e_thumb.png.
        avatar_url (str | Unset):
    """

    date: datetime.datetime
    date_diff: str
    first_blood: bool
    id: int
    name: str
    object_type: str
    points: int
    type_: str
    user: TeamActivityUser
    challenge_category: str | Unset = UNSET
    flag_title: str | Unset = UNSET
    machine_avatar: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        date_diff = self.date_diff

        first_blood = self.first_blood

        id = self.id

        name = self.name

        object_type = self.object_type

        points = self.points

        type_ = self.type_

        user = self.user.to_dict()

        challenge_category = self.challenge_category

        flag_title = self.flag_title

        machine_avatar = self.machine_avatar

        avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "date_diff": date_diff,
                "first_blood": first_blood,
                "id": id,
                "name": name,
                "object_type": object_type,
                "points": points,
                "type": type_,
                "user": user,
            }
        )
        if challenge_category is not UNSET:
            field_dict["challenge_category"] = challenge_category
        if flag_title is not UNSET:
            field_dict["flag_title"] = flag_title
        if machine_avatar is not UNSET:
            field_dict["machine_avatar"] = machine_avatar
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_activity_user import TeamActivityUser

        d = dict(src_dict)
        date = datetime.datetime.fromisoformat(d.pop("date"))

        date_diff = d.pop("date_diff")

        first_blood = d.pop("first_blood")

        id = d.pop("id")

        name = d.pop("name")

        object_type = d.pop("object_type")

        points = d.pop("points")

        type_ = d.pop("type")

        user = TeamActivityUser.from_dict(d.pop("user"))

        challenge_category = d.pop("challenge_category", UNSET)

        flag_title = d.pop("flag_title", UNSET)

        machine_avatar = d.pop("machine_avatar", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        team_activity_item = cls(
            date=date,
            date_diff=date_diff,
            first_blood=first_blood,
            id=id,
            name=name,
            object_type=object_type,
            points=points,
            type_=type_,
            user=user,
            challenge_category=challenge_category,
            flag_title=flag_title,
            machine_avatar=machine_avatar,
            avatar_url=avatar_url,
        )

        team_activity_item.additional_properties = d
        return team_activity_item

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

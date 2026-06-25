from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_profile_activity_prolab_type import UserProfileActivityProlabType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfileActivityProlab")


@_attrs_define
class UserProfileActivityProlab:
    """
    Attributes:
        type_ (UserProfileActivityProlabType):
        id (int):
        name (str):
        points (int):
        own_date (datetime.datetime):
        prolab_id (int):
        prolab_name (str):
        prolab_identifier (str):
        avatar (str | Unset):
        blood (bool | None | Unset):
    """

    type_: UserProfileActivityProlabType
    id: int
    name: str
    points: int
    own_date: datetime.datetime
    prolab_id: int
    prolab_name: str
    prolab_identifier: str
    avatar: str | Unset = UNSET
    blood: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        name = self.name

        points = self.points

        own_date = self.own_date.isoformat()

        prolab_id = self.prolab_id

        prolab_name = self.prolab_name

        prolab_identifier = self.prolab_identifier

        avatar = self.avatar

        blood: bool | None | Unset
        if isinstance(self.blood, Unset):
            blood = UNSET
        else:
            blood = self.blood

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "points": points,
                "ownDate": own_date,
                "prolabId": prolab_id,
                "prolabName": prolab_name,
                "prolabIdentifier": prolab_identifier,
            }
        )
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if blood is not UNSET:
            field_dict["blood"] = blood

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = UserProfileActivityProlabType(d.pop("type"))

        id = d.pop("id")

        name = d.pop("name")

        points = d.pop("points")

        own_date = datetime.datetime.fromisoformat(d.pop("ownDate"))

        prolab_id = d.pop("prolabId")

        prolab_name = d.pop("prolabName")

        prolab_identifier = d.pop("prolabIdentifier")

        avatar = d.pop("avatar", UNSET)

        def _parse_blood(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        blood = _parse_blood(d.pop("blood", UNSET))

        user_profile_activity_prolab = cls(
            type_=type_,
            id=id,
            name=name,
            points=points,
            own_date=own_date,
            prolab_id=prolab_id,
            prolab_name=prolab_name,
            prolab_identifier=prolab_identifier,
            avatar=avatar,
            blood=blood,
        )

        user_profile_activity_prolab.additional_properties = d
        return user_profile_activity_prolab

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

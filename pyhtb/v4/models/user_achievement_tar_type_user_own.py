from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAchievementTarTypeUserOwn")


@_attrs_define
class UserAchievementTarTypeUserOwn:
    """
    Attributes:
        date (str | Unset):  Example: 14 Jul 2024.
        date_iso8601 (datetime.datetime | Unset):  Example: 2024-07-14T06:51:22+00:00.
        points (int | Unset):
        rank (int | Unset):
        experience_points (int | Unset):
    """

    date: str | Unset = UNSET
    date_iso8601: datetime.datetime | Unset = UNSET
    points: int | Unset = UNSET
    rank: int | Unset = UNSET
    experience_points: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        date_iso8601: str | Unset = UNSET
        if not isinstance(self.date_iso8601, Unset):
            date_iso8601 = self.date_iso8601.isoformat()

        points = self.points

        rank = self.rank

        experience_points = self.experience_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if date_iso8601 is not UNSET:
            field_dict["date_iso8601"] = date_iso8601
        if points is not UNSET:
            field_dict["points"] = points
        if rank is not UNSET:
            field_dict["rank"] = rank
        if experience_points is not UNSET:
            field_dict["experience_points"] = experience_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        _date_iso8601 = d.pop("date_iso8601", UNSET)
        date_iso8601: datetime.datetime | Unset
        if isinstance(_date_iso8601, Unset):
            date_iso8601 = UNSET
        else:
            date_iso8601 = datetime.datetime.fromisoformat(_date_iso8601)

        points = d.pop("points", UNSET)

        rank = d.pop("rank", UNSET)

        experience_points = d.pop("experience_points", UNSET)

        user_achievement_tar_type_user_own = cls(
            date=date,
            date_iso8601=date_iso8601,
            points=points,
            rank=rank,
            experience_points=experience_points,
        )

        user_achievement_tar_type_user_own.additional_properties = d
        return user_achievement_tar_type_user_own

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

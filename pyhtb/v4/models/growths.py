from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Growths")


@_attrs_define
class Growths:
    """
    Attributes:
        compared_to_date (datetime.datetime | Unset):
        points (int | Unset):
        points_growth (str | Unset):
        previous_points (int | Unset):
        previous_rank (int | Unset):
        rank (int | Unset):
        rank_growth (str | Unset):
    """

    compared_to_date: datetime.datetime | Unset = UNSET
    points: int | Unset = UNSET
    points_growth: str | Unset = UNSET
    previous_points: int | Unset = UNSET
    previous_rank: int | Unset = UNSET
    rank: int | Unset = UNSET
    rank_growth: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compared_to_date: str | Unset = UNSET
        if not isinstance(self.compared_to_date, Unset):
            compared_to_date = self.compared_to_date.isoformat()

        points = self.points

        points_growth = self.points_growth

        previous_points = self.previous_points

        previous_rank = self.previous_rank

        rank = self.rank

        rank_growth = self.rank_growth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compared_to_date is not UNSET:
            field_dict["compared_to_date"] = compared_to_date
        if points is not UNSET:
            field_dict["points"] = points
        if points_growth is not UNSET:
            field_dict["points_growth"] = points_growth
        if previous_points is not UNSET:
            field_dict["previous_points"] = previous_points
        if previous_rank is not UNSET:
            field_dict["previous_rank"] = previous_rank
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_growth is not UNSET:
            field_dict["rank_growth"] = rank_growth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _compared_to_date = d.pop("compared_to_date", UNSET)
        compared_to_date: datetime.datetime | Unset
        if isinstance(_compared_to_date, Unset):
            compared_to_date = UNSET
        else:
            compared_to_date = datetime.datetime.fromisoformat(_compared_to_date)

        points = d.pop("points", UNSET)

        points_growth = d.pop("points_growth", UNSET)

        previous_points = d.pop("previous_points", UNSET)

        previous_rank = d.pop("previous_rank", UNSET)

        rank = d.pop("rank", UNSET)

        rank_growth = d.pop("rank_growth", UNSET)

        growths = cls(
            compared_to_date=compared_to_date,
            points=points,
            points_growth=points_growth,
            previous_points=previous_points,
            previous_rank=previous_rank,
            rank=rank,
            rank_growth=rank_growth,
        )

        growths.additional_properties = d
        return growths

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

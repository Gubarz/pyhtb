from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RankingGraphStats")


@_attrs_define
class RankingGraphStats:
    """
    Attributes:
        chart_data (list[int] | None | Unset):
        points_diff (int | Unset):
        points_growth (str | Unset):
        ranks_diff (int | Unset):
    """

    chart_data: list[int] | None | Unset = UNSET
    points_diff: int | Unset = UNSET
    points_growth: str | Unset = UNSET
    ranks_diff: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chart_data: list[int] | None | Unset
        if isinstance(self.chart_data, Unset):
            chart_data = UNSET
        elif isinstance(self.chart_data, list):
            chart_data = self.chart_data

        else:
            chart_data = self.chart_data

        points_diff = self.points_diff

        points_growth = self.points_growth

        ranks_diff = self.ranks_diff

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chart_data is not UNSET:
            field_dict["chart_data"] = chart_data
        if points_diff is not UNSET:
            field_dict["points_diff"] = points_diff
        if points_growth is not UNSET:
            field_dict["points_growth"] = points_growth
        if ranks_diff is not UNSET:
            field_dict["ranks_diff"] = ranks_diff

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_chart_data(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_int_array_type_0 = cast(list[int], data)

                return componentsschemas_int_array_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        chart_data = _parse_chart_data(d.pop("chart_data", UNSET))

        points_diff = d.pop("points_diff", UNSET)

        points_growth = d.pop("points_growth", UNSET)

        ranks_diff = d.pop("ranks_diff", UNSET)

        ranking_graph_stats = cls(
            chart_data=chart_data,
            points_diff=points_diff,
            points_growth=points_growth,
            ranks_diff=ranks_diff,
        )

        ranking_graph_stats.additional_properties = d
        return ranking_graph_stats

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

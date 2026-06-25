from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UniversityStatsResponse")


@_attrs_define
class UniversityStatsResponse:
    """Schema definition for University Stats responses

    Attributes:
        rank (str):
        total_points (int):
        members (int):
        respects (int):
        machine_solves (int):
        challenge_solves (int):
        sherlock_solves (int):
        total_bloods (int):
    """

    rank: str
    total_points: int
    members: int
    respects: int
    machine_solves: int
    challenge_solves: int
    sherlock_solves: int
    total_bloods: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        total_points = self.total_points

        members = self.members

        respects = self.respects

        machine_solves = self.machine_solves

        challenge_solves = self.challenge_solves

        sherlock_solves = self.sherlock_solves

        total_bloods = self.total_bloods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
                "total_points": total_points,
                "members": members,
                "respects": respects,
                "machine_solves": machine_solves,
                "challenge_solves": challenge_solves,
                "sherlock_solves": sherlock_solves,
                "total_bloods": total_bloods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rank = d.pop("rank")

        total_points = d.pop("total_points")

        members = d.pop("members")

        respects = d.pop("respects")

        machine_solves = d.pop("machine_solves")

        challenge_solves = d.pop("challenge_solves")

        sherlock_solves = d.pop("sherlock_solves")

        total_bloods = d.pop("total_bloods")

        university_stats_response = cls(
            rank=rank,
            total_points=total_points,
            members=members,
            respects=respects,
            machine_solves=machine_solves,
            challenge_solves=challenge_solves,
            sherlock_solves=sherlock_solves,
            total_bloods=total_bloods,
        )

        university_stats_response.additional_properties = d
        return university_stats_response

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

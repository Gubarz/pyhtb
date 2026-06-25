from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RankingsUniversitiesItem")


@_attrs_define
class RankingsUniversitiesItem:
    """
    Attributes:
        challenge_bloods (int | Unset):
        challenge_owns (int | Unset):
        country (str | Unset):
        fortress (int | Unset):
        id (int | Unset):
        name (str | Unset):
        points (int | Unset):
        rank (int | Unset):
        ranks_diff (int | None | Unset):
        root_bloods (int | Unset):
        root_owns (int | Unset):
        students (int | Unset):
        user_bloods (int | Unset):
        user_owns (int | Unset):
    """

    challenge_bloods: int | Unset = UNSET
    challenge_owns: int | Unset = UNSET
    country: str | Unset = UNSET
    fortress: int | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    points: int | Unset = UNSET
    rank: int | Unset = UNSET
    ranks_diff: int | None | Unset = UNSET
    root_bloods: int | Unset = UNSET
    root_owns: int | Unset = UNSET
    students: int | Unset = UNSET
    user_bloods: int | Unset = UNSET
    user_owns: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_bloods = self.challenge_bloods

        challenge_owns = self.challenge_owns

        country = self.country

        fortress = self.fortress

        id = self.id

        name = self.name

        points = self.points

        rank = self.rank

        ranks_diff: int | None | Unset
        if isinstance(self.ranks_diff, Unset):
            ranks_diff = UNSET
        else:
            ranks_diff = self.ranks_diff

        root_bloods = self.root_bloods

        root_owns = self.root_owns

        students = self.students

        user_bloods = self.user_bloods

        user_owns = self.user_owns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge_bloods is not UNSET:
            field_dict["challenge_bloods"] = challenge_bloods
        if challenge_owns is not UNSET:
            field_dict["challenge_owns"] = challenge_owns
        if country is not UNSET:
            field_dict["country"] = country
        if fortress is not UNSET:
            field_dict["fortress"] = fortress
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if points is not UNSET:
            field_dict["points"] = points
        if rank is not UNSET:
            field_dict["rank"] = rank
        if ranks_diff is not UNSET:
            field_dict["ranks_diff"] = ranks_diff
        if root_bloods is not UNSET:
            field_dict["root_bloods"] = root_bloods
        if root_owns is not UNSET:
            field_dict["root_owns"] = root_owns
        if students is not UNSET:
            field_dict["students"] = students
        if user_bloods is not UNSET:
            field_dict["user_bloods"] = user_bloods
        if user_owns is not UNSET:
            field_dict["user_owns"] = user_owns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge_bloods = d.pop("challenge_bloods", UNSET)

        challenge_owns = d.pop("challenge_owns", UNSET)

        country = d.pop("country", UNSET)

        fortress = d.pop("fortress", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        points = d.pop("points", UNSET)

        rank = d.pop("rank", UNSET)

        def _parse_ranks_diff(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ranks_diff = _parse_ranks_diff(d.pop("ranks_diff", UNSET))

        root_bloods = d.pop("root_bloods", UNSET)

        root_owns = d.pop("root_owns", UNSET)

        students = d.pop("students", UNSET)

        user_bloods = d.pop("user_bloods", UNSET)

        user_owns = d.pop("user_owns", UNSET)

        rankings_universities_item = cls(
            challenge_bloods=challenge_bloods,
            challenge_owns=challenge_owns,
            country=country,
            fortress=fortress,
            id=id,
            name=name,
            points=points,
            rank=rank,
            ranks_diff=ranks_diff,
            root_bloods=root_bloods,
            root_owns=root_owns,
            students=students,
            user_bloods=user_bloods,
            user_owns=user_owns,
        )

        rankings_universities_item.additional_properties = d
        return rankings_universities_item

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

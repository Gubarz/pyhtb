from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_ranking_type_1 import UserRankingType1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_ranking import UserRanking


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        avatar_thumb (str | Unset):
        id (int | Unset):
        name (str | Unset):
        points (int | Unset):
        rank_name (str | Unset):
        ranking (int | Unset | UserRankingType1):
        rankings (list[UserRanking] | Unset):
        respected_by_count (int | Unset):
        root_owns_count (int | Unset):
        user_owns_count (int | Unset):
    """

    avatar_thumb: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    points: int | Unset = UNSET
    rank_name: str | Unset = UNSET
    ranking: int | Unset | UserRankingType1 = UNSET
    rankings: list[UserRanking] | Unset = UNSET
    respected_by_count: int | Unset = UNSET
    root_owns_count: int | Unset = UNSET
    user_owns_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_thumb = self.avatar_thumb

        id = self.id

        name = self.name

        points = self.points

        rank_name = self.rank_name

        ranking: int | str | Unset
        if isinstance(self.ranking, Unset):
            ranking = UNSET
        elif isinstance(self.ranking, UserRankingType1):
            ranking = self.ranking.value
        else:
            ranking = self.ranking

        rankings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rankings, Unset):
            rankings = []
            for rankings_item_data in self.rankings:
                rankings_item = rankings_item_data.to_dict()
                rankings.append(rankings_item)

        respected_by_count = self.respected_by_count

        root_owns_count = self.root_owns_count

        user_owns_count = self.user_owns_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_thumb is not UNSET:
            field_dict["avatar_thumb"] = avatar_thumb
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if points is not UNSET:
            field_dict["points"] = points
        if rank_name is not UNSET:
            field_dict["rank_name"] = rank_name
        if ranking is not UNSET:
            field_dict["ranking"] = ranking
        if rankings is not UNSET:
            field_dict["rankings"] = rankings
        if respected_by_count is not UNSET:
            field_dict["respected_by_count"] = respected_by_count
        if root_owns_count is not UNSET:
            field_dict["root_owns_count"] = root_owns_count
        if user_owns_count is not UNSET:
            field_dict["user_owns_count"] = user_owns_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_ranking import UserRanking

        d = dict(src_dict)
        avatar_thumb = d.pop("avatar_thumb", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        points = d.pop("points", UNSET)

        rank_name = d.pop("rank_name", UNSET)

        def _parse_ranking(data: object) -> int | Unset | UserRankingType1:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ranking_type_1 = UserRankingType1(data)

                return ranking_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(int | Unset | UserRankingType1, data)

        ranking = _parse_ranking(d.pop("ranking", UNSET))

        _rankings = d.pop("rankings", UNSET)
        rankings: list[UserRanking] | Unset = UNSET
        if _rankings is not UNSET:
            rankings = []
            for rankings_item_data in _rankings:
                rankings_item = UserRanking.from_dict(rankings_item_data)

                rankings.append(rankings_item)

        respected_by_count = d.pop("respected_by_count", UNSET)

        root_owns_count = d.pop("root_owns_count", UNSET)

        user_owns_count = d.pop("user_owns_count", UNSET)

        user = cls(
            avatar_thumb=avatar_thumb,
            id=id,
            name=name,
            points=points,
            rank_name=rank_name,
            ranking=ranking,
            rankings=rankings,
            respected_by_count=respected_by_count,
            root_owns_count=root_owns_count,
            user_owns_count=user_owns_count,
        )

        user.additional_properties = d
        return user

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

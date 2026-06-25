from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flags_to_next_rank_type_0 import FlagsToNextRankType0
    from ..models.next_rank import NextRank
    from ..models.season_user_rank_data_total_season_flags import (
        SeasonUserRankDataTotalSeasonFlags,
    )


T = TypeVar("T", bound="SeasonUserRankData")


@_attrs_define
class SeasonUserRankData:
    """
    Attributes:
        flags_to_next_rank (FlagsToNextRankType0 | list[Any] | Unset):
        league (str | Unset):
        rank (int | Unset):
        rank_suffix (str | Unset):
        total_ranks (int | Unset):
        total_season_points (int | Unset):
        next_rank (NextRank | Unset):
        root_owns (int | Unset):
        root_bloods (int | Unset):
        user_owns (int | Unset):
        user_bloods (int | Unset):
        total_season_flags (SeasonUserRankDataTotalSeasonFlags | Unset):
        total_season_bloods (int | Unset):
        season_content_id (str | Unset):
    """

    flags_to_next_rank: FlagsToNextRankType0 | list[Any] | Unset = UNSET
    league: str | Unset = UNSET
    rank: int | Unset = UNSET
    rank_suffix: str | Unset = UNSET
    total_ranks: int | Unset = UNSET
    total_season_points: int | Unset = UNSET
    next_rank: NextRank | Unset = UNSET
    root_owns: int | Unset = UNSET
    root_bloods: int | Unset = UNSET
    user_owns: int | Unset = UNSET
    user_bloods: int | Unset = UNSET
    total_season_flags: SeasonUserRankDataTotalSeasonFlags | Unset = UNSET
    total_season_bloods: int | Unset = UNSET
    season_content_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flags_to_next_rank_type_0 import FlagsToNextRankType0

        flags_to_next_rank: dict[str, Any] | list[Any] | Unset
        if isinstance(self.flags_to_next_rank, Unset):
            flags_to_next_rank = UNSET
        elif isinstance(self.flags_to_next_rank, FlagsToNextRankType0):
            flags_to_next_rank = self.flags_to_next_rank.to_dict()
        else:
            flags_to_next_rank = self.flags_to_next_rank

        league = self.league

        rank = self.rank

        rank_suffix = self.rank_suffix

        total_ranks = self.total_ranks

        total_season_points = self.total_season_points

        next_rank: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_rank, Unset):
            next_rank = self.next_rank.to_dict()

        root_owns = self.root_owns

        root_bloods = self.root_bloods

        user_owns = self.user_owns

        user_bloods = self.user_bloods

        total_season_flags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_season_flags, Unset):
            total_season_flags = self.total_season_flags.to_dict()

        total_season_bloods = self.total_season_bloods

        season_content_id = self.season_content_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flags_to_next_rank is not UNSET:
            field_dict["flags_to_next_rank"] = flags_to_next_rank
        if league is not UNSET:
            field_dict["league"] = league
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_suffix is not UNSET:
            field_dict["rank_suffix"] = rank_suffix
        if total_ranks is not UNSET:
            field_dict["total_ranks"] = total_ranks
        if total_season_points is not UNSET:
            field_dict["total_season_points"] = total_season_points
        if next_rank is not UNSET:
            field_dict["next_rank"] = next_rank
        if root_owns is not UNSET:
            field_dict["root_owns"] = root_owns
        if root_bloods is not UNSET:
            field_dict["root_bloods"] = root_bloods
        if user_owns is not UNSET:
            field_dict["user_owns"] = user_owns
        if user_bloods is not UNSET:
            field_dict["user_bloods"] = user_bloods
        if total_season_flags is not UNSET:
            field_dict["total_season_flags"] = total_season_flags
        if total_season_bloods is not UNSET:
            field_dict["total_season_bloods"] = total_season_bloods
        if season_content_id is not UNSET:
            field_dict["season_content_id"] = season_content_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flags_to_next_rank_type_0 import FlagsToNextRankType0
        from ..models.next_rank import NextRank
        from ..models.season_user_rank_data_total_season_flags import (
            SeasonUserRankDataTotalSeasonFlags,
        )

        d = dict(src_dict)

        def _parse_flags_to_next_rank(
            data: object,
        ) -> FlagsToNextRankType0 | list[Any] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_flags_to_next_rank_type_0 = (
                    FlagsToNextRankType0.from_dict(data)
                )

                return componentsschemas_flags_to_next_rank_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            componentsschemas_flags_to_next_rank_type_1 = cast(list[Any], data)

            return componentsschemas_flags_to_next_rank_type_1

        flags_to_next_rank = _parse_flags_to_next_rank(
            d.pop("flags_to_next_rank", UNSET)
        )

        league = d.pop("league", UNSET)

        rank = d.pop("rank", UNSET)

        rank_suffix = d.pop("rank_suffix", UNSET)

        total_ranks = d.pop("total_ranks", UNSET)

        total_season_points = d.pop("total_season_points", UNSET)

        _next_rank = d.pop("next_rank", UNSET)
        next_rank: NextRank | Unset
        if isinstance(_next_rank, Unset):
            next_rank = UNSET
        else:
            next_rank = NextRank.from_dict(_next_rank)

        root_owns = d.pop("root_owns", UNSET)

        root_bloods = d.pop("root_bloods", UNSET)

        user_owns = d.pop("user_owns", UNSET)

        user_bloods = d.pop("user_bloods", UNSET)

        _total_season_flags = d.pop("total_season_flags", UNSET)
        total_season_flags: SeasonUserRankDataTotalSeasonFlags | Unset
        if isinstance(_total_season_flags, Unset):
            total_season_flags = UNSET
        else:
            total_season_flags = SeasonUserRankDataTotalSeasonFlags.from_dict(
                _total_season_flags
            )

        total_season_bloods = d.pop("total_season_bloods", UNSET)

        season_content_id = d.pop("season_content_id", UNSET)

        season_user_rank_data = cls(
            flags_to_next_rank=flags_to_next_rank,
            league=league,
            rank=rank,
            rank_suffix=rank_suffix,
            total_ranks=total_ranks,
            total_season_points=total_season_points,
            next_rank=next_rank,
            root_owns=root_owns,
            root_bloods=root_bloods,
            user_owns=user_owns,
            user_bloods=user_bloods,
            total_season_flags=total_season_flags,
            total_season_bloods=total_season_bloods,
            season_content_id=season_content_id,
        )

        season_user_rank_data.additional_properties = d
        return season_user_rank_data

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.growths import Growths
    from ..models.profile_user_team_info import ProfileUserTeamInfo
    from ..models.ranking_graph_stats import RankingGraphStats


T = TypeVar("T", bound="ProfileUserStats")


@_attrs_define
class ProfileUserStats:
    """
    Attributes:
        current_rank_progress (float | Unset):
        growths (Growths | Unset):
        id (int | Unset):
        name (str | Unset):
        next_rank (str | Unset):
        next_rank_points (float | Unset):
        points (int | Unset):
        rank (str | Unset):
        rank_id (int | Unset):
        rank_ownership (float | Unset):
        rank_requirement (int | Unset):
        ranking (int | Unset):
        ranking_graph_stats (RankingGraphStats | Unset):
        respects (int | Unset):
        sso_id (bool | Unset):
        subscription (str | Unset):
        system_bloods (int | Unset):
        system_owns (int | Unset):
        team (ProfileUserTeamInfo | Unset):
        university_name (None | str | Unset):
        user_bloods (int | Unset):
        user_owns (int | Unset):
        challenge_bloods (int | Unset):
    """

    current_rank_progress: float | Unset = UNSET
    growths: Growths | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    next_rank: str | Unset = UNSET
    next_rank_points: float | Unset = UNSET
    points: int | Unset = UNSET
    rank: str | Unset = UNSET
    rank_id: int | Unset = UNSET
    rank_ownership: float | Unset = UNSET
    rank_requirement: int | Unset = UNSET
    ranking: int | Unset = UNSET
    ranking_graph_stats: RankingGraphStats | Unset = UNSET
    respects: int | Unset = UNSET
    sso_id: bool | Unset = UNSET
    subscription: str | Unset = UNSET
    system_bloods: int | Unset = UNSET
    system_owns: int | Unset = UNSET
    team: ProfileUserTeamInfo | Unset = UNSET
    university_name: None | str | Unset = UNSET
    user_bloods: int | Unset = UNSET
    user_owns: int | Unset = UNSET
    challenge_bloods: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_rank_progress = self.current_rank_progress

        growths: dict[str, Any] | Unset = UNSET
        if not isinstance(self.growths, Unset):
            growths = self.growths.to_dict()

        id = self.id

        name = self.name

        next_rank = self.next_rank

        next_rank_points = self.next_rank_points

        points = self.points

        rank = self.rank

        rank_id = self.rank_id

        rank_ownership = self.rank_ownership

        rank_requirement = self.rank_requirement

        ranking = self.ranking

        ranking_graph_stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ranking_graph_stats, Unset):
            ranking_graph_stats = self.ranking_graph_stats.to_dict()

        respects = self.respects

        sso_id = self.sso_id

        subscription = self.subscription

        system_bloods = self.system_bloods

        system_owns = self.system_owns

        team: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        university_name: None | str | Unset
        if isinstance(self.university_name, Unset):
            university_name = UNSET
        else:
            university_name = self.university_name

        user_bloods = self.user_bloods

        user_owns = self.user_owns

        challenge_bloods = self.challenge_bloods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_rank_progress is not UNSET:
            field_dict["current_rank_progress"] = current_rank_progress
        if growths is not UNSET:
            field_dict["growths"] = growths
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if next_rank is not UNSET:
            field_dict["next_rank"] = next_rank
        if next_rank_points is not UNSET:
            field_dict["next_rank_points"] = next_rank_points
        if points is not UNSET:
            field_dict["points"] = points
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_id is not UNSET:
            field_dict["rank_id"] = rank_id
        if rank_ownership is not UNSET:
            field_dict["rank_ownership"] = rank_ownership
        if rank_requirement is not UNSET:
            field_dict["rank_requirement"] = rank_requirement
        if ranking is not UNSET:
            field_dict["ranking"] = ranking
        if ranking_graph_stats is not UNSET:
            field_dict["rankingGraphStats"] = ranking_graph_stats
        if respects is not UNSET:
            field_dict["respects"] = respects
        if sso_id is not UNSET:
            field_dict["sso_id"] = sso_id
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if system_bloods is not UNSET:
            field_dict["system_bloods"] = system_bloods
        if system_owns is not UNSET:
            field_dict["system_owns"] = system_owns
        if team is not UNSET:
            field_dict["team"] = team
        if university_name is not UNSET:
            field_dict["university_name"] = university_name
        if user_bloods is not UNSET:
            field_dict["user_bloods"] = user_bloods
        if user_owns is not UNSET:
            field_dict["user_owns"] = user_owns
        if challenge_bloods is not UNSET:
            field_dict["challenge_bloods"] = challenge_bloods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.growths import Growths
        from ..models.profile_user_team_info import ProfileUserTeamInfo
        from ..models.ranking_graph_stats import RankingGraphStats

        d = dict(src_dict)
        current_rank_progress = d.pop("current_rank_progress", UNSET)

        _growths = d.pop("growths", UNSET)
        growths: Growths | Unset
        if isinstance(_growths, Unset):
            growths = UNSET
        else:
            growths = Growths.from_dict(_growths)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        next_rank = d.pop("next_rank", UNSET)

        next_rank_points = d.pop("next_rank_points", UNSET)

        points = d.pop("points", UNSET)

        rank = d.pop("rank", UNSET)

        rank_id = d.pop("rank_id", UNSET)

        rank_ownership = d.pop("rank_ownership", UNSET)

        rank_requirement = d.pop("rank_requirement", UNSET)

        ranking = d.pop("ranking", UNSET)

        _ranking_graph_stats = d.pop("rankingGraphStats", UNSET)
        ranking_graph_stats: RankingGraphStats | Unset
        if isinstance(_ranking_graph_stats, Unset):
            ranking_graph_stats = UNSET
        else:
            ranking_graph_stats = RankingGraphStats.from_dict(_ranking_graph_stats)

        respects = d.pop("respects", UNSET)

        sso_id = d.pop("sso_id", UNSET)

        subscription = d.pop("subscription", UNSET)

        system_bloods = d.pop("system_bloods", UNSET)

        system_owns = d.pop("system_owns", UNSET)

        _team = d.pop("team", UNSET)
        team: ProfileUserTeamInfo | Unset
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = ProfileUserTeamInfo.from_dict(_team)

        def _parse_university_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        university_name = _parse_university_name(d.pop("university_name", UNSET))

        user_bloods = d.pop("user_bloods", UNSET)

        user_owns = d.pop("user_owns", UNSET)

        challenge_bloods = d.pop("challenge_bloods", UNSET)

        profile_user_stats = cls(
            current_rank_progress=current_rank_progress,
            growths=growths,
            id=id,
            name=name,
            next_rank=next_rank,
            next_rank_points=next_rank_points,
            points=points,
            rank=rank,
            rank_id=rank_id,
            rank_ownership=rank_ownership,
            rank_requirement=rank_requirement,
            ranking=ranking,
            ranking_graph_stats=ranking_graph_stats,
            respects=respects,
            sso_id=sso_id,
            subscription=subscription,
            system_bloods=system_bloods,
            system_owns=system_owns,
            team=team,
            university_name=university_name,
            user_bloods=user_bloods,
            user_owns=user_owns,
            challenge_bloods=challenge_bloods,
        )

        profile_user_stats.additional_properties = d
        return profile_user_stats

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

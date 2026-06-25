from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_profile_team import UserProfileTeam
    from ..models.user_profile_university_team_type_0 import (
        UserProfileUniversityTeamType0,
    )


T = TypeVar("T", bound="UserProfile")


@_attrs_define
class UserProfile:
    """
    Attributes:
        avatar (str | Unset):
        country_code (str | Unset):
        country_name (str | Unset):
        current_rank_progress (float | None | Unset):
        github (None | str | Unset):
        id (int | Unset):
        is_dedicated_vip (bool | Unset):
        is_followed (bool | Unset):
        is_respected (bool | Unset):
        is_vip (bool | Unset):
        linkedin (None | str | Unset):
        name (str | Unset):
        next_rank (None | str | Unset):
        next_rank_points (float | None | Unset):
        points (int | Unset):
        public (bool | Unset):
        rank (str | Unset):
        rank_id (int | Unset):
        rank_ownership (float | Unset):
        rank_requirement (int | None | Unset):
        ranking (int | Unset):
        respects (int | Unset):
        sso_id (bool | Unset):
        system_bloods (int | Unset):
        system_owns (int | Unset):
        team (UserProfileTeam | Unset):
        timezone (str | Unset):
        twitter (None | str | Unset):
        university (None | Unset | UserProfileUniversityTeamType0):
        university_name (None | str | Unset):
        user_bloods (int | Unset):
        user_owns (int | Unset):
        followed_by_count (int | Unset):
        user_respects (int | Unset):
        joined_date (datetime.datetime | Unset):
        user_follows (int | Unset):
        challenge_bloods (int | Unset):
        full_name (str | Unset):
        cv (None | str | Unset):
        cpe_id (int | None | Unset):
        phone_number (None | str | Unset):
        server (None | str | Unset):
        account_id (str | Unset):
    """

    avatar: str | Unset = UNSET
    country_code: str | Unset = UNSET
    country_name: str | Unset = UNSET
    current_rank_progress: float | None | Unset = UNSET
    github: None | str | Unset = UNSET
    id: int | Unset = UNSET
    is_dedicated_vip: bool | Unset = UNSET
    is_followed: bool | Unset = UNSET
    is_respected: bool | Unset = UNSET
    is_vip: bool | Unset = UNSET
    linkedin: None | str | Unset = UNSET
    name: str | Unset = UNSET
    next_rank: None | str | Unset = UNSET
    next_rank_points: float | None | Unset = UNSET
    points: int | Unset = UNSET
    public: bool | Unset = UNSET
    rank: str | Unset = UNSET
    rank_id: int | Unset = UNSET
    rank_ownership: float | Unset = UNSET
    rank_requirement: int | None | Unset = UNSET
    ranking: int | Unset = UNSET
    respects: int | Unset = UNSET
    sso_id: bool | Unset = UNSET
    system_bloods: int | Unset = UNSET
    system_owns: int | Unset = UNSET
    team: UserProfileTeam | Unset = UNSET
    timezone: str | Unset = UNSET
    twitter: None | str | Unset = UNSET
    university: None | Unset | UserProfileUniversityTeamType0 = UNSET
    university_name: None | str | Unset = UNSET
    user_bloods: int | Unset = UNSET
    user_owns: int | Unset = UNSET
    followed_by_count: int | Unset = UNSET
    user_respects: int | Unset = UNSET
    joined_date: datetime.datetime | Unset = UNSET
    user_follows: int | Unset = UNSET
    challenge_bloods: int | Unset = UNSET
    full_name: str | Unset = UNSET
    cv: None | str | Unset = UNSET
    cpe_id: int | None | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    server: None | str | Unset = UNSET
    account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_profile_university_team_type_0 import (
            UserProfileUniversityTeamType0,
        )

        avatar = self.avatar

        country_code = self.country_code

        country_name = self.country_name

        current_rank_progress: float | None | Unset
        if isinstance(self.current_rank_progress, Unset):
            current_rank_progress = UNSET
        else:
            current_rank_progress = self.current_rank_progress

        github: None | str | Unset
        if isinstance(self.github, Unset):
            github = UNSET
        else:
            github = self.github

        id = self.id

        is_dedicated_vip = self.is_dedicated_vip

        is_followed = self.is_followed

        is_respected = self.is_respected

        is_vip = self.is_vip

        linkedin: None | str | Unset
        if isinstance(self.linkedin, Unset):
            linkedin = UNSET
        else:
            linkedin = self.linkedin

        name = self.name

        next_rank: None | str | Unset
        if isinstance(self.next_rank, Unset):
            next_rank = UNSET
        else:
            next_rank = self.next_rank

        next_rank_points: float | None | Unset
        if isinstance(self.next_rank_points, Unset):
            next_rank_points = UNSET
        else:
            next_rank_points = self.next_rank_points

        points = self.points

        public = self.public

        rank = self.rank

        rank_id = self.rank_id

        rank_ownership = self.rank_ownership

        rank_requirement: int | None | Unset
        if isinstance(self.rank_requirement, Unset):
            rank_requirement = UNSET
        else:
            rank_requirement = self.rank_requirement

        ranking = self.ranking

        respects = self.respects

        sso_id = self.sso_id

        system_bloods = self.system_bloods

        system_owns = self.system_owns

        team: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        timezone = self.timezone

        twitter: None | str | Unset
        if isinstance(self.twitter, Unset):
            twitter = UNSET
        else:
            twitter = self.twitter

        university: dict[str, Any] | None | Unset
        if isinstance(self.university, Unset):
            university = UNSET
        elif isinstance(self.university, UserProfileUniversityTeamType0):
            university = self.university.to_dict()
        else:
            university = self.university

        university_name: None | str | Unset
        if isinstance(self.university_name, Unset):
            university_name = UNSET
        else:
            university_name = self.university_name

        user_bloods = self.user_bloods

        user_owns = self.user_owns

        followed_by_count = self.followed_by_count

        user_respects = self.user_respects

        joined_date: str | Unset = UNSET
        if not isinstance(self.joined_date, Unset):
            joined_date = self.joined_date.isoformat()

        user_follows = self.user_follows

        challenge_bloods = self.challenge_bloods

        full_name = self.full_name

        cv: None | str | Unset
        if isinstance(self.cv, Unset):
            cv = UNSET
        else:
            cv = self.cv

        cpe_id: int | None | Unset
        if isinstance(self.cpe_id, Unset):
            cpe_id = UNSET
        else:
            cpe_id = self.cpe_id

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        server: None | str | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        else:
            server = self.server

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if current_rank_progress is not UNSET:
            field_dict["current_rank_progress"] = current_rank_progress
        if github is not UNSET:
            field_dict["github"] = github
        if id is not UNSET:
            field_dict["id"] = id
        if is_dedicated_vip is not UNSET:
            field_dict["isDedicatedVip"] = is_dedicated_vip
        if is_followed is not UNSET:
            field_dict["isFollowed"] = is_followed
        if is_respected is not UNSET:
            field_dict["isRespected"] = is_respected
        if is_vip is not UNSET:
            field_dict["isVip"] = is_vip
        if linkedin is not UNSET:
            field_dict["linkedin"] = linkedin
        if name is not UNSET:
            field_dict["name"] = name
        if next_rank is not UNSET:
            field_dict["next_rank"] = next_rank
        if next_rank_points is not UNSET:
            field_dict["next_rank_points"] = next_rank_points
        if points is not UNSET:
            field_dict["points"] = points
        if public is not UNSET:
            field_dict["public"] = public
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
        if respects is not UNSET:
            field_dict["respects"] = respects
        if sso_id is not UNSET:
            field_dict["sso_id"] = sso_id
        if system_bloods is not UNSET:
            field_dict["system_bloods"] = system_bloods
        if system_owns is not UNSET:
            field_dict["system_owns"] = system_owns
        if team is not UNSET:
            field_dict["team"] = team
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if university is not UNSET:
            field_dict["university"] = university
        if university_name is not UNSET:
            field_dict["university_name"] = university_name
        if user_bloods is not UNSET:
            field_dict["user_bloods"] = user_bloods
        if user_owns is not UNSET:
            field_dict["user_owns"] = user_owns
        if followed_by_count is not UNSET:
            field_dict["followed_by_count"] = followed_by_count
        if user_respects is not UNSET:
            field_dict["user_respects"] = user_respects
        if joined_date is not UNSET:
            field_dict["joined_date"] = joined_date
        if user_follows is not UNSET:
            field_dict["user_follows"] = user_follows
        if challenge_bloods is not UNSET:
            field_dict["challenge_bloods"] = challenge_bloods
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if cv is not UNSET:
            field_dict["cv"] = cv
        if cpe_id is not UNSET:
            field_dict["cpe_id"] = cpe_id
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if server is not UNSET:
            field_dict["server"] = server
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_profile_team import UserProfileTeam
        from ..models.user_profile_university_team_type_0 import (
            UserProfileUniversityTeamType0,
        )

        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        country_code = d.pop("country_code", UNSET)

        country_name = d.pop("country_name", UNSET)

        def _parse_current_rank_progress(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_rank_progress = _parse_current_rank_progress(
            d.pop("current_rank_progress", UNSET)
        )

        def _parse_github(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        github = _parse_github(d.pop("github", UNSET))

        id = d.pop("id", UNSET)

        is_dedicated_vip = d.pop("isDedicatedVip", UNSET)

        is_followed = d.pop("isFollowed", UNSET)

        is_respected = d.pop("isRespected", UNSET)

        is_vip = d.pop("isVip", UNSET)

        def _parse_linkedin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin = _parse_linkedin(d.pop("linkedin", UNSET))

        name = d.pop("name", UNSET)

        def _parse_next_rank(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_rank = _parse_next_rank(d.pop("next_rank", UNSET))

        def _parse_next_rank_points(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        next_rank_points = _parse_next_rank_points(d.pop("next_rank_points", UNSET))

        points = d.pop("points", UNSET)

        public = d.pop("public", UNSET)

        rank = d.pop("rank", UNSET)

        rank_id = d.pop("rank_id", UNSET)

        rank_ownership = d.pop("rank_ownership", UNSET)

        def _parse_rank_requirement(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rank_requirement = _parse_rank_requirement(d.pop("rank_requirement", UNSET))

        ranking = d.pop("ranking", UNSET)

        respects = d.pop("respects", UNSET)

        sso_id = d.pop("sso_id", UNSET)

        system_bloods = d.pop("system_bloods", UNSET)

        system_owns = d.pop("system_owns", UNSET)

        _team = d.pop("team", UNSET)
        team: UserProfileTeam | Unset
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = UserProfileTeam.from_dict(_team)

        timezone = d.pop("timezone", UNSET)

        def _parse_twitter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter = _parse_twitter(d.pop("twitter", UNSET))

        def _parse_university(
            data: object,
        ) -> None | Unset | UserProfileUniversityTeamType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_profile_university_team_type_0 = (
                    UserProfileUniversityTeamType0.from_dict(data)
                )

                return componentsschemas_user_profile_university_team_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserProfileUniversityTeamType0, data)

        university = _parse_university(d.pop("university", UNSET))

        def _parse_university_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        university_name = _parse_university_name(d.pop("university_name", UNSET))

        user_bloods = d.pop("user_bloods", UNSET)

        user_owns = d.pop("user_owns", UNSET)

        followed_by_count = d.pop("followed_by_count", UNSET)

        user_respects = d.pop("user_respects", UNSET)

        _joined_date = d.pop("joined_date", UNSET)
        joined_date: datetime.datetime | Unset
        if isinstance(_joined_date, Unset):
            joined_date = UNSET
        else:
            joined_date = datetime.datetime.fromisoformat(_joined_date)

        user_follows = d.pop("user_follows", UNSET)

        challenge_bloods = d.pop("challenge_bloods", UNSET)

        full_name = d.pop("full_name", UNSET)

        def _parse_cv(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cv = _parse_cv(d.pop("cv", UNSET))

        def _parse_cpe_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpe_id = _parse_cpe_id(d.pop("cpe_id", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phone_number", UNSET))

        def _parse_server(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server = _parse_server(d.pop("server", UNSET))

        account_id = d.pop("account_id", UNSET)

        user_profile = cls(
            avatar=avatar,
            country_code=country_code,
            country_name=country_name,
            current_rank_progress=current_rank_progress,
            github=github,
            id=id,
            is_dedicated_vip=is_dedicated_vip,
            is_followed=is_followed,
            is_respected=is_respected,
            is_vip=is_vip,
            linkedin=linkedin,
            name=name,
            next_rank=next_rank,
            next_rank_points=next_rank_points,
            points=points,
            public=public,
            rank=rank,
            rank_id=rank_id,
            rank_ownership=rank_ownership,
            rank_requirement=rank_requirement,
            ranking=ranking,
            respects=respects,
            sso_id=sso_id,
            system_bloods=system_bloods,
            system_owns=system_owns,
            team=team,
            timezone=timezone,
            twitter=twitter,
            university=university,
            university_name=university_name,
            user_bloods=user_bloods,
            user_owns=user_owns,
            followed_by_count=followed_by_count,
            user_respects=user_respects,
            joined_date=joined_date,
            user_follows=user_follows,
            challenge_bloods=challenge_bloods,
            full_name=full_name,
            cv=cv,
            cpe_id=cpe_id,
            phone_number=phone_number,
            server=server,
            account_id=account_id,
        )

        user_profile.additional_properties = d
        return user_profile

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

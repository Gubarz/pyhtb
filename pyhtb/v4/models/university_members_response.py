from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_member_team import TeamMemberTeam


T = TypeVar("T", bound="UniversityMembersResponse")


@_attrs_define
class UniversityMembersResponse:
    """University Members Resposne

    Attributes:
        avatar (None | str | Unset):
        country_code (None | str | Unset):
        country_name (str | Unset):
        id (int | Unset):
        name (str | Unset):
        points (int | Unset):
        public (int | Unset):
        rank (int | str | Unset):
        rank_text (str | Unset):
        role (str | Unset):
        root_bloods_count (int | Unset):
        root_owns (int | Unset):
        university (TeamMemberTeam | Unset):
        user_bloods_count (int | Unset):
        user_owns (int | Unset):
    """

    avatar: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    country_name: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    points: int | Unset = UNSET
    public: int | Unset = UNSET
    rank: int | str | Unset = UNSET
    rank_text: str | Unset = UNSET
    role: str | Unset = UNSET
    root_bloods_count: int | Unset = UNSET
    root_owns: int | Unset = UNSET
    university: TeamMemberTeam | Unset = UNSET
    user_bloods_count: int | Unset = UNSET
    user_owns: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        country_name = self.country_name

        id = self.id

        name = self.name

        points = self.points

        public = self.public

        rank: int | str | Unset
        if isinstance(self.rank, Unset):
            rank = UNSET
        else:
            rank = self.rank

        rank_text = self.rank_text

        role = self.role

        root_bloods_count = self.root_bloods_count

        root_owns = self.root_owns

        university: dict[str, Any] | Unset = UNSET
        if not isinstance(self.university, Unset):
            university = self.university.to_dict()

        user_bloods_count = self.user_bloods_count

        user_owns = self.user_owns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if points is not UNSET:
            field_dict["points"] = points
        if public is not UNSET:
            field_dict["public"] = public
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_text is not UNSET:
            field_dict["rank_text"] = rank_text
        if role is not UNSET:
            field_dict["role"] = role
        if root_bloods_count is not UNSET:
            field_dict["root_bloods_count"] = root_bloods_count
        if root_owns is not UNSET:
            field_dict["root_owns"] = root_owns
        if university is not UNSET:
            field_dict["university"] = university
        if user_bloods_count is not UNSET:
            field_dict["user_bloods_count"] = user_bloods_count
        if user_owns is not UNSET:
            field_dict["user_owns"] = user_owns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_member_team import TeamMemberTeam

        d = dict(src_dict)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        country_name = d.pop("country_name", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        points = d.pop("points", UNSET)

        public = d.pop("public", UNSET)

        def _parse_rank(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        rank = _parse_rank(d.pop("rank", UNSET))

        rank_text = d.pop("rank_text", UNSET)

        role = d.pop("role", UNSET)

        root_bloods_count = d.pop("root_bloods_count", UNSET)

        root_owns = d.pop("root_owns", UNSET)

        _university = d.pop("university", UNSET)
        university: TeamMemberTeam | Unset
        if isinstance(_university, Unset):
            university = UNSET
        else:
            university = TeamMemberTeam.from_dict(_university)

        user_bloods_count = d.pop("user_bloods_count", UNSET)

        user_owns = d.pop("user_owns", UNSET)

        university_members_response = cls(
            avatar=avatar,
            country_code=country_code,
            country_name=country_name,
            id=id,
            name=name,
            points=points,
            public=public,
            rank=rank,
            rank_text=rank_text,
            role=role,
            root_bloods_count=root_bloods_count,
            root_owns=root_owns,
            university=university,
            user_bloods_count=user_bloods_count,
            user_owns=user_owns,
        )

        university_members_response.additional_properties = d
        return university_members_response

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

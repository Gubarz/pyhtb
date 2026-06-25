from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Prolab")


@_attrs_define
class Prolab:
    """Schema definition for Prolab

    Attributes:
        cover_img_url (None | str | Unset):
        designated_category (str | Unset):  Example: Red team_ Operator.
        id (int | Unset):  Example: 1.
        identifier (str | Unset):
        lab_servers_count (int | Unset):  Example: 6.
        level (int | Unset):  Example: 1.
        mini (bool | Unset):
        name (str | Unset):  Example: RastaLabs.
        new (bool | Unset):
        ownership (float | Unset):
        pro_flags_count (int | Unset):  Example: 22.
        pro_machines_count (int | Unset):  Example: 15.
        release_at (datetime.datetime | Unset):  Example: 2018-01-02T06:00:00.000000Z.
        skill_level (str | Unset):  Example: INTERMEDIATE.
        state (str | Unset):
        team (str | Unset):  Example: red.
        user_eligible_for_certificate (bool | Unset):
        content_id (str | Unset):
        rating (float | Unset):
        rating_count (int | Unset):
        pro_flags_owns_count (int | Unset):
        avatar_48_circle_url (str | Unset):
        avatar_48_url (str | Unset):
        avatar_url (str | Unset):
    """

    cover_img_url: None | str | Unset = UNSET
    designated_category: str | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    lab_servers_count: int | Unset = UNSET
    level: int | Unset = UNSET
    mini: bool | Unset = UNSET
    name: str | Unset = UNSET
    new: bool | Unset = UNSET
    ownership: float | Unset = UNSET
    pro_flags_count: int | Unset = UNSET
    pro_machines_count: int | Unset = UNSET
    release_at: datetime.datetime | Unset = UNSET
    skill_level: str | Unset = UNSET
    state: str | Unset = UNSET
    team: str | Unset = UNSET
    user_eligible_for_certificate: bool | Unset = UNSET
    content_id: str | Unset = UNSET
    rating: float | Unset = UNSET
    rating_count: int | Unset = UNSET
    pro_flags_owns_count: int | Unset = UNSET
    avatar_48_circle_url: str | Unset = UNSET
    avatar_48_url: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cover_img_url: None | str | Unset
        if isinstance(self.cover_img_url, Unset):
            cover_img_url = UNSET
        else:
            cover_img_url = self.cover_img_url

        designated_category = self.designated_category

        id = self.id

        identifier = self.identifier

        lab_servers_count = self.lab_servers_count

        level = self.level

        mini = self.mini

        name = self.name

        new = self.new

        ownership = self.ownership

        pro_flags_count = self.pro_flags_count

        pro_machines_count = self.pro_machines_count

        release_at: str | Unset = UNSET
        if not isinstance(self.release_at, Unset):
            release_at = self.release_at.isoformat()

        skill_level = self.skill_level

        state = self.state

        team = self.team

        user_eligible_for_certificate = self.user_eligible_for_certificate

        content_id = self.content_id

        rating = self.rating

        rating_count = self.rating_count

        pro_flags_owns_count = self.pro_flags_owns_count

        avatar_48_circle_url = self.avatar_48_circle_url

        avatar_48_url = self.avatar_48_url

        avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cover_img_url is not UNSET:
            field_dict["cover_img_url"] = cover_img_url
        if designated_category is not UNSET:
            field_dict["designated_category"] = designated_category
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if lab_servers_count is not UNSET:
            field_dict["lab_servers_count"] = lab_servers_count
        if level is not UNSET:
            field_dict["level"] = level
        if mini is not UNSET:
            field_dict["mini"] = mini
        if name is not UNSET:
            field_dict["name"] = name
        if new is not UNSET:
            field_dict["new"] = new
        if ownership is not UNSET:
            field_dict["ownership"] = ownership
        if pro_flags_count is not UNSET:
            field_dict["pro_flags_count"] = pro_flags_count
        if pro_machines_count is not UNSET:
            field_dict["pro_machines_count"] = pro_machines_count
        if release_at is not UNSET:
            field_dict["release_at"] = release_at
        if skill_level is not UNSET:
            field_dict["skill_level"] = skill_level
        if state is not UNSET:
            field_dict["state"] = state
        if team is not UNSET:
            field_dict["team"] = team
        if user_eligible_for_certificate is not UNSET:
            field_dict["user_eligible_for_certificate"] = user_eligible_for_certificate
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_count is not UNSET:
            field_dict["rating_count"] = rating_count
        if pro_flags_owns_count is not UNSET:
            field_dict["pro_flags_owns_count"] = pro_flags_owns_count
        if avatar_48_circle_url is not UNSET:
            field_dict["avatar_48_circle_url"] = avatar_48_circle_url
        if avatar_48_url is not UNSET:
            field_dict["avatar_48_url"] = avatar_48_url
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cover_img_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_img_url = _parse_cover_img_url(d.pop("cover_img_url", UNSET))

        designated_category = d.pop("designated_category", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        lab_servers_count = d.pop("lab_servers_count", UNSET)

        level = d.pop("level", UNSET)

        mini = d.pop("mini", UNSET)

        name = d.pop("name", UNSET)

        new = d.pop("new", UNSET)

        ownership = d.pop("ownership", UNSET)

        pro_flags_count = d.pop("pro_flags_count", UNSET)

        pro_machines_count = d.pop("pro_machines_count", UNSET)

        _release_at = d.pop("release_at", UNSET)
        release_at: datetime.datetime | Unset
        if isinstance(_release_at, Unset):
            release_at = UNSET
        else:
            release_at = datetime.datetime.fromisoformat(_release_at)

        skill_level = d.pop("skill_level", UNSET)

        state = d.pop("state", UNSET)

        team = d.pop("team", UNSET)

        user_eligible_for_certificate = d.pop("user_eligible_for_certificate", UNSET)

        content_id = d.pop("content_id", UNSET)

        rating = d.pop("rating", UNSET)

        rating_count = d.pop("rating_count", UNSET)

        pro_flags_owns_count = d.pop("pro_flags_owns_count", UNSET)

        avatar_48_circle_url = d.pop("avatar_48_circle_url", UNSET)

        avatar_48_url = d.pop("avatar_48_url", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        prolab = cls(
            cover_img_url=cover_img_url,
            designated_category=designated_category,
            id=id,
            identifier=identifier,
            lab_servers_count=lab_servers_count,
            level=level,
            mini=mini,
            name=name,
            new=new,
            ownership=ownership,
            pro_flags_count=pro_flags_count,
            pro_machines_count=pro_machines_count,
            release_at=release_at,
            skill_level=skill_level,
            state=state,
            team=team,
            user_eligible_for_certificate=user_eligible_for_certificate,
            content_id=content_id,
            rating=rating,
            rating_count=rating_count,
            pro_flags_owns_count=pro_flags_owns_count,
            avatar_48_circle_url=avatar_48_circle_url,
            avatar_48_url=avatar_48_url,
            avatar_url=avatar_url,
        )

        prolab.additional_properties = d
        return prolab

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

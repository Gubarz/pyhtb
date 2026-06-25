from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendedCard")


@_attrs_define
class RecommendedCard:
    """Schema definition for Recommended Card

    Attributes:
        category_name (str | Unset):  Example: AI - ML.
        difficulty (str | Unset):  Example: Medium.
        id (int | Unset):  Example: 753.
        name (str | Unset):  Example: Prometheon.
        rating (float | Unset):
        release_date (str | Unset):  Example: 2024-08-09T20:00:00.000000Z.
        retire_challenge_id (int | Unset):  Example: 445.
        retired (bool | Unset):
        state (str | Unset):  Example: unreleased.
        url_name (str | Unset):  Example: prometheon.
        avatar_url (str | Unset):
    """

    category_name: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    rating: float | Unset = UNSET
    release_date: str | Unset = UNSET
    retire_challenge_id: int | Unset = UNSET
    retired: bool | Unset = UNSET
    state: str | Unset = UNSET
    url_name: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_name = self.category_name

        difficulty = self.difficulty

        id = self.id

        name = self.name

        rating = self.rating

        release_date = self.release_date

        retire_challenge_id = self.retire_challenge_id

        retired = self.retired

        state = self.state

        url_name = self.url_name

        avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rating is not UNSET:
            field_dict["rating"] = rating
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if retire_challenge_id is not UNSET:
            field_dict["retire_challenge_id"] = retire_challenge_id
        if retired is not UNSET:
            field_dict["retired"] = retired
        if state is not UNSET:
            field_dict["state"] = state
        if url_name is not UNSET:
            field_dict["url_name"] = url_name
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_name = d.pop("category_name", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rating = d.pop("rating", UNSET)

        release_date = d.pop("release_date", UNSET)

        retire_challenge_id = d.pop("retire_challenge_id", UNSET)

        retired = d.pop("retired", UNSET)

        state = d.pop("state", UNSET)

        url_name = d.pop("url_name", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        recommended_card = cls(
            category_name=category_name,
            difficulty=difficulty,
            id=id,
            name=name,
            rating=rating,
            release_date=release_date,
            retire_challenge_id=retire_challenge_id,
            retired=retired,
            state=state,
            url_name=url_name,
            avatar_url=avatar_url,
        )

        recommended_card.additional_properties = d
        return recommended_card

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

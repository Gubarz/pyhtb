from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.challenge_retires_type_0 import ChallengeRetiresType0
    from ..models.difficulty_chart_type_1 import DifficultyChartType1
    from ..models.label import Label


T = TypeVar("T", bound="ChallengeList")


@_attrs_define
class ChallengeList:
    """Schema definition for Challenge List

    Attributes:
        auth_user_has_reviewed (bool | Unset):
        avatar (None | str | Unset):
        category_id (int | Unset):  Example: 4.
        category_name (str | Unset):  Example: Pwn.
        difficulty (str | Unset):  Example: Very Easy.
        difficulty_chart (DifficultyChartType1 | list[Any] | Unset):
        id (int | Unset):  Example: 706.
        is_owned (bool | Unset):
        name (str | Unset):  Example: Regularity.
        pinned (bool | Unset):
        play_methods (list[None | str] | None | Unset):
        rating (float | None | Unset):  Example: 4.
        rating_count (int | Unset):  Example: 1.
        release_date (datetime.datetime | Unset):  Example: 2024-06-07T20:00:00.000000Z.
        retires (ChallengeRetiresType0 | None | Unset):
        solves (int | Unset):  Example: 132.
        state (str | Unset):  Example: retired.
        user_difficulty (str | Unset):  Example: 3.33.
        labels (list[Label] | Unset):
    """

    auth_user_has_reviewed: bool | Unset = UNSET
    avatar: None | str | Unset = UNSET
    category_id: int | Unset = UNSET
    category_name: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    difficulty_chart: DifficultyChartType1 | list[Any] | Unset = UNSET
    id: int | Unset = UNSET
    is_owned: bool | Unset = UNSET
    name: str | Unset = UNSET
    pinned: bool | Unset = UNSET
    play_methods: list[None | str] | None | Unset = UNSET
    rating: float | None | Unset = UNSET
    rating_count: int | Unset = UNSET
    release_date: datetime.datetime | Unset = UNSET
    retires: ChallengeRetiresType0 | None | Unset = UNSET
    solves: int | Unset = UNSET
    state: str | Unset = UNSET
    user_difficulty: str | Unset = UNSET
    labels: list[Label] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.challenge_retires_type_0 import ChallengeRetiresType0

        auth_user_has_reviewed = self.auth_user_has_reviewed

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        category_id = self.category_id

        category_name = self.category_name

        difficulty = self.difficulty

        difficulty_chart: dict[str, Any] | list[Any] | Unset
        if isinstance(self.difficulty_chart, Unset):
            difficulty_chart = UNSET
        elif isinstance(self.difficulty_chart, list):
            difficulty_chart = self.difficulty_chart

        else:
            difficulty_chart = self.difficulty_chart.to_dict()

        id = self.id

        is_owned = self.is_owned

        name = self.name

        pinned = self.pinned

        play_methods: list[None | str] | None | Unset
        if isinstance(self.play_methods, Unset):
            play_methods = UNSET
        elif isinstance(self.play_methods, list):
            play_methods = []
            for componentsschemas_string_array_type_0_item_data in self.play_methods:
                componentsschemas_string_array_type_0_item: None | str
                componentsschemas_string_array_type_0_item = (
                    componentsschemas_string_array_type_0_item_data
                )
                play_methods.append(componentsschemas_string_array_type_0_item)

        else:
            play_methods = self.play_methods

        rating: float | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        rating_count = self.rating_count

        release_date: str | Unset = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        retires: dict[str, Any] | None | Unset
        if isinstance(self.retires, Unset):
            retires = UNSET
        elif isinstance(self.retires, ChallengeRetiresType0):
            retires = self.retires.to_dict()
        else:
            retires = self.retires

        solves = self.solves

        state = self.state

        user_difficulty = self.user_difficulty

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for componentsschemas_label_items_item_data in self.labels:
                componentsschemas_label_items_item = (
                    componentsschemas_label_items_item_data.to_dict()
                )
                labels.append(componentsschemas_label_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_user_has_reviewed is not UNSET:
            field_dict["auth_user_has_reviewed"] = auth_user_has_reviewed
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if difficulty_chart is not UNSET:
            field_dict["difficulty_chart"] = difficulty_chart
        if id is not UNSET:
            field_dict["id"] = id
        if is_owned is not UNSET:
            field_dict["is_owned"] = is_owned
        if name is not UNSET:
            field_dict["name"] = name
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if play_methods is not UNSET:
            field_dict["play_methods"] = play_methods
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_count is not UNSET:
            field_dict["rating_count"] = rating_count
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if retires is not UNSET:
            field_dict["retires"] = retires
        if solves is not UNSET:
            field_dict["solves"] = solves
        if state is not UNSET:
            field_dict["state"] = state
        if user_difficulty is not UNSET:
            field_dict["user_difficulty"] = user_difficulty
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge_retires_type_0 import ChallengeRetiresType0
        from ..models.difficulty_chart_type_1 import DifficultyChartType1
        from ..models.label import Label

        d = dict(src_dict)
        auth_user_has_reviewed = d.pop("auth_user_has_reviewed", UNSET)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        category_id = d.pop("category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        def _parse_difficulty_chart(
            data: object,
        ) -> DifficultyChartType1 | list[Any] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_difficulty_chart_type_0 = cast(list[Any], data)

                return componentsschemas_difficulty_chart_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_difficulty_chart_type_1 = DifficultyChartType1.from_dict(
                data
            )

            return componentsschemas_difficulty_chart_type_1

        difficulty_chart = _parse_difficulty_chart(d.pop("difficulty_chart", UNSET))

        id = d.pop("id", UNSET)

        is_owned = d.pop("is_owned", UNSET)

        name = d.pop("name", UNSET)

        pinned = d.pop("pinned", UNSET)

        def _parse_play_methods(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_string_array_type_0 = []
                _componentsschemas_string_array_type_0 = data
                for (
                    componentsschemas_string_array_type_0_item_data
                ) in _componentsschemas_string_array_type_0:

                    def _parse_componentsschemas_string_array_type_0_item(
                        data: object,
                    ) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    componentsschemas_string_array_type_0_item = (
                        _parse_componentsschemas_string_array_type_0_item(
                            componentsschemas_string_array_type_0_item_data
                        )
                    )

                    componentsschemas_string_array_type_0.append(
                        componentsschemas_string_array_type_0_item
                    )

                return componentsschemas_string_array_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        play_methods = _parse_play_methods(d.pop("play_methods", UNSET))

        def _parse_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))

        rating_count = d.pop("rating_count", UNSET)

        _release_date = d.pop("release_date", UNSET)
        release_date: datetime.datetime | Unset
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = datetime.datetime.fromisoformat(_release_date)

        def _parse_retires(data: object) -> ChallengeRetiresType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_challenge_retires_type_0 = (
                    ChallengeRetiresType0.from_dict(data)
                )

                return componentsschemas_challenge_retires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChallengeRetiresType0 | None | Unset, data)

        retires = _parse_retires(d.pop("retires", UNSET))

        solves = d.pop("solves", UNSET)

        state = d.pop("state", UNSET)

        user_difficulty = d.pop("user_difficulty", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[Label] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for componentsschemas_label_items_item_data in _labels:
                componentsschemas_label_items_item = Label.from_dict(
                    componentsschemas_label_items_item_data
                )

                labels.append(componentsschemas_label_items_item)

        challenge_list = cls(
            auth_user_has_reviewed=auth_user_has_reviewed,
            avatar=avatar,
            category_id=category_id,
            category_name=category_name,
            difficulty=difficulty,
            difficulty_chart=difficulty_chart,
            id=id,
            is_owned=is_owned,
            name=name,
            pinned=pinned,
            play_methods=play_methods,
            rating=rating,
            rating_count=rating_count,
            release_date=release_date,
            retires=retires,
            solves=solves,
            state=state,
            user_difficulty=user_difficulty,
            labels=labels,
        )

        challenge_list.additional_properties = d
        return challenge_list

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

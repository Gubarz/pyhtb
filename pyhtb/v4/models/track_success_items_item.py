from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.difficulty_chart_type_1 import DifficultyChartType1


T = TypeVar("T", bound="TrackSuccessItemsItem")


@_attrs_define
class TrackSuccessItemsItem:
    """
    Attributes:
        avatar (None | str | Unset):
        category (None | str | Unset):
        complete (bool | Unset):
        difficulty (str | Unset):
        difficulty_ratings (DifficultyChartType1 | list[Any] | Unset):
        id (int | Unset):
        name (str | Unset):
        os (None | str | Unset):
        type_ (str | Unset):
    """

    avatar: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    complete: bool | Unset = UNSET
    difficulty: str | Unset = UNSET
    difficulty_ratings: DifficultyChartType1 | list[Any] | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    os: None | str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        complete = self.complete

        difficulty = self.difficulty

        difficulty_ratings: dict[str, Any] | list[Any] | Unset
        if isinstance(self.difficulty_ratings, Unset):
            difficulty_ratings = UNSET
        elif isinstance(self.difficulty_ratings, list):
            difficulty_ratings = self.difficulty_ratings

        else:
            difficulty_ratings = self.difficulty_ratings.to_dict()

        id = self.id

        name = self.name

        os: None | str | Unset
        if isinstance(self.os, Unset):
            os = UNSET
        else:
            os = self.os

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if category is not UNSET:
            field_dict["category"] = category
        if complete is not UNSET:
            field_dict["complete"] = complete
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if difficulty_ratings is not UNSET:
            field_dict["difficulty_ratings"] = difficulty_ratings
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.difficulty_chart_type_1 import DifficultyChartType1

        d = dict(src_dict)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        complete = d.pop("complete", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        def _parse_difficulty_ratings(
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

        difficulty_ratings = _parse_difficulty_ratings(
            d.pop("difficulty_ratings", UNSET)
        )

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_os(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        os = _parse_os(d.pop("os", UNSET))

        type_ = d.pop("type", UNSET)

        track_success_items_item = cls(
            avatar=avatar,
            category=category,
            complete=complete,
            difficulty=difficulty,
            difficulty_ratings=difficulty_ratings,
            id=id,
            name=name,
            os=os,
            type_=type_,
        )

        track_success_items_item.additional_properties = d
        return track_success_items_item

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

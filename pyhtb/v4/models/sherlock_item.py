from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label import Label
    from ..models.sherlock_retires_type_0 import SherlockRetiresType0


T = TypeVar("T", bound="SherlockItem")


@_attrs_define
class SherlockItem:
    """Schema definition for Sherlock Item

    Attributes:
        auth_user_has_reviewed (bool | Unset):
        avatar (str | Unset):
        category_id (int | Unset):
        category_name (str | Unset):
        difficulty (str | Unset):
        id (int | Unset):
        is_owned (bool | Unset):
        name (str | Unset):
        pinned (bool | Unset):
        play_methods (list[None | str] | None | Unset):
        progress (int | Unset):
        rating (float | None | Unset):
        rating_count (int | Unset):
        release_date (datetime.datetime | Unset):
        retires (None | SherlockRetiresType0 | Unset):
        solves (int | Unset):
        state (str | Unset): The state of the item.
        labels (list[Label] | Unset):
    """

    auth_user_has_reviewed: bool | Unset = UNSET
    avatar: str | Unset = UNSET
    category_id: int | Unset = UNSET
    category_name: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    id: int | Unset = UNSET
    is_owned: bool | Unset = UNSET
    name: str | Unset = UNSET
    pinned: bool | Unset = UNSET
    play_methods: list[None | str] | None | Unset = UNSET
    progress: int | Unset = UNSET
    rating: float | None | Unset = UNSET
    rating_count: int | Unset = UNSET
    release_date: datetime.datetime | Unset = UNSET
    retires: None | SherlockRetiresType0 | Unset = UNSET
    solves: int | Unset = UNSET
    state: str | Unset = UNSET
    labels: list[Label] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sherlock_retires_type_0 import SherlockRetiresType0

        auth_user_has_reviewed = self.auth_user_has_reviewed

        avatar = self.avatar

        category_id = self.category_id

        category_name = self.category_name

        difficulty = self.difficulty

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

        progress = self.progress

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
        elif isinstance(self.retires, SherlockRetiresType0):
            retires = self.retires.to_dict()
        else:
            retires = self.retires

        solves = self.solves

        state = self.state

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
        if progress is not UNSET:
            field_dict["progress"] = progress
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
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label import Label
        from ..models.sherlock_retires_type_0 import SherlockRetiresType0

        d = dict(src_dict)
        auth_user_has_reviewed = d.pop("auth_user_has_reviewed", UNSET)

        avatar = d.pop("avatar", UNSET)

        category_id = d.pop("category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        difficulty = d.pop("difficulty", UNSET)

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

        progress = d.pop("progress", UNSET)

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

        def _parse_retires(data: object) -> None | SherlockRetiresType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sherlock_retires_type_0 = (
                    SherlockRetiresType0.from_dict(data)
                )

                return componentsschemas_sherlock_retires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SherlockRetiresType0 | Unset, data)

        retires = _parse_retires(d.pop("retires", UNSET))

        solves = d.pop("solves", UNSET)

        state = d.pop("state", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[Label] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for componentsschemas_label_items_item_data in _labels:
                componentsschemas_label_items_item = Label.from_dict(
                    componentsschemas_label_items_item_data
                )

                labels.append(componentsschemas_label_items_item)

        sherlock_item = cls(
            auth_user_has_reviewed=auth_user_has_reviewed,
            avatar=avatar,
            category_id=category_id,
            category_name=category_name,
            difficulty=difficulty,
            id=id,
            is_owned=is_owned,
            name=name,
            pinned=pinned,
            play_methods=play_methods,
            progress=progress,
            rating=rating,
            rating_count=rating_count,
            release_date=release_date,
            retires=retires,
            solves=solves,
            state=state,
            labels=labels,
        )

        sherlock_item.additional_properties = d
        return sherlock_item

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

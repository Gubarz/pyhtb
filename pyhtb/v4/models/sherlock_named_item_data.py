from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag import Tag


T = TypeVar("T", bound="SherlockNamedItemData")


@_attrs_define
class SherlockNamedItemData:
    """
    Attributes:
        auth_user_has_reviewed (bool | Unset):
        avatar (str | Unset):  Example: /storage/challenges/cbcb58ac2e496207586df2854b17995f.png.
        avatar_url (str | Unset):  Example:
            https://cdn.services-k8s.prod.aws.htb.systems/content/sherlocks/avatar/9ea47ecf-b5aa-4a60-aa89-b1915754afdd.png.
        category_id (int | Unset):  Example: 16.
        category_name (str | Unset):  Example: Malware Analysis.
        difficulty (str | Unset):  Example: Insane.
        favorite (bool | Unset):
        id (int | Unset):  Example: 565.
        is_todo (bool | Unset):
        name (str | Unset):  Example: Safecracker.
        play_methods (list[None | str] | None | Unset):
        rating (float | Unset):  Example: 4.555555555555555.
        rating_count (int | Unset):  Example: 18.
        release_at (datetime.datetime | Unset):
        retired (bool | Unset):
        show_go_vip (bool | Unset):
        state (str | Unset):  Example: retired_free.
        tags (list[Tag] | Unset):
        writeup_visible (bool | Unset):
        user_can_review (bool | Unset):
    """

    auth_user_has_reviewed: bool | Unset = UNSET
    avatar: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    category_id: int | Unset = UNSET
    category_name: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    favorite: bool | Unset = UNSET
    id: int | Unset = UNSET
    is_todo: bool | Unset = UNSET
    name: str | Unset = UNSET
    play_methods: list[None | str] | None | Unset = UNSET
    rating: float | Unset = UNSET
    rating_count: int | Unset = UNSET
    release_at: datetime.datetime | Unset = UNSET
    retired: bool | Unset = UNSET
    show_go_vip: bool | Unset = UNSET
    state: str | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    writeup_visible: bool | Unset = UNSET
    user_can_review: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_user_has_reviewed = self.auth_user_has_reviewed

        avatar = self.avatar

        avatar_url = self.avatar_url

        category_id = self.category_id

        category_name = self.category_name

        difficulty = self.difficulty

        favorite = self.favorite

        id = self.id

        is_todo = self.is_todo

        name = self.name

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

        rating = self.rating

        rating_count = self.rating_count

        release_at: str | Unset = UNSET
        if not isinstance(self.release_at, Unset):
            release_at = self.release_at.isoformat()

        retired = self.retired

        show_go_vip = self.show_go_vip

        state = self.state

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for componentsschemas_tag_category_tags_items_item_data in self.tags:
                componentsschemas_tag_category_tags_items_item = (
                    componentsschemas_tag_category_tags_items_item_data.to_dict()
                )
                tags.append(componentsschemas_tag_category_tags_items_item)

        writeup_visible = self.writeup_visible

        user_can_review = self.user_can_review

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_user_has_reviewed is not UNSET:
            field_dict["auth_user_has_reviewed"] = auth_user_has_reviewed
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if id is not UNSET:
            field_dict["id"] = id
        if is_todo is not UNSET:
            field_dict["isTodo"] = is_todo
        if name is not UNSET:
            field_dict["name"] = name
        if play_methods is not UNSET:
            field_dict["play_methods"] = play_methods
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_count is not UNSET:
            field_dict["rating_count"] = rating_count
        if release_at is not UNSET:
            field_dict["release_at"] = release_at
        if retired is not UNSET:
            field_dict["retired"] = retired
        if show_go_vip is not UNSET:
            field_dict["show_go_vip"] = show_go_vip
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if writeup_visible is not UNSET:
            field_dict["writeup_visible"] = writeup_visible
        if user_can_review is not UNSET:
            field_dict["user_can_review"] = user_can_review

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag import Tag

        d = dict(src_dict)
        auth_user_has_reviewed = d.pop("auth_user_has_reviewed", UNSET)

        avatar = d.pop("avatar", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        category_id = d.pop("category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        favorite = d.pop("favorite", UNSET)

        id = d.pop("id", UNSET)

        is_todo = d.pop("isTodo", UNSET)

        name = d.pop("name", UNSET)

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

        rating = d.pop("rating", UNSET)

        rating_count = d.pop("rating_count", UNSET)

        _release_at = d.pop("release_at", UNSET)
        release_at: datetime.datetime | Unset
        if isinstance(_release_at, Unset):
            release_at = UNSET
        else:
            release_at = datetime.datetime.fromisoformat(_release_at)

        retired = d.pop("retired", UNSET)

        show_go_vip = d.pop("show_go_vip", UNSET)

        state = d.pop("state", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for componentsschemas_tag_category_tags_items_item_data in _tags:
                componentsschemas_tag_category_tags_items_item = Tag.from_dict(
                    componentsschemas_tag_category_tags_items_item_data
                )

                tags.append(componentsschemas_tag_category_tags_items_item)

        writeup_visible = d.pop("writeup_visible", UNSET)

        user_can_review = d.pop("user_can_review", UNSET)

        sherlock_named_item_data = cls(
            auth_user_has_reviewed=auth_user_has_reviewed,
            avatar=avatar,
            avatar_url=avatar_url,
            category_id=category_id,
            category_name=category_name,
            difficulty=difficulty,
            favorite=favorite,
            id=id,
            is_todo=is_todo,
            name=name,
            play_methods=play_methods,
            rating=rating,
            rating_count=rating_count,
            release_at=release_at,
            retired=retired,
            show_go_vip=show_go_vip,
            state=state,
            tags=tags,
            writeup_visible=writeup_visible,
            user_can_review=user_can_review,
        )

        sherlock_named_item_data.additional_properties = d
        return sherlock_named_item_data

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

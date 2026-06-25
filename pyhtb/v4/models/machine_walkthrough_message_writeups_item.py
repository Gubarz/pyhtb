from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineWalkthroughMessageWriteupsItem")


@_attrs_define
class MachineWalkthroughMessageWriteupsItem:
    """
    Attributes:
        created_at (str | Unset):
        disliked_by_user (None | str | Unset):
        id (int | Unset):
        language_code (None | str | Unset):
        language_name (None | str | Unset):
        liked_by_user (None | str | Unset):
        rating (int | Unset):
        total_ratings (int | Unset):
        url (str | Unset):
        user_avatar (str | Unset):
        user_id (int | Unset):
        user_name (str | Unset):
    """

    created_at: str | Unset = UNSET
    disliked_by_user: None | str | Unset = UNSET
    id: int | Unset = UNSET
    language_code: None | str | Unset = UNSET
    language_name: None | str | Unset = UNSET
    liked_by_user: None | str | Unset = UNSET
    rating: int | Unset = UNSET
    total_ratings: int | Unset = UNSET
    url: str | Unset = UNSET
    user_avatar: str | Unset = UNSET
    user_id: int | Unset = UNSET
    user_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        disliked_by_user: None | str | Unset
        if isinstance(self.disliked_by_user, Unset):
            disliked_by_user = UNSET
        else:
            disliked_by_user = self.disliked_by_user

        id = self.id

        language_code: None | str | Unset
        if isinstance(self.language_code, Unset):
            language_code = UNSET
        else:
            language_code = self.language_code

        language_name: None | str | Unset
        if isinstance(self.language_name, Unset):
            language_name = UNSET
        else:
            language_name = self.language_name

        liked_by_user: None | str | Unset
        if isinstance(self.liked_by_user, Unset):
            liked_by_user = UNSET
        else:
            liked_by_user = self.liked_by_user

        rating = self.rating

        total_ratings = self.total_ratings

        url = self.url

        user_avatar = self.user_avatar

        user_id = self.user_id

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if disliked_by_user is not UNSET:
            field_dict["disliked_by_user"] = disliked_by_user
        if id is not UNSET:
            field_dict["id"] = id
        if language_code is not UNSET:
            field_dict["language_code"] = language_code
        if language_name is not UNSET:
            field_dict["language_name"] = language_name
        if liked_by_user is not UNSET:
            field_dict["liked_by_user"] = liked_by_user
        if rating is not UNSET:
            field_dict["rating"] = rating
        if total_ratings is not UNSET:
            field_dict["total_ratings"] = total_ratings
        if url is not UNSET:
            field_dict["url"] = url
        if user_avatar is not UNSET:
            field_dict["user_avatar"] = user_avatar
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        def _parse_disliked_by_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disliked_by_user = _parse_disliked_by_user(d.pop("disliked_by_user", UNSET))

        id = d.pop("id", UNSET)

        def _parse_language_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_code = _parse_language_code(d.pop("language_code", UNSET))

        def _parse_language_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_name = _parse_language_name(d.pop("language_name", UNSET))

        def _parse_liked_by_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        liked_by_user = _parse_liked_by_user(d.pop("liked_by_user", UNSET))

        rating = d.pop("rating", UNSET)

        total_ratings = d.pop("total_ratings", UNSET)

        url = d.pop("url", UNSET)

        user_avatar = d.pop("user_avatar", UNSET)

        user_id = d.pop("user_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        machine_walkthrough_message_writeups_item = cls(
            created_at=created_at,
            disliked_by_user=disliked_by_user,
            id=id,
            language_code=language_code,
            language_name=language_name,
            liked_by_user=liked_by_user,
            rating=rating,
            total_ratings=total_ratings,
            url=url,
            user_avatar=user_avatar,
            user_id=user_id,
            user_name=user_name,
        )

        machine_walkthrough_message_writeups_item.additional_properties = d
        return machine_walkthrough_message_writeups_item

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

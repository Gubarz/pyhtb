from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.track_success_items_item import TrackSuccessItemsItem
    from ..models.tracks_creator import TracksCreator


T = TypeVar("T", bound="TracksIdResponse")


@_attrs_define
class TracksIdResponse:
    """Schema definition for Tracks Id Response

    Attributes:
        completed (bool | Unset):
        completion_cta (int | None | Unset):
        completion_message (None | str | Unset):
        completion_url (None | str | Unset):
        cover_image (None | str | Unset):
        creator (TracksCreator | Unset):
        description (str | Unset):
        difficulty (str | Unset):
        enrolled (bool | Unset):
        has_completion_message (bool | Unset):
        id (int | Unset):
        items (list[TrackSuccessItemsItem] | Unset):
        liked (bool | Unset):
        likes (int | Unset):
        name (str | Unset):
        official (bool | Unset):
        staff_pick (float | Unset):
    """

    completed: bool | Unset = UNSET
    completion_cta: int | None | Unset = UNSET
    completion_message: None | str | Unset = UNSET
    completion_url: None | str | Unset = UNSET
    cover_image: None | str | Unset = UNSET
    creator: TracksCreator | Unset = UNSET
    description: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    enrolled: bool | Unset = UNSET
    has_completion_message: bool | Unset = UNSET
    id: int | Unset = UNSET
    items: list[TrackSuccessItemsItem] | Unset = UNSET
    liked: bool | Unset = UNSET
    likes: int | Unset = UNSET
    name: str | Unset = UNSET
    official: bool | Unset = UNSET
    staff_pick: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed = self.completed

        completion_cta: int | None | Unset
        if isinstance(self.completion_cta, Unset):
            completion_cta = UNSET
        else:
            completion_cta = self.completion_cta

        completion_message: None | str | Unset
        if isinstance(self.completion_message, Unset):
            completion_message = UNSET
        else:
            completion_message = self.completion_message

        completion_url: None | str | Unset
        if isinstance(self.completion_url, Unset):
            completion_url = UNSET
        else:
            completion_url = self.completion_url

        cover_image: None | str | Unset
        if isinstance(self.cover_image, Unset):
            cover_image = UNSET
        else:
            cover_image = self.cover_image

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        description = self.description

        difficulty = self.difficulty

        enrolled = self.enrolled

        has_completion_message = self.has_completion_message

        id = self.id

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for componentsschemas_track_success_items_items_item_data in self.items:
                componentsschemas_track_success_items_items_item = (
                    componentsschemas_track_success_items_items_item_data.to_dict()
                )
                items.append(componentsschemas_track_success_items_items_item)

        liked = self.liked

        likes = self.likes

        name = self.name

        official = self.official

        staff_pick = self.staff_pick

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed is not UNSET:
            field_dict["completed"] = completed
        if completion_cta is not UNSET:
            field_dict["completion_cta"] = completion_cta
        if completion_message is not UNSET:
            field_dict["completion_message"] = completion_message
        if completion_url is not UNSET:
            field_dict["completion_url"] = completion_url
        if cover_image is not UNSET:
            field_dict["cover_image"] = cover_image
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if enrolled is not UNSET:
            field_dict["enrolled"] = enrolled
        if has_completion_message is not UNSET:
            field_dict["has_completion_message"] = has_completion_message
        if id is not UNSET:
            field_dict["id"] = id
        if items is not UNSET:
            field_dict["items"] = items
        if liked is not UNSET:
            field_dict["liked"] = liked
        if likes is not UNSET:
            field_dict["likes"] = likes
        if name is not UNSET:
            field_dict["name"] = name
        if official is not UNSET:
            field_dict["official"] = official
        if staff_pick is not UNSET:
            field_dict["staff_pick"] = staff_pick

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.track_success_items_item import TrackSuccessItemsItem
        from ..models.tracks_creator import TracksCreator

        d = dict(src_dict)
        completed = d.pop("completed", UNSET)

        def _parse_completion_cta(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        completion_cta = _parse_completion_cta(d.pop("completion_cta", UNSET))

        def _parse_completion_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_message = _parse_completion_message(
            d.pop("completion_message", UNSET)
        )

        def _parse_completion_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_url = _parse_completion_url(d.pop("completion_url", UNSET))

        def _parse_cover_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_image = _parse_cover_image(d.pop("cover_image", UNSET))

        _creator = d.pop("creator", UNSET)
        creator: TracksCreator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = TracksCreator.from_dict(_creator)

        description = d.pop("description", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        enrolled = d.pop("enrolled", UNSET)

        has_completion_message = d.pop("has_completion_message", UNSET)

        id = d.pop("id", UNSET)

        _items = d.pop("items", UNSET)
        items: list[TrackSuccessItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for componentsschemas_track_success_items_items_item_data in _items:
                componentsschemas_track_success_items_items_item = (
                    TrackSuccessItemsItem.from_dict(
                        componentsschemas_track_success_items_items_item_data
                    )
                )

                items.append(componentsschemas_track_success_items_items_item)

        liked = d.pop("liked", UNSET)

        likes = d.pop("likes", UNSET)

        name = d.pop("name", UNSET)

        official = d.pop("official", UNSET)

        staff_pick = d.pop("staff_pick", UNSET)

        tracks_id_response = cls(
            completed=completed,
            completion_cta=completion_cta,
            completion_message=completion_message,
            completion_url=completion_url,
            cover_image=cover_image,
            creator=creator,
            description=description,
            difficulty=difficulty,
            enrolled=enrolled,
            has_completion_message=has_completion_message,
            id=id,
            items=items,
            liked=liked,
            likes=likes,
            name=name,
            official=official,
            staff_pick=staff_pick,
        )

        tracks_id_response.additional_properties = d
        return tracks_id_response

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

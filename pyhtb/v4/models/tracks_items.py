from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tracks_creator import TracksCreator


T = TypeVar("T", bound="TracksItems")


@_attrs_define
class TracksItems:
    """
    Attributes:
        cover_image (str):  Example: /storage/tracks/61.png.
        creator (TracksCreator):
        difficulty (str): Difficulty level (e.g., Very Easy, Easy, Medium, Hard, etc.) Example: Easy.
        id (int):  Example: 61.
        likes (int):  Example: 92.
        name (str):  Example: Detecting Active Directory Attacks.
        official (bool):  Example: True.
        staff_pick (int):
    """

    cover_image: str
    creator: TracksCreator
    difficulty: str
    id: int
    likes: int
    name: str
    official: bool
    staff_pick: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cover_image = self.cover_image

        creator = self.creator.to_dict()

        difficulty = self.difficulty

        id = self.id

        likes = self.likes

        name = self.name

        official = self.official

        staff_pick = self.staff_pick

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cover_image": cover_image,
                "creator": creator,
                "difficulty": difficulty,
                "id": id,
                "likes": likes,
                "name": name,
                "official": official,
                "staff_pick": staff_pick,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracks_creator import TracksCreator

        d = dict(src_dict)
        cover_image = d.pop("cover_image")

        creator = TracksCreator.from_dict(d.pop("creator"))

        difficulty = d.pop("difficulty")

        id = d.pop("id")

        likes = d.pop("likes")

        name = d.pop("name")

        official = d.pop("official")

        staff_pick = d.pop("staff_pick")

        tracks_items = cls(
            cover_image=cover_image,
            creator=creator,
            difficulty=difficulty,
            id=id,
            likes=likes,
            name=name,
            official=official,
            staff_pick=staff_pick,
        )

        tracks_items.additional_properties = d
        return tracks_items

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

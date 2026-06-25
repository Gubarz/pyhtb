from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.streak_data import StreakData


T = TypeVar("T", bound="AccountResponse")


@_attrs_define
class AccountResponse:
    """Schema definition for Account response

    Attributes:
        level (int):
        level_title (str):
        level_grade (str):
        rank_image (str):
        rank_image_background (str):
        outro_animation (str):
        intro_animation (str):
        total_experience_points (int):
        level_experience_points (int):
        experience_until_next_level (int):
        streak_data (StreakData):
    """

    level: int
    level_title: str
    level_grade: str
    rank_image: str
    rank_image_background: str
    outro_animation: str
    intro_animation: str
    total_experience_points: int
    level_experience_points: int
    experience_until_next_level: int
    streak_data: StreakData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level = self.level

        level_title = self.level_title

        level_grade = self.level_grade

        rank_image = self.rank_image

        rank_image_background = self.rank_image_background

        outro_animation = self.outro_animation

        intro_animation = self.intro_animation

        total_experience_points = self.total_experience_points

        level_experience_points = self.level_experience_points

        experience_until_next_level = self.experience_until_next_level

        streak_data = self.streak_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "levelTitle": level_title,
                "levelGrade": level_grade,
                "rankImage": rank_image,
                "rankImageBackground": rank_image_background,
                "outroAnimation": outro_animation,
                "introAnimation": intro_animation,
                "totalExperiencePoints": total_experience_points,
                "levelExperiencePoints": level_experience_points,
                "experienceUntilNextLevel": experience_until_next_level,
                "streakData": streak_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.streak_data import StreakData

        d = dict(src_dict)
        level = d.pop("level")

        level_title = d.pop("levelTitle")

        level_grade = d.pop("levelGrade")

        rank_image = d.pop("rankImage")

        rank_image_background = d.pop("rankImageBackground")

        outro_animation = d.pop("outroAnimation")

        intro_animation = d.pop("introAnimation")

        total_experience_points = d.pop("totalExperiencePoints")

        level_experience_points = d.pop("levelExperiencePoints")

        experience_until_next_level = d.pop("experienceUntilNextLevel")

        streak_data = StreakData.from_dict(d.pop("streakData"))

        account_response = cls(
            level=level,
            level_title=level_title,
            level_grade=level_grade,
            rank_image=rank_image,
            rank_image_background=rank_image_background,
            outro_animation=outro_animation,
            intro_animation=intro_animation,
            total_experience_points=total_experience_points,
            level_experience_points=level_experience_points,
            experience_until_next_level=experience_until_next_level,
            streak_data=streak_data,
        )

        account_response.additional_properties = d
        return account_response

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

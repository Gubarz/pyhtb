from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StreakData")


@_attrs_define
class StreakData:
    """
    Attributes:
        counter (int):
        current_experience_points (int):
        required_experience_points (int):
        remaining_experience_points (int):
        expires_at (datetime.datetime):
        is_completed (bool):
        in_danger (bool):
        max_streak (int):
        streak_savers (int):
    """

    counter: int
    current_experience_points: int
    required_experience_points: int
    remaining_experience_points: int
    expires_at: datetime.datetime
    is_completed: bool
    in_danger: bool
    max_streak: int
    streak_savers: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counter = self.counter

        current_experience_points = self.current_experience_points

        required_experience_points = self.required_experience_points

        remaining_experience_points = self.remaining_experience_points

        expires_at = self.expires_at.isoformat()

        is_completed = self.is_completed

        in_danger = self.in_danger

        max_streak = self.max_streak

        streak_savers = self.streak_savers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "counter": counter,
                "currentExperiencePoints": current_experience_points,
                "requiredExperiencePoints": required_experience_points,
                "remainingExperiencePoints": remaining_experience_points,
                "expiresAt": expires_at,
                "isCompleted": is_completed,
                "inDanger": in_danger,
                "maxStreak": max_streak,
                "streakSavers": streak_savers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        counter = d.pop("counter")

        current_experience_points = d.pop("currentExperiencePoints")

        required_experience_points = d.pop("requiredExperiencePoints")

        remaining_experience_points = d.pop("remainingExperiencePoints")

        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))

        is_completed = d.pop("isCompleted")

        in_danger = d.pop("inDanger")

        max_streak = d.pop("maxStreak")

        streak_savers = d.pop("streakSavers")

        streak_data = cls(
            counter=counter,
            current_experience_points=current_experience_points,
            required_experience_points=required_experience_points,
            remaining_experience_points=remaining_experience_points,
            expires_at=expires_at,
            is_completed=is_completed,
            in_danger=in_danger,
            max_streak=max_streak,
            streak_savers=streak_savers,
        )

        streak_data.additional_properties = d
        return streak_data

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

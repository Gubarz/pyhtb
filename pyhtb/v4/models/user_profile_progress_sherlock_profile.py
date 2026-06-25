from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.challenge_categories import ChallengeCategories
    from ..models.challenge_difficulties import ChallengeDifficulties
    from ..models.user_profile_progress_sherlock_profile_challenge_owns import (
        UserProfileProgressSherlockProfileChallengeOwns,
    )


T = TypeVar("T", bound="UserProfileProgressSherlockProfile")


@_attrs_define
class UserProfileProgressSherlockProfile:
    """
    Attributes:
        challenge_categories (list[ChallengeCategories] | Unset):
        challenge_difficulties (list[ChallengeDifficulties] | Unset):
        challenge_owns (UserProfileProgressSherlockProfileChallengeOwns | Unset):
        solved_tasks (float | Unset):
        total_bloods (int | Unset):
    """

    challenge_categories: list[ChallengeCategories] | Unset = UNSET
    challenge_difficulties: list[ChallengeDifficulties] | Unset = UNSET
    challenge_owns: UserProfileProgressSherlockProfileChallengeOwns | Unset = UNSET
    solved_tasks: float | Unset = UNSET
    total_bloods: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.challenge_categories, Unset):
            challenge_categories = []
            for componentsschemas_user_profile_progress_sherlock_profile_challenge_categories_items_item_data in self.challenge_categories:
                componentsschemas_user_profile_progress_sherlock_profile_challenge_categories_items_item = componentsschemas_user_profile_progress_sherlock_profile_challenge_categories_items_item_data.to_dict()
                challenge_categories.append(
                    componentsschemas_user_profile_progress_sherlock_profile_challenge_categories_items_item
                )

        challenge_difficulties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.challenge_difficulties, Unset):
            challenge_difficulties = []
            for componentsschemas_user_profile_progress_sherlock_profile_challenge_difficulties_items_item_data in self.challenge_difficulties:
                componentsschemas_user_profile_progress_sherlock_profile_challenge_difficulties_items_item = componentsschemas_user_profile_progress_sherlock_profile_challenge_difficulties_items_item_data.to_dict()
                challenge_difficulties.append(
                    componentsschemas_user_profile_progress_sherlock_profile_challenge_difficulties_items_item
                )

        challenge_owns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.challenge_owns, Unset):
            challenge_owns = self.challenge_owns.to_dict()

        solved_tasks = self.solved_tasks

        total_bloods = self.total_bloods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge_categories is not UNSET:
            field_dict["challenge_categories"] = challenge_categories
        if challenge_difficulties is not UNSET:
            field_dict["challenge_difficulties"] = challenge_difficulties
        if challenge_owns is not UNSET:
            field_dict["challenge_owns"] = challenge_owns
        if solved_tasks is not UNSET:
            field_dict["solved_tasks"] = solved_tasks
        if total_bloods is not UNSET:
            field_dict["total_bloods"] = total_bloods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge_categories import ChallengeCategories
        from ..models.challenge_difficulties import ChallengeDifficulties
        from ..models.user_profile_progress_sherlock_profile_challenge_owns import (
            UserProfileProgressSherlockProfileChallengeOwns,
        )

        d = dict(src_dict)
        _challenge_categories = d.pop("challenge_categories", UNSET)
        challenge_categories: list[ChallengeCategories] | Unset = UNSET
        if _challenge_categories is not UNSET:
            challenge_categories = []
            for componentsschemas_user_profile_progress_sherlock_profile_challenge_categories_items_item_data in _challenge_categories:
                componentsschemas_user_profile_progress_sherlock_profile_challenge_categories_items_item = ChallengeCategories.from_dict(
                    componentsschemas_user_profile_progress_sherlock_profile_challenge_categories_items_item_data
                )

                challenge_categories.append(
                    componentsschemas_user_profile_progress_sherlock_profile_challenge_categories_items_item
                )

        _challenge_difficulties = d.pop("challenge_difficulties", UNSET)
        challenge_difficulties: list[ChallengeDifficulties] | Unset = UNSET
        if _challenge_difficulties is not UNSET:
            challenge_difficulties = []
            for componentsschemas_user_profile_progress_sherlock_profile_challenge_difficulties_items_item_data in _challenge_difficulties:
                componentsschemas_user_profile_progress_sherlock_profile_challenge_difficulties_items_item = ChallengeDifficulties.from_dict(
                    componentsschemas_user_profile_progress_sherlock_profile_challenge_difficulties_items_item_data
                )

                challenge_difficulties.append(
                    componentsschemas_user_profile_progress_sherlock_profile_challenge_difficulties_items_item
                )

        _challenge_owns = d.pop("challenge_owns", UNSET)
        challenge_owns: UserProfileProgressSherlockProfileChallengeOwns | Unset
        if isinstance(_challenge_owns, Unset):
            challenge_owns = UNSET
        else:
            challenge_owns = UserProfileProgressSherlockProfileChallengeOwns.from_dict(
                _challenge_owns
            )

        solved_tasks = d.pop("solved_tasks", UNSET)

        total_bloods = d.pop("total_bloods", UNSET)

        user_profile_progress_sherlock_profile = cls(
            challenge_categories=challenge_categories,
            challenge_difficulties=challenge_difficulties,
            challenge_owns=challenge_owns,
            solved_tasks=solved_tasks,
            total_bloods=total_bloods,
        )

        user_profile_progress_sherlock_profile.additional_properties = d
        return user_profile_progress_sherlock_profile

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

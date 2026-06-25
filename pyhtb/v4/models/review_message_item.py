from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helpful_reviews import HelpfulReviews
    from ..models.review_user import ReviewUser


T = TypeVar("T", bound="ReviewMessageItem")


@_attrs_define
class ReviewMessageItem:
    """
    Attributes:
        auth_user_in_helpful_reviews (bool | Unset):
        created_at (datetime.datetime | Unset):  Example: 2023-01-28T21:42:53.000000Z.
        difficulty (int | None | Unset):
        featured (int | Unset):
        helpful_reviews (list[HelpfulReviews] | Unset):
        helpful_reviews_count (int | Unset):
        id (int | Unset):  Example: 3242342.
        message (str | Unset):  Example: User was great, would user again.
        released (int | Unset):  Example: 1.
        stars (int | Unset):  Example: 5.
        title (None | str | Unset):  Example: A++++.
        user (None | ReviewUser | Unset):
        user_id (int | Unset):  Example: 234234.
        headline (None | str | Unset):
        review (None | str | Unset):
    """

    auth_user_in_helpful_reviews: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    difficulty: int | None | Unset = UNSET
    featured: int | Unset = UNSET
    helpful_reviews: list[HelpfulReviews] | Unset = UNSET
    helpful_reviews_count: int | Unset = UNSET
    id: int | Unset = UNSET
    message: str | Unset = UNSET
    released: int | Unset = UNSET
    stars: int | Unset = UNSET
    title: None | str | Unset = UNSET
    user: None | ReviewUser | Unset = UNSET
    user_id: int | Unset = UNSET
    headline: None | str | Unset = UNSET
    review: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.review_user import ReviewUser

        auth_user_in_helpful_reviews = self.auth_user_in_helpful_reviews

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        difficulty: int | None | Unset
        if isinstance(self.difficulty, Unset):
            difficulty = UNSET
        else:
            difficulty = self.difficulty

        featured = self.featured

        helpful_reviews: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.helpful_reviews, Unset):
            helpful_reviews = []
            for (
                componentsschemas_helpful_reviews_items_item_data
            ) in self.helpful_reviews:
                componentsschemas_helpful_reviews_items_item = (
                    componentsschemas_helpful_reviews_items_item_data.to_dict()
                )
                helpful_reviews.append(componentsschemas_helpful_reviews_items_item)

        helpful_reviews_count = self.helpful_reviews_count

        id = self.id

        message = self.message

        released = self.released

        stars = self.stars

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, ReviewUser):
            user = self.user.to_dict()
        else:
            user = self.user

        user_id = self.user_id

        headline: None | str | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        review: None | str | Unset
        if isinstance(self.review, Unset):
            review = UNSET
        else:
            review = self.review

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_user_in_helpful_reviews is not UNSET:
            field_dict["authUserInHelpfulReviews"] = auth_user_in_helpful_reviews
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if featured is not UNSET:
            field_dict["featured"] = featured
        if helpful_reviews is not UNSET:
            field_dict["helpful_reviews"] = helpful_reviews
        if helpful_reviews_count is not UNSET:
            field_dict["helpful_reviews_count"] = helpful_reviews_count
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if released is not UNSET:
            field_dict["released"] = released
        if stars is not UNSET:
            field_dict["stars"] = stars
        if title is not UNSET:
            field_dict["title"] = title
        if user is not UNSET:
            field_dict["user"] = user
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if headline is not UNSET:
            field_dict["headline"] = headline
        if review is not UNSET:
            field_dict["review"] = review

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helpful_reviews import HelpfulReviews
        from ..models.review_user import ReviewUser

        d = dict(src_dict)
        auth_user_in_helpful_reviews = d.pop("authUserInHelpfulReviews", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        def _parse_difficulty(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        difficulty = _parse_difficulty(d.pop("difficulty", UNSET))

        featured = d.pop("featured", UNSET)

        _helpful_reviews = d.pop("helpful_reviews", UNSET)
        helpful_reviews: list[HelpfulReviews] | Unset = UNSET
        if _helpful_reviews is not UNSET:
            helpful_reviews = []
            for componentsschemas_helpful_reviews_items_item_data in _helpful_reviews:
                componentsschemas_helpful_reviews_items_item = HelpfulReviews.from_dict(
                    componentsschemas_helpful_reviews_items_item_data
                )

                helpful_reviews.append(componentsschemas_helpful_reviews_items_item)

        helpful_reviews_count = d.pop("helpful_reviews_count", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        released = d.pop("released", UNSET)

        stars = d.pop("stars", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_user(data: object) -> None | ReviewUser | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_basic_info_type_0 = ReviewUser.from_dict(data)

                return componentsschemas_user_basic_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewUser | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        user_id = d.pop("user_id", UNSET)

        def _parse_headline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))

        def _parse_review(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review = _parse_review(d.pop("review", UNSET))

        review_message_item = cls(
            auth_user_in_helpful_reviews=auth_user_in_helpful_reviews,
            created_at=created_at,
            difficulty=difficulty,
            featured=featured,
            helpful_reviews=helpful_reviews,
            helpful_reviews_count=helpful_reviews_count,
            id=id,
            message=message,
            released=released,
            stars=stars,
            title=title,
            user=user,
            user_id=user_id,
            headline=headline,
            review=review,
        )

        review_message_item.additional_properties = d
        return review_message_item

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

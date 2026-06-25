from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feedback_for_chart import FeedbackForChart
    from ..models.machine_creator import MachineCreator
    from ..models.machine_label import MachineLabel
    from ..models.machine_play_info import MachinePlayInfo
    from ..models.machine_retiring_type_0 import MachineRetiringType0


T = TypeVar("T", bound="MachinesItem")


@_attrs_define
class MachinesItem:
    """Schema definition for a Machine card

    Attributes:
        id (int):
        name (str):
        avatar (str):
        os (str):
        points (int):
        rating (float):
        rating_count (int):
        release_date (datetime.datetime):
        free (bool):
        difficulty (int):
        difficulty_text (str):
        user_owns_count (int):
        auth_user_in_user_owns (bool):
        root_owns_count (int):
        auth_user_has_reviewed (bool):
        auth_user_in_root_owns (bool):
        todo (bool):
        competitive (bool):
        feedback_for_chart (FeedbackForChart):
        play_info (MachinePlayInfo):
        labels (list[MachineLabel]):
        recommended (bool):
        price_tier (int):
        first_creator (MachineCreator):
        cocreators (list[MachineCreator]):
        state (str):
        task_completion_percentage (str):
        sp_flag (int):
        is_single_flag (bool):
        retired_date (datetime.datetime | None | Unset):
        active (bool | None | Unset):
        ip (None | str | Unset):
        required_subscription (None | str | Unset):
        retiring (MachineRetiringType0 | None | Unset):
    """

    id: int
    name: str
    avatar: str
    os: str
    points: int
    rating: float
    rating_count: int
    release_date: datetime.datetime
    free: bool
    difficulty: int
    difficulty_text: str
    user_owns_count: int
    auth_user_in_user_owns: bool
    root_owns_count: int
    auth_user_has_reviewed: bool
    auth_user_in_root_owns: bool
    todo: bool
    competitive: bool
    feedback_for_chart: FeedbackForChart
    play_info: MachinePlayInfo
    labels: list[MachineLabel]
    recommended: bool
    price_tier: int
    first_creator: MachineCreator
    cocreators: list[MachineCreator]
    state: str
    task_completion_percentage: str
    sp_flag: int
    is_single_flag: bool
    retired_date: datetime.datetime | None | Unset = UNSET
    active: bool | None | Unset = UNSET
    ip: None | str | Unset = UNSET
    required_subscription: None | str | Unset = UNSET
    retiring: MachineRetiringType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.machine_retiring_type_0 import MachineRetiringType0

        id = self.id

        name = self.name

        avatar = self.avatar

        os = self.os

        points = self.points

        rating = self.rating

        rating_count = self.rating_count

        release_date = self.release_date.isoformat()

        free = self.free

        difficulty = self.difficulty

        difficulty_text = self.difficulty_text

        user_owns_count = self.user_owns_count

        auth_user_in_user_owns = self.auth_user_in_user_owns

        root_owns_count = self.root_owns_count

        auth_user_has_reviewed = self.auth_user_has_reviewed

        auth_user_in_root_owns = self.auth_user_in_root_owns

        todo = self.todo

        competitive = self.competitive

        feedback_for_chart = self.feedback_for_chart.to_dict()

        play_info = self.play_info.to_dict()

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        recommended = self.recommended

        price_tier = self.price_tier

        first_creator = self.first_creator.to_dict()

        cocreators = []
        for cocreators_item_data in self.cocreators:
            cocreators_item = cocreators_item_data.to_dict()
            cocreators.append(cocreators_item)

        state = self.state

        task_completion_percentage = self.task_completion_percentage

        sp_flag = self.sp_flag

        is_single_flag = self.is_single_flag

        retired_date: None | str | Unset
        if isinstance(self.retired_date, Unset):
            retired_date = UNSET
        elif isinstance(self.retired_date, datetime.datetime):
            retired_date = self.retired_date.isoformat()
        else:
            retired_date = self.retired_date

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        required_subscription: None | str | Unset
        if isinstance(self.required_subscription, Unset):
            required_subscription = UNSET
        else:
            required_subscription = self.required_subscription

        retiring: dict[str, Any] | None | Unset
        if isinstance(self.retiring, Unset):
            retiring = UNSET
        elif isinstance(self.retiring, MachineRetiringType0):
            retiring = self.retiring.to_dict()
        else:
            retiring = self.retiring

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "avatar": avatar,
                "os": os,
                "points": points,
                "rating": rating,
                "ratingCount": rating_count,
                "releaseDate": release_date,
                "free": free,
                "difficulty": difficulty,
                "difficultyText": difficulty_text,
                "userOwnsCount": user_owns_count,
                "authUserInUserOwns": auth_user_in_user_owns,
                "rootOwnsCount": root_owns_count,
                "authUserHasReviewed": auth_user_has_reviewed,
                "authUserInRootOwns": auth_user_in_root_owns,
                "todo": todo,
                "competitive": competitive,
                "feedbackForChart": feedback_for_chart,
                "playInfo": play_info,
                "labels": labels,
                "recommended": recommended,
                "priceTier": price_tier,
                "firstCreator": first_creator,
                "cocreators": cocreators,
                "state": state,
                "taskCompletionPercentage": task_completion_percentage,
                "spFlag": sp_flag,
                "isSingleFlag": is_single_flag,
            }
        )
        if retired_date is not UNSET:
            field_dict["retiredDate"] = retired_date
        if active is not UNSET:
            field_dict["active"] = active
        if ip is not UNSET:
            field_dict["ip"] = ip
        if required_subscription is not UNSET:
            field_dict["requiredSubscription"] = required_subscription
        if retiring is not UNSET:
            field_dict["retiring"] = retiring

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_for_chart import FeedbackForChart
        from ..models.machine_creator import MachineCreator
        from ..models.machine_label import MachineLabel
        from ..models.machine_play_info import MachinePlayInfo
        from ..models.machine_retiring_type_0 import MachineRetiringType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        avatar = d.pop("avatar")

        os = d.pop("os")

        points = d.pop("points")

        rating = d.pop("rating")

        rating_count = d.pop("ratingCount")

        release_date = datetime.datetime.fromisoformat(d.pop("releaseDate"))

        free = d.pop("free")

        difficulty = d.pop("difficulty")

        difficulty_text = d.pop("difficultyText")

        user_owns_count = d.pop("userOwnsCount")

        auth_user_in_user_owns = d.pop("authUserInUserOwns")

        root_owns_count = d.pop("rootOwnsCount")

        auth_user_has_reviewed = d.pop("authUserHasReviewed")

        auth_user_in_root_owns = d.pop("authUserInRootOwns")

        todo = d.pop("todo")

        competitive = d.pop("competitive")

        feedback_for_chart = FeedbackForChart.from_dict(d.pop("feedbackForChart"))

        play_info = MachinePlayInfo.from_dict(d.pop("playInfo"))

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = MachineLabel.from_dict(labels_item_data)

            labels.append(labels_item)

        recommended = d.pop("recommended")

        price_tier = d.pop("priceTier")

        first_creator = MachineCreator.from_dict(d.pop("firstCreator"))

        cocreators = []
        _cocreators = d.pop("cocreators")
        for cocreators_item_data in _cocreators:
            cocreators_item = MachineCreator.from_dict(cocreators_item_data)

            cocreators.append(cocreators_item)

        state = d.pop("state")

        task_completion_percentage = d.pop("taskCompletionPercentage")

        sp_flag = d.pop("spFlag")

        is_single_flag = d.pop("isSingleFlag")

        def _parse_retired_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retired_date_type_0 = datetime.datetime.fromisoformat(data)

                return retired_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        retired_date = _parse_retired_date(d.pop("retiredDate", UNSET))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        def _parse_required_subscription(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        required_subscription = _parse_required_subscription(
            d.pop("requiredSubscription", UNSET)
        )

        def _parse_retiring(data: object) -> MachineRetiringType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_machine_retiring_type_0 = (
                    MachineRetiringType0.from_dict(data)
                )

                return componentsschemas_machine_retiring_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MachineRetiringType0 | None | Unset, data)

        retiring = _parse_retiring(d.pop("retiring", UNSET))

        machines_item = cls(
            id=id,
            name=name,
            avatar=avatar,
            os=os,
            points=points,
            rating=rating,
            rating_count=rating_count,
            release_date=release_date,
            free=free,
            difficulty=difficulty,
            difficulty_text=difficulty_text,
            user_owns_count=user_owns_count,
            auth_user_in_user_owns=auth_user_in_user_owns,
            root_owns_count=root_owns_count,
            auth_user_has_reviewed=auth_user_has_reviewed,
            auth_user_in_root_owns=auth_user_in_root_owns,
            todo=todo,
            competitive=competitive,
            feedback_for_chart=feedback_for_chart,
            play_info=play_info,
            labels=labels,
            recommended=recommended,
            price_tier=price_tier,
            first_creator=first_creator,
            cocreators=cocreators,
            state=state,
            task_completion_percentage=task_completion_percentage,
            sp_flag=sp_flag,
            is_single_flag=is_single_flag,
            retired_date=retired_date,
            active=active,
            ip=ip,
            required_subscription=required_subscription,
            retiring=retiring,
        )

        machines_item.additional_properties = d
        return machines_item

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

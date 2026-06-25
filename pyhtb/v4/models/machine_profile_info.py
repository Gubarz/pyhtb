from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.academy_module import AcademyModule
    from ..models.blood_info import BloodInfo
    from ..models.difficulty_chart_type_1 import DifficultyChartType1
    from ..models.maker import Maker
    from ..models.play_info import PlayInfo


T = TypeVar("T", bound="MachineProfileInfo")


@_attrs_define
class MachineProfileInfo:
    """Schema definition for Machine Profile Info

    Attributes:
        academy_modules (list[AcademyModule] | None | Unset):
        active (bool | Unset):
        auth_user_first_root_time (None | str | Unset):  Example: 18H 6M 57S.
        auth_user_first_user_time (None | str | Unset):  Example: 3H 47M 43S.
        auth_user_has_reviewed (bool | Unset):
        auth_user_has_submitted_matrix (bool | Unset):
        auth_user_in_root_owns (bool | Unset):  Example: True.
        auth_user_in_user_owns (bool | Unset):  Example: True.
        avatar (str | Unset):  Example: /storage/avatars/a2c2bd7b4e98ff8b782ed590896305a1.png.
        can_access_walkthrough (bool | Unset):
        difficulty_text (str | Unset):  Example: Medium.
        feedback_for_chart (DifficultyChartType1 | list[Any] | Unset):
        free (bool | Unset):  Example: True.
        has_changelog (bool | Unset):
        id (int | Unset):  Example: 601.
        info_status (None | str | Unset):
        machine_pwned_date (str | Unset):
        ip (None | str | Unset):  Example: 10.10.10.10.
        is_guided_enabled (bool | Unset):
        is_todo (bool | Unset):
        machine_mode (None | str | Unset):  Example: seasonal.
        maker (Maker | None | Unset): Schema definition for Maker
        maker2 (Maker | None | Unset): Schema definition for Maker
        name (str | Unset):  Example: SolarLab.
        os (str | Unset):  Example: Windows.
        own_rank (int | None | Unset):  Example: 292.
        play_info (PlayInfo | Unset): Schema definition for Play Info
        points (int | Unset):  Example: 30.
        recommended (bool | Unset):
        release (datetime.datetime | Unset):  Example: 2024-05-11T19:00:00.000000Z.
        retired (bool | Unset):
        reviews_count (int | Unset):  Example: 71.
        root_blood (BloodInfo | Unset): Schema definition for Blood Info
        root_owns_count (int | Unset):  Example: 1355.
        season_id (int | None | Unset):  Example: 5.
        show_go_vip (bool | Unset):
        show_go_vip_server (bool | Unset):
        sp_flag (int | Unset):
        stars (float | Unset):  Example: 4.6.
        start_mode (str | Unset):  Example: spawn.
        static_points (int | Unset):  Example: 30.
        synopsis (None | str | Unset):
        user_blood (BloodInfo | Unset): Schema definition for Blood Info
        user_can_review (bool | Unset):
        user_owns_count (int | Unset):  Example: 1573.
        price_tier (int | Unset):
        required_subscription (None | str | Unset):
        switch_server_warning (None | str | Unset):
        is_single_flag (bool | Unset):
        bot_has_blood (bool | Unset):
        experience_points (int | Unset):
    """

    academy_modules: list[AcademyModule] | None | Unset = UNSET
    active: bool | Unset = UNSET
    auth_user_first_root_time: None | str | Unset = UNSET
    auth_user_first_user_time: None | str | Unset = UNSET
    auth_user_has_reviewed: bool | Unset = UNSET
    auth_user_has_submitted_matrix: bool | Unset = UNSET
    auth_user_in_root_owns: bool | Unset = UNSET
    auth_user_in_user_owns: bool | Unset = UNSET
    avatar: str | Unset = UNSET
    can_access_walkthrough: bool | Unset = UNSET
    difficulty_text: str | Unset = UNSET
    feedback_for_chart: DifficultyChartType1 | list[Any] | Unset = UNSET
    free: bool | Unset = UNSET
    has_changelog: bool | Unset = UNSET
    id: int | Unset = UNSET
    info_status: None | str | Unset = UNSET
    machine_pwned_date: str | Unset = UNSET
    ip: None | str | Unset = UNSET
    is_guided_enabled: bool | Unset = UNSET
    is_todo: bool | Unset = UNSET
    machine_mode: None | str | Unset = UNSET
    maker: Maker | None | Unset = UNSET
    maker2: Maker | None | Unset = UNSET
    name: str | Unset = UNSET
    os: str | Unset = UNSET
    own_rank: int | None | Unset = UNSET
    play_info: PlayInfo | Unset = UNSET
    points: int | Unset = UNSET
    recommended: bool | Unset = UNSET
    release: datetime.datetime | Unset = UNSET
    retired: bool | Unset = UNSET
    reviews_count: int | Unset = UNSET
    root_blood: BloodInfo | Unset = UNSET
    root_owns_count: int | Unset = UNSET
    season_id: int | None | Unset = UNSET
    show_go_vip: bool | Unset = UNSET
    show_go_vip_server: bool | Unset = UNSET
    sp_flag: int | Unset = UNSET
    stars: float | Unset = UNSET
    start_mode: str | Unset = UNSET
    static_points: int | Unset = UNSET
    synopsis: None | str | Unset = UNSET
    user_blood: BloodInfo | Unset = UNSET
    user_can_review: bool | Unset = UNSET
    user_owns_count: int | Unset = UNSET
    price_tier: int | Unset = UNSET
    required_subscription: None | str | Unset = UNSET
    switch_server_warning: None | str | Unset = UNSET
    is_single_flag: bool | Unset = UNSET
    bot_has_blood: bool | Unset = UNSET
    experience_points: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.maker import Maker

        academy_modules: list[dict[str, Any]] | None | Unset
        if isinstance(self.academy_modules, Unset):
            academy_modules = UNSET
        elif isinstance(self.academy_modules, list):
            academy_modules = []
            for (
                componentsschemas_academy_modules_items_type_0_item_data
            ) in self.academy_modules:
                componentsschemas_academy_modules_items_type_0_item = (
                    componentsschemas_academy_modules_items_type_0_item_data.to_dict()
                )
                academy_modules.append(
                    componentsschemas_academy_modules_items_type_0_item
                )

        else:
            academy_modules = self.academy_modules

        active = self.active

        auth_user_first_root_time: None | str | Unset
        if isinstance(self.auth_user_first_root_time, Unset):
            auth_user_first_root_time = UNSET
        else:
            auth_user_first_root_time = self.auth_user_first_root_time

        auth_user_first_user_time: None | str | Unset
        if isinstance(self.auth_user_first_user_time, Unset):
            auth_user_first_user_time = UNSET
        else:
            auth_user_first_user_time = self.auth_user_first_user_time

        auth_user_has_reviewed = self.auth_user_has_reviewed

        auth_user_has_submitted_matrix = self.auth_user_has_submitted_matrix

        auth_user_in_root_owns = self.auth_user_in_root_owns

        auth_user_in_user_owns = self.auth_user_in_user_owns

        avatar = self.avatar

        can_access_walkthrough = self.can_access_walkthrough

        difficulty_text = self.difficulty_text

        feedback_for_chart: dict[str, Any] | list[Any] | Unset
        if isinstance(self.feedback_for_chart, Unset):
            feedback_for_chart = UNSET
        elif isinstance(self.feedback_for_chart, list):
            feedback_for_chart = self.feedback_for_chart

        else:
            feedback_for_chart = self.feedback_for_chart.to_dict()

        free = self.free

        has_changelog = self.has_changelog

        id = self.id

        info_status: None | str | Unset
        if isinstance(self.info_status, Unset):
            info_status = UNSET
        else:
            info_status = self.info_status

        machine_pwned_date = self.machine_pwned_date

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        is_guided_enabled = self.is_guided_enabled

        is_todo = self.is_todo

        machine_mode: None | str | Unset
        if isinstance(self.machine_mode, Unset):
            machine_mode = UNSET
        else:
            machine_mode = self.machine_mode

        maker: dict[str, Any] | None | Unset
        if isinstance(self.maker, Unset):
            maker = UNSET
        elif isinstance(self.maker, Maker):
            maker = self.maker.to_dict()
        else:
            maker = self.maker

        maker2: dict[str, Any] | None | Unset
        if isinstance(self.maker2, Unset):
            maker2 = UNSET
        elif isinstance(self.maker2, Maker):
            maker2 = self.maker2.to_dict()
        else:
            maker2 = self.maker2

        name = self.name

        os = self.os

        own_rank: int | None | Unset
        if isinstance(self.own_rank, Unset):
            own_rank = UNSET
        else:
            own_rank = self.own_rank

        play_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.play_info, Unset):
            play_info = self.play_info.to_dict()

        points = self.points

        recommended = self.recommended

        release: str | Unset = UNSET
        if not isinstance(self.release, Unset):
            release = self.release.isoformat()

        retired = self.retired

        reviews_count = self.reviews_count

        root_blood: dict[str, Any] | Unset = UNSET
        if not isinstance(self.root_blood, Unset):
            root_blood = self.root_blood.to_dict()

        root_owns_count = self.root_owns_count

        season_id: int | None | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        else:
            season_id = self.season_id

        show_go_vip = self.show_go_vip

        show_go_vip_server = self.show_go_vip_server

        sp_flag = self.sp_flag

        stars = self.stars

        start_mode = self.start_mode

        static_points = self.static_points

        synopsis: None | str | Unset
        if isinstance(self.synopsis, Unset):
            synopsis = UNSET
        else:
            synopsis = self.synopsis

        user_blood: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_blood, Unset):
            user_blood = self.user_blood.to_dict()

        user_can_review = self.user_can_review

        user_owns_count = self.user_owns_count

        price_tier = self.price_tier

        required_subscription: None | str | Unset
        if isinstance(self.required_subscription, Unset):
            required_subscription = UNSET
        else:
            required_subscription = self.required_subscription

        switch_server_warning: None | str | Unset
        if isinstance(self.switch_server_warning, Unset):
            switch_server_warning = UNSET
        else:
            switch_server_warning = self.switch_server_warning

        is_single_flag = self.is_single_flag

        bot_has_blood = self.bot_has_blood

        experience_points = self.experience_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if academy_modules is not UNSET:
            field_dict["academy_modules"] = academy_modules
        if active is not UNSET:
            field_dict["active"] = active
        if auth_user_first_root_time is not UNSET:
            field_dict["authUserFirstRootTime"] = auth_user_first_root_time
        if auth_user_first_user_time is not UNSET:
            field_dict["authUserFirstUserTime"] = auth_user_first_user_time
        if auth_user_has_reviewed is not UNSET:
            field_dict["authUserHasReviewed"] = auth_user_has_reviewed
        if auth_user_has_submitted_matrix is not UNSET:
            field_dict["authUserHasSubmittedMatrix"] = auth_user_has_submitted_matrix
        if auth_user_in_root_owns is not UNSET:
            field_dict["authUserInRootOwns"] = auth_user_in_root_owns
        if auth_user_in_user_owns is not UNSET:
            field_dict["authUserInUserOwns"] = auth_user_in_user_owns
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if can_access_walkthrough is not UNSET:
            field_dict["can_access_walkthrough"] = can_access_walkthrough
        if difficulty_text is not UNSET:
            field_dict["difficultyText"] = difficulty_text
        if feedback_for_chart is not UNSET:
            field_dict["feedbackForChart"] = feedback_for_chart
        if free is not UNSET:
            field_dict["free"] = free
        if has_changelog is not UNSET:
            field_dict["has_changelog"] = has_changelog
        if id is not UNSET:
            field_dict["id"] = id
        if info_status is not UNSET:
            field_dict["info_status"] = info_status
        if machine_pwned_date is not UNSET:
            field_dict["machinePwnedDate"] = machine_pwned_date
        if ip is not UNSET:
            field_dict["ip"] = ip
        if is_guided_enabled is not UNSET:
            field_dict["isGuidedEnabled"] = is_guided_enabled
        if is_todo is not UNSET:
            field_dict["isTodo"] = is_todo
        if machine_mode is not UNSET:
            field_dict["machine_mode"] = machine_mode
        if maker is not UNSET:
            field_dict["maker"] = maker
        if maker2 is not UNSET:
            field_dict["maker2"] = maker2
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if own_rank is not UNSET:
            field_dict["ownRank"] = own_rank
        if play_info is not UNSET:
            field_dict["playInfo"] = play_info
        if points is not UNSET:
            field_dict["points"] = points
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if release is not UNSET:
            field_dict["release"] = release
        if retired is not UNSET:
            field_dict["retired"] = retired
        if reviews_count is not UNSET:
            field_dict["reviews_count"] = reviews_count
        if root_blood is not UNSET:
            field_dict["rootBlood"] = root_blood
        if root_owns_count is not UNSET:
            field_dict["root_owns_count"] = root_owns_count
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if show_go_vip is not UNSET:
            field_dict["show_go_vip"] = show_go_vip
        if show_go_vip_server is not UNSET:
            field_dict["show_go_vip_server"] = show_go_vip_server
        if sp_flag is not UNSET:
            field_dict["sp_flag"] = sp_flag
        if stars is not UNSET:
            field_dict["stars"] = stars
        if start_mode is not UNSET:
            field_dict["start_mode"] = start_mode
        if static_points is not UNSET:
            field_dict["static_points"] = static_points
        if synopsis is not UNSET:
            field_dict["synopsis"] = synopsis
        if user_blood is not UNSET:
            field_dict["userBlood"] = user_blood
        if user_can_review is not UNSET:
            field_dict["user_can_review"] = user_can_review
        if user_owns_count is not UNSET:
            field_dict["user_owns_count"] = user_owns_count
        if price_tier is not UNSET:
            field_dict["priceTier"] = price_tier
        if required_subscription is not UNSET:
            field_dict["requiredSubscription"] = required_subscription
        if switch_server_warning is not UNSET:
            field_dict["switchServerWarning"] = switch_server_warning
        if is_single_flag is not UNSET:
            field_dict["isSingleFlag"] = is_single_flag
        if bot_has_blood is not UNSET:
            field_dict["botHasBlood"] = bot_has_blood
        if experience_points is not UNSET:
            field_dict["experience_points"] = experience_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.academy_module import AcademyModule
        from ..models.blood_info import BloodInfo
        from ..models.difficulty_chart_type_1 import DifficultyChartType1
        from ..models.maker import Maker
        from ..models.play_info import PlayInfo

        d = dict(src_dict)

        def _parse_academy_modules(data: object) -> list[AcademyModule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_academy_modules_items_type_0 = []
                _componentsschemas_academy_modules_items_type_0 = data
                for (
                    componentsschemas_academy_modules_items_type_0_item_data
                ) in _componentsschemas_academy_modules_items_type_0:
                    componentsschemas_academy_modules_items_type_0_item = (
                        AcademyModule.from_dict(
                            componentsschemas_academy_modules_items_type_0_item_data
                        )
                    )

                    componentsschemas_academy_modules_items_type_0.append(
                        componentsschemas_academy_modules_items_type_0_item
                    )

                return componentsschemas_academy_modules_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AcademyModule] | None | Unset, data)

        academy_modules = _parse_academy_modules(d.pop("academy_modules", UNSET))

        active = d.pop("active", UNSET)

        def _parse_auth_user_first_root_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_user_first_root_time = _parse_auth_user_first_root_time(
            d.pop("authUserFirstRootTime", UNSET)
        )

        def _parse_auth_user_first_user_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_user_first_user_time = _parse_auth_user_first_user_time(
            d.pop("authUserFirstUserTime", UNSET)
        )

        auth_user_has_reviewed = d.pop("authUserHasReviewed", UNSET)

        auth_user_has_submitted_matrix = d.pop("authUserHasSubmittedMatrix", UNSET)

        auth_user_in_root_owns = d.pop("authUserInRootOwns", UNSET)

        auth_user_in_user_owns = d.pop("authUserInUserOwns", UNSET)

        avatar = d.pop("avatar", UNSET)

        can_access_walkthrough = d.pop("can_access_walkthrough", UNSET)

        difficulty_text = d.pop("difficultyText", UNSET)

        def _parse_feedback_for_chart(
            data: object,
        ) -> DifficultyChartType1 | list[Any] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_difficulty_chart_type_0 = cast(list[Any], data)

                return componentsschemas_difficulty_chart_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_difficulty_chart_type_1 = DifficultyChartType1.from_dict(
                data
            )

            return componentsschemas_difficulty_chart_type_1

        feedback_for_chart = _parse_feedback_for_chart(d.pop("feedbackForChart", UNSET))

        free = d.pop("free", UNSET)

        has_changelog = d.pop("has_changelog", UNSET)

        id = d.pop("id", UNSET)

        def _parse_info_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        info_status = _parse_info_status(d.pop("info_status", UNSET))

        machine_pwned_date = d.pop("machinePwnedDate", UNSET)

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        is_guided_enabled = d.pop("isGuidedEnabled", UNSET)

        is_todo = d.pop("isTodo", UNSET)

        def _parse_machine_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        machine_mode = _parse_machine_mode(d.pop("machine_mode", UNSET))

        def _parse_maker(data: object) -> Maker | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_maker_type_0 = Maker.from_dict(data)

                return componentsschemas_maker_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Maker | None | Unset, data)

        maker = _parse_maker(d.pop("maker", UNSET))

        def _parse_maker2(data: object) -> Maker | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_maker_type_0 = Maker.from_dict(data)

                return componentsschemas_maker_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Maker | None | Unset, data)

        maker2 = _parse_maker2(d.pop("maker2", UNSET))

        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        def _parse_own_rank(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        own_rank = _parse_own_rank(d.pop("ownRank", UNSET))

        _play_info = d.pop("playInfo", UNSET)
        play_info: PlayInfo | Unset
        if isinstance(_play_info, Unset):
            play_info = UNSET
        else:
            play_info = PlayInfo.from_dict(_play_info)

        points = d.pop("points", UNSET)

        recommended = d.pop("recommended", UNSET)

        _release = d.pop("release", UNSET)
        release: datetime.datetime | Unset
        if isinstance(_release, Unset):
            release = UNSET
        else:
            release = datetime.datetime.fromisoformat(_release)

        retired = d.pop("retired", UNSET)

        reviews_count = d.pop("reviews_count", UNSET)

        _root_blood = d.pop("rootBlood", UNSET)
        root_blood: BloodInfo | Unset
        if isinstance(_root_blood, Unset):
            root_blood = UNSET
        else:
            root_blood = BloodInfo.from_dict(_root_blood)

        root_owns_count = d.pop("root_owns_count", UNSET)

        def _parse_season_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        season_id = _parse_season_id(d.pop("season_id", UNSET))

        show_go_vip = d.pop("show_go_vip", UNSET)

        show_go_vip_server = d.pop("show_go_vip_server", UNSET)

        sp_flag = d.pop("sp_flag", UNSET)

        stars = d.pop("stars", UNSET)

        start_mode = d.pop("start_mode", UNSET)

        static_points = d.pop("static_points", UNSET)

        def _parse_synopsis(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        synopsis = _parse_synopsis(d.pop("synopsis", UNSET))

        _user_blood = d.pop("userBlood", UNSET)
        user_blood: BloodInfo | Unset
        if isinstance(_user_blood, Unset):
            user_blood = UNSET
        else:
            user_blood = BloodInfo.from_dict(_user_blood)

        user_can_review = d.pop("user_can_review", UNSET)

        user_owns_count = d.pop("user_owns_count", UNSET)

        price_tier = d.pop("priceTier", UNSET)

        def _parse_required_subscription(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        required_subscription = _parse_required_subscription(
            d.pop("requiredSubscription", UNSET)
        )

        def _parse_switch_server_warning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        switch_server_warning = _parse_switch_server_warning(
            d.pop("switchServerWarning", UNSET)
        )

        is_single_flag = d.pop("isSingleFlag", UNSET)

        bot_has_blood = d.pop("botHasBlood", UNSET)

        experience_points = d.pop("experience_points", UNSET)

        machine_profile_info = cls(
            academy_modules=academy_modules,
            active=active,
            auth_user_first_root_time=auth_user_first_root_time,
            auth_user_first_user_time=auth_user_first_user_time,
            auth_user_has_reviewed=auth_user_has_reviewed,
            auth_user_has_submitted_matrix=auth_user_has_submitted_matrix,
            auth_user_in_root_owns=auth_user_in_root_owns,
            auth_user_in_user_owns=auth_user_in_user_owns,
            avatar=avatar,
            can_access_walkthrough=can_access_walkthrough,
            difficulty_text=difficulty_text,
            feedback_for_chart=feedback_for_chart,
            free=free,
            has_changelog=has_changelog,
            id=id,
            info_status=info_status,
            machine_pwned_date=machine_pwned_date,
            ip=ip,
            is_guided_enabled=is_guided_enabled,
            is_todo=is_todo,
            machine_mode=machine_mode,
            maker=maker,
            maker2=maker2,
            name=name,
            os=os,
            own_rank=own_rank,
            play_info=play_info,
            points=points,
            recommended=recommended,
            release=release,
            retired=retired,
            reviews_count=reviews_count,
            root_blood=root_blood,
            root_owns_count=root_owns_count,
            season_id=season_id,
            show_go_vip=show_go_vip,
            show_go_vip_server=show_go_vip_server,
            sp_flag=sp_flag,
            stars=stars,
            start_mode=start_mode,
            static_points=static_points,
            synopsis=synopsis,
            user_blood=user_blood,
            user_can_review=user_can_review,
            user_owns_count=user_owns_count,
            price_tier=price_tier,
            required_subscription=required_subscription,
            switch_server_warning=switch_server_warning,
            is_single_flag=is_single_flag,
            bot_has_blood=bot_has_blood,
            experience_points=experience_points,
        )

        machine_profile_info.additional_properties = d
        return machine_profile_info

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

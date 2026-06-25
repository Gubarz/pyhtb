from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.difficulty_chart_type_1 import DifficultyChartType1
    from ..models.play_info_alt import PlayInfoAlt
    from ..models.tag import Tag


T = TypeVar("T", bound="Challenge")


@_attrs_define
class Challenge:
    """Schema definition for Challenge

    Attributes:
        auth_user_has_reviewed (bool | Unset):
        reviews_count (int | Unset):
        play_info (PlayInfoAlt | Unset): Alternate structure of PlayInfo used in Sherlocks and Challenges
        docker_status (None | str | Unset):
        show_go_vip (bool | Unset):
        has_changelog (bool | Unset):
        auth_user_solve (bool | Unset):
        auth_user_solve_time (None | str | Unset):
        can_access_walkthough (bool | Unset):
        category_name (str | Unset):  Example: Crypto.
        creator2_avatar (None | str | Unset):
        creator2_id (int | None | Unset):
        creator2_name (None | str | Unset):
        creator_avatar (str | Unset):  Example: /storage/avatars/2a956277f4de5800bf659c63cbbd140b.png.
        creator_id (int | Unset):  Example: 185587.
        creator_name (str | Unset):  Example: DaysOfLife.
        description (str | Unset):  Example: The more the merrier, right? We decided to mash two of the best
            cryptosytems together for the best product....
        difficulty (str | Unset):  Example: Medium.
        difficulty_chart (DifficultyChartType1 | list[Any] | Unset):
        dislike_by_auth_user (bool | Unset):
        dislikes (int | Unset):
        docker (bool | None | Unset):  Example: True.
        docker_ip (None | str | Unset):
        docker_ports (list[int] | None | Unset):
        download (bool | Unset):  Example: True.
        file_name (None | str | Unset):
        file_size (None | str | Unset):
        first_blood_time (str | Unset):  Example: 0H 39M 49S.
        first_blood_user (str | Unset):  Example: sampriti.
        first_blood_user_avatar (str | Unset):  Example: /storage/avatars/03d6176149e9fe81c83590dd4e7a5225.png.
        first_blood_user_id (int | Unset):  Example: 836.
        id (int | Unset):  Example: 206.
        is_respected (bool | Unset):
        is_respected_2 (bool | None | Unset):
        is_todo (bool | Unset):
        like_by_auth_user (bool | Unset):
        likes (int | Unset):
        name (str | Unset):  Example: Composition.
        play_methods (list[None | str] | None | Unset):
        points (int | str | Unset):
        recommended (int | Unset):
        release_date (datetime.datetime | Unset):  Example: 2021-04-02T20:00:00.000000Z.
        released (int | Unset):  Example: 1.
        retired (bool | Unset):  Example: True.
        sha256 (None | str | Unset):  Example: b3edd221b1ca7ae93673ddcbdfe5dbe2109998db2865f0e1b8ec5cc9fac56492.
        solves (int | Unset):  Example: 704.
        stars (float | Unset):  Example: 4.8.
        state (str | Unset):  Example: retired.
        tags (list[Tag] | Unset):
        user_can_review (bool | Unset):  Example: True.
        user_submitted_difficulty (int | None | Unset):
        avatar_url (str | Unset):
        experience_points (int | Unset):
    """

    auth_user_has_reviewed: bool | Unset = UNSET
    reviews_count: int | Unset = UNSET
    play_info: PlayInfoAlt | Unset = UNSET
    docker_status: None | str | Unset = UNSET
    show_go_vip: bool | Unset = UNSET
    has_changelog: bool | Unset = UNSET
    auth_user_solve: bool | Unset = UNSET
    auth_user_solve_time: None | str | Unset = UNSET
    can_access_walkthough: bool | Unset = UNSET
    category_name: str | Unset = UNSET
    creator2_avatar: None | str | Unset = UNSET
    creator2_id: int | None | Unset = UNSET
    creator2_name: None | str | Unset = UNSET
    creator_avatar: str | Unset = UNSET
    creator_id: int | Unset = UNSET
    creator_name: str | Unset = UNSET
    description: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    difficulty_chart: DifficultyChartType1 | list[Any] | Unset = UNSET
    dislike_by_auth_user: bool | Unset = UNSET
    dislikes: int | Unset = UNSET
    docker: bool | None | Unset = UNSET
    docker_ip: None | str | Unset = UNSET
    docker_ports: list[int] | None | Unset = UNSET
    download: bool | Unset = UNSET
    file_name: None | str | Unset = UNSET
    file_size: None | str | Unset = UNSET
    first_blood_time: str | Unset = UNSET
    first_blood_user: str | Unset = UNSET
    first_blood_user_avatar: str | Unset = UNSET
    first_blood_user_id: int | Unset = UNSET
    id: int | Unset = UNSET
    is_respected: bool | Unset = UNSET
    is_respected_2: bool | None | Unset = UNSET
    is_todo: bool | Unset = UNSET
    like_by_auth_user: bool | Unset = UNSET
    likes: int | Unset = UNSET
    name: str | Unset = UNSET
    play_methods: list[None | str] | None | Unset = UNSET
    points: int | str | Unset = UNSET
    recommended: int | Unset = UNSET
    release_date: datetime.datetime | Unset = UNSET
    released: int | Unset = UNSET
    retired: bool | Unset = UNSET
    sha256: None | str | Unset = UNSET
    solves: int | Unset = UNSET
    stars: float | Unset = UNSET
    state: str | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    user_can_review: bool | Unset = UNSET
    user_submitted_difficulty: int | None | Unset = UNSET
    avatar_url: str | Unset = UNSET
    experience_points: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_user_has_reviewed = self.auth_user_has_reviewed

        reviews_count = self.reviews_count

        play_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.play_info, Unset):
            play_info = self.play_info.to_dict()

        docker_status: None | str | Unset
        if isinstance(self.docker_status, Unset):
            docker_status = UNSET
        else:
            docker_status = self.docker_status

        show_go_vip = self.show_go_vip

        has_changelog = self.has_changelog

        auth_user_solve = self.auth_user_solve

        auth_user_solve_time: None | str | Unset
        if isinstance(self.auth_user_solve_time, Unset):
            auth_user_solve_time = UNSET
        else:
            auth_user_solve_time = self.auth_user_solve_time

        can_access_walkthough = self.can_access_walkthough

        category_name = self.category_name

        creator2_avatar: None | str | Unset
        if isinstance(self.creator2_avatar, Unset):
            creator2_avatar = UNSET
        else:
            creator2_avatar = self.creator2_avatar

        creator2_id: int | None | Unset
        if isinstance(self.creator2_id, Unset):
            creator2_id = UNSET
        else:
            creator2_id = self.creator2_id

        creator2_name: None | str | Unset
        if isinstance(self.creator2_name, Unset):
            creator2_name = UNSET
        else:
            creator2_name = self.creator2_name

        creator_avatar = self.creator_avatar

        creator_id = self.creator_id

        creator_name = self.creator_name

        description = self.description

        difficulty = self.difficulty

        difficulty_chart: dict[str, Any] | list[Any] | Unset
        if isinstance(self.difficulty_chart, Unset):
            difficulty_chart = UNSET
        elif isinstance(self.difficulty_chart, list):
            difficulty_chart = self.difficulty_chart

        else:
            difficulty_chart = self.difficulty_chart.to_dict()

        dislike_by_auth_user = self.dislike_by_auth_user

        dislikes = self.dislikes

        docker: bool | None | Unset
        if isinstance(self.docker, Unset):
            docker = UNSET
        else:
            docker = self.docker

        docker_ip: None | str | Unset
        if isinstance(self.docker_ip, Unset):
            docker_ip = UNSET
        else:
            docker_ip = self.docker_ip

        docker_ports: list[int] | None | Unset
        if isinstance(self.docker_ports, Unset):
            docker_ports = UNSET
        elif isinstance(self.docker_ports, list):
            docker_ports = self.docker_ports

        else:
            docker_ports = self.docker_ports

        download = self.download

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_size: None | str | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        first_blood_time = self.first_blood_time

        first_blood_user = self.first_blood_user

        first_blood_user_avatar = self.first_blood_user_avatar

        first_blood_user_id = self.first_blood_user_id

        id = self.id

        is_respected = self.is_respected

        is_respected_2: bool | None | Unset
        if isinstance(self.is_respected_2, Unset):
            is_respected_2 = UNSET
        else:
            is_respected_2 = self.is_respected_2

        is_todo = self.is_todo

        like_by_auth_user = self.like_by_auth_user

        likes = self.likes

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

        points: int | str | Unset
        if isinstance(self.points, Unset):
            points = UNSET
        else:
            points = self.points

        recommended = self.recommended

        release_date: str | Unset = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        released = self.released

        retired = self.retired

        sha256: None | str | Unset
        if isinstance(self.sha256, Unset):
            sha256 = UNSET
        else:
            sha256 = self.sha256

        solves = self.solves

        stars = self.stars

        state = self.state

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for componentsschemas_tag_category_tags_items_item_data in self.tags:
                componentsschemas_tag_category_tags_items_item = (
                    componentsschemas_tag_category_tags_items_item_data.to_dict()
                )
                tags.append(componentsschemas_tag_category_tags_items_item)

        user_can_review = self.user_can_review

        user_submitted_difficulty: int | None | Unset
        if isinstance(self.user_submitted_difficulty, Unset):
            user_submitted_difficulty = UNSET
        else:
            user_submitted_difficulty = self.user_submitted_difficulty

        avatar_url = self.avatar_url

        experience_points = self.experience_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_user_has_reviewed is not UNSET:
            field_dict["authUserHasReviewed"] = auth_user_has_reviewed
        if reviews_count is not UNSET:
            field_dict["reviews_count"] = reviews_count
        if play_info is not UNSET:
            field_dict["play_info"] = play_info
        if docker_status is not UNSET:
            field_dict["docker_status"] = docker_status
        if show_go_vip is not UNSET:
            field_dict["show_go_vip"] = show_go_vip
        if has_changelog is not UNSET:
            field_dict["has_changelog"] = has_changelog
        if auth_user_solve is not UNSET:
            field_dict["authUserSolve"] = auth_user_solve
        if auth_user_solve_time is not UNSET:
            field_dict["authUserSolveTime"] = auth_user_solve_time
        if can_access_walkthough is not UNSET:
            field_dict["can_access_walkthough"] = can_access_walkthough
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if creator2_avatar is not UNSET:
            field_dict["creator2_avatar"] = creator2_avatar
        if creator2_id is not UNSET:
            field_dict["creator2_id"] = creator2_id
        if creator2_name is not UNSET:
            field_dict["creator2_name"] = creator2_name
        if creator_avatar is not UNSET:
            field_dict["creator_avatar"] = creator_avatar
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if creator_name is not UNSET:
            field_dict["creator_name"] = creator_name
        if description is not UNSET:
            field_dict["description"] = description
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if difficulty_chart is not UNSET:
            field_dict["difficulty_chart"] = difficulty_chart
        if dislike_by_auth_user is not UNSET:
            field_dict["dislikeByAuthUser"] = dislike_by_auth_user
        if dislikes is not UNSET:
            field_dict["dislikes"] = dislikes
        if docker is not UNSET:
            field_dict["docker"] = docker
        if docker_ip is not UNSET:
            field_dict["docker_ip"] = docker_ip
        if docker_ports is not UNSET:
            field_dict["docker_ports"] = docker_ports
        if download is not UNSET:
            field_dict["download"] = download
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if first_blood_time is not UNSET:
            field_dict["first_blood_time"] = first_blood_time
        if first_blood_user is not UNSET:
            field_dict["first_blood_user"] = first_blood_user
        if first_blood_user_avatar is not UNSET:
            field_dict["first_blood_user_avatar"] = first_blood_user_avatar
        if first_blood_user_id is not UNSET:
            field_dict["first_blood_user_id"] = first_blood_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_respected is not UNSET:
            field_dict["isRespected"] = is_respected
        if is_respected_2 is not UNSET:
            field_dict["isRespected2"] = is_respected_2
        if is_todo is not UNSET:
            field_dict["isTodo"] = is_todo
        if like_by_auth_user is not UNSET:
            field_dict["likeByAuthUser"] = like_by_auth_user
        if likes is not UNSET:
            field_dict["likes"] = likes
        if name is not UNSET:
            field_dict["name"] = name
        if play_methods is not UNSET:
            field_dict["play_methods"] = play_methods
        if points is not UNSET:
            field_dict["points"] = points
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if released is not UNSET:
            field_dict["released"] = released
        if retired is not UNSET:
            field_dict["retired"] = retired
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if solves is not UNSET:
            field_dict["solves"] = solves
        if stars is not UNSET:
            field_dict["stars"] = stars
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if user_can_review is not UNSET:
            field_dict["user_can_review"] = user_can_review
        if user_submitted_difficulty is not UNSET:
            field_dict["user_submitted_difficulty"] = user_submitted_difficulty
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if experience_points is not UNSET:
            field_dict["experience_points"] = experience_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.difficulty_chart_type_1 import DifficultyChartType1
        from ..models.play_info_alt import PlayInfoAlt
        from ..models.tag import Tag

        d = dict(src_dict)
        auth_user_has_reviewed = d.pop("authUserHasReviewed", UNSET)

        reviews_count = d.pop("reviews_count", UNSET)

        _play_info = d.pop("play_info", UNSET)
        play_info: PlayInfoAlt | Unset
        if isinstance(_play_info, Unset):
            play_info = UNSET
        else:
            play_info = PlayInfoAlt.from_dict(_play_info)

        def _parse_docker_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        docker_status = _parse_docker_status(d.pop("docker_status", UNSET))

        show_go_vip = d.pop("show_go_vip", UNSET)

        has_changelog = d.pop("has_changelog", UNSET)

        auth_user_solve = d.pop("authUserSolve", UNSET)

        def _parse_auth_user_solve_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_user_solve_time = _parse_auth_user_solve_time(
            d.pop("authUserSolveTime", UNSET)
        )

        can_access_walkthough = d.pop("can_access_walkthough", UNSET)

        category_name = d.pop("category_name", UNSET)

        def _parse_creator2_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        creator2_avatar = _parse_creator2_avatar(d.pop("creator2_avatar", UNSET))

        def _parse_creator2_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        creator2_id = _parse_creator2_id(d.pop("creator2_id", UNSET))

        def _parse_creator2_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        creator2_name = _parse_creator2_name(d.pop("creator2_name", UNSET))

        creator_avatar = d.pop("creator_avatar", UNSET)

        creator_id = d.pop("creator_id", UNSET)

        creator_name = d.pop("creator_name", UNSET)

        description = d.pop("description", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        def _parse_difficulty_chart(
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

        difficulty_chart = _parse_difficulty_chart(d.pop("difficulty_chart", UNSET))

        dislike_by_auth_user = d.pop("dislikeByAuthUser", UNSET)

        dislikes = d.pop("dislikes", UNSET)

        def _parse_docker(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        docker = _parse_docker(d.pop("docker", UNSET))

        def _parse_docker_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        docker_ip = _parse_docker_ip(d.pop("docker_ip", UNSET))

        def _parse_docker_ports(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_int_array_type_0 = cast(list[int], data)

                return componentsschemas_int_array_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        docker_ports = _parse_docker_ports(d.pop("docker_ports", UNSET))

        download = d.pop("download", UNSET)

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_file_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        first_blood_time = d.pop("first_blood_time", UNSET)

        first_blood_user = d.pop("first_blood_user", UNSET)

        first_blood_user_avatar = d.pop("first_blood_user_avatar", UNSET)

        first_blood_user_id = d.pop("first_blood_user_id", UNSET)

        id = d.pop("id", UNSET)

        is_respected = d.pop("isRespected", UNSET)

        def _parse_is_respected_2(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_respected_2 = _parse_is_respected_2(d.pop("isRespected2", UNSET))

        is_todo = d.pop("isTodo", UNSET)

        like_by_auth_user = d.pop("likeByAuthUser", UNSET)

        likes = d.pop("likes", UNSET)

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

        def _parse_points(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        points = _parse_points(d.pop("points", UNSET))

        recommended = d.pop("recommended", UNSET)

        _release_date = d.pop("release_date", UNSET)
        release_date: datetime.datetime | Unset
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = datetime.datetime.fromisoformat(_release_date)

        released = d.pop("released", UNSET)

        retired = d.pop("retired", UNSET)

        def _parse_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sha256 = _parse_sha256(d.pop("sha256", UNSET))

        solves = d.pop("solves", UNSET)

        stars = d.pop("stars", UNSET)

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

        user_can_review = d.pop("user_can_review", UNSET)

        def _parse_user_submitted_difficulty(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_submitted_difficulty = _parse_user_submitted_difficulty(
            d.pop("user_submitted_difficulty", UNSET)
        )

        avatar_url = d.pop("avatar_url", UNSET)

        experience_points = d.pop("experience_points", UNSET)

        challenge = cls(
            auth_user_has_reviewed=auth_user_has_reviewed,
            reviews_count=reviews_count,
            play_info=play_info,
            docker_status=docker_status,
            show_go_vip=show_go_vip,
            has_changelog=has_changelog,
            auth_user_solve=auth_user_solve,
            auth_user_solve_time=auth_user_solve_time,
            can_access_walkthough=can_access_walkthough,
            category_name=category_name,
            creator2_avatar=creator2_avatar,
            creator2_id=creator2_id,
            creator2_name=creator2_name,
            creator_avatar=creator_avatar,
            creator_id=creator_id,
            creator_name=creator_name,
            description=description,
            difficulty=difficulty,
            difficulty_chart=difficulty_chart,
            dislike_by_auth_user=dislike_by_auth_user,
            dislikes=dislikes,
            docker=docker,
            docker_ip=docker_ip,
            docker_ports=docker_ports,
            download=download,
            file_name=file_name,
            file_size=file_size,
            first_blood_time=first_blood_time,
            first_blood_user=first_blood_user,
            first_blood_user_avatar=first_blood_user_avatar,
            first_blood_user_id=first_blood_user_id,
            id=id,
            is_respected=is_respected,
            is_respected_2=is_respected_2,
            is_todo=is_todo,
            like_by_auth_user=like_by_auth_user,
            likes=likes,
            name=name,
            play_methods=play_methods,
            points=points,
            recommended=recommended,
            release_date=release_date,
            released=released,
            retired=retired,
            sha256=sha256,
            solves=solves,
            stars=stars,
            state=state,
            tags=tags,
            user_can_review=user_can_review,
            user_submitted_difficulty=user_submitted_difficulty,
            avatar_url=avatar_url,
            experience_points=experience_points,
        )

        challenge.additional_properties = d
        return challenge

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

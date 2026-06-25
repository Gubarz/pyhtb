from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PesentationDetail")


@_attrs_define
class PesentationDetail:
    """
    Attributes:
        mission (str | Unset):
        what_is_title (str | Unset):
        what_is_description (str | Unset):
        who_is_for_description (str | Unset):
        skills (list[None | str] | None | Unset):
        attitude (list[None | str] | None | Unset):
        what_will_gain_title (str | Unset):
        what_will_gain_points (list[None | str] | None | Unset):
    """

    mission: str | Unset = UNSET
    what_is_title: str | Unset = UNSET
    what_is_description: str | Unset = UNSET
    who_is_for_description: str | Unset = UNSET
    skills: list[None | str] | None | Unset = UNSET
    attitude: list[None | str] | None | Unset = UNSET
    what_will_gain_title: str | Unset = UNSET
    what_will_gain_points: list[None | str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mission = self.mission

        what_is_title = self.what_is_title

        what_is_description = self.what_is_description

        who_is_for_description = self.who_is_for_description

        skills: list[None | str] | None | Unset
        if isinstance(self.skills, Unset):
            skills = UNSET
        elif isinstance(self.skills, list):
            skills = []
            for componentsschemas_string_array_type_0_item_data in self.skills:
                componentsschemas_string_array_type_0_item: None | str
                componentsschemas_string_array_type_0_item = (
                    componentsschemas_string_array_type_0_item_data
                )
                skills.append(componentsschemas_string_array_type_0_item)

        else:
            skills = self.skills

        attitude: list[None | str] | None | Unset
        if isinstance(self.attitude, Unset):
            attitude = UNSET
        elif isinstance(self.attitude, list):
            attitude = []
            for componentsschemas_string_array_type_0_item_data in self.attitude:
                componentsschemas_string_array_type_0_item: None | str
                componentsschemas_string_array_type_0_item = (
                    componentsschemas_string_array_type_0_item_data
                )
                attitude.append(componentsschemas_string_array_type_0_item)

        else:
            attitude = self.attitude

        what_will_gain_title = self.what_will_gain_title

        what_will_gain_points: list[None | str] | None | Unset
        if isinstance(self.what_will_gain_points, Unset):
            what_will_gain_points = UNSET
        elif isinstance(self.what_will_gain_points, list):
            what_will_gain_points = []
            for (
                componentsschemas_string_array_type_0_item_data
            ) in self.what_will_gain_points:
                componentsschemas_string_array_type_0_item: None | str
                componentsschemas_string_array_type_0_item = (
                    componentsschemas_string_array_type_0_item_data
                )
                what_will_gain_points.append(componentsschemas_string_array_type_0_item)

        else:
            what_will_gain_points = self.what_will_gain_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mission is not UNSET:
            field_dict["mission"] = mission
        if what_is_title is not UNSET:
            field_dict["whatIsTitle"] = what_is_title
        if what_is_description is not UNSET:
            field_dict["whatIsDescription"] = what_is_description
        if who_is_for_description is not UNSET:
            field_dict["whoIsForDescription"] = who_is_for_description
        if skills is not UNSET:
            field_dict["skills"] = skills
        if attitude is not UNSET:
            field_dict["attitude"] = attitude
        if what_will_gain_title is not UNSET:
            field_dict["whatWillGainTitle"] = what_will_gain_title
        if what_will_gain_points is not UNSET:
            field_dict["whatWillGainPoints"] = what_will_gain_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mission = d.pop("mission", UNSET)

        what_is_title = d.pop("whatIsTitle", UNSET)

        what_is_description = d.pop("whatIsDescription", UNSET)

        who_is_for_description = d.pop("whoIsForDescription", UNSET)

        def _parse_skills(data: object) -> list[None | str] | None | Unset:
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

        skills = _parse_skills(d.pop("skills", UNSET))

        def _parse_attitude(data: object) -> list[None | str] | None | Unset:
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

        attitude = _parse_attitude(d.pop("attitude", UNSET))

        what_will_gain_title = d.pop("whatWillGainTitle", UNSET)

        def _parse_what_will_gain_points(
            data: object,
        ) -> list[None | str] | None | Unset:
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

        what_will_gain_points = _parse_what_will_gain_points(
            d.pop("whatWillGainPoints", UNSET)
        )

        pesentation_detail = cls(
            mission=mission,
            what_is_title=what_is_title,
            what_is_description=what_is_description,
            who_is_for_description=who_is_for_description,
            skills=skills,
            attitude=attitude,
            what_will_gain_title=what_will_gain_title,
            what_will_gain_points=what_will_gain_points,
        )

        pesentation_detail.additional_properties = d
        return pesentation_detail

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

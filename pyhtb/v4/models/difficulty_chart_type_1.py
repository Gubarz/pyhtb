from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DifficultyChartType1")


@_attrs_define
class DifficultyChartType1:
    """
    Attributes:
        counter_bit_hard (int | Unset):  Example: 7.
        counter_brain_fuck (int | Unset):  Example: 6.
        counter_cake (int | Unset):  Example: 23.
        counter_easy (int | Unset):  Example: 26.
        counter_ex_hard (int | Unset):  Example: 1.
        counter_hard (int | Unset):  Example: 1.
        counter_medium (int | Unset):  Example: 9.
        counter_too_easy (int | Unset):  Example: 17.
        counter_too_hard (int | Unset):  Example: 3.
        counter_very_easy (int | Unset):  Example: 35.
    """

    counter_bit_hard: int | Unset = UNSET
    counter_brain_fuck: int | Unset = UNSET
    counter_cake: int | Unset = UNSET
    counter_easy: int | Unset = UNSET
    counter_ex_hard: int | Unset = UNSET
    counter_hard: int | Unset = UNSET
    counter_medium: int | Unset = UNSET
    counter_too_easy: int | Unset = UNSET
    counter_too_hard: int | Unset = UNSET
    counter_very_easy: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counter_bit_hard = self.counter_bit_hard

        counter_brain_fuck = self.counter_brain_fuck

        counter_cake = self.counter_cake

        counter_easy = self.counter_easy

        counter_ex_hard = self.counter_ex_hard

        counter_hard = self.counter_hard

        counter_medium = self.counter_medium

        counter_too_easy = self.counter_too_easy

        counter_too_hard = self.counter_too_hard

        counter_very_easy = self.counter_very_easy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counter_bit_hard is not UNSET:
            field_dict["counterBitHard"] = counter_bit_hard
        if counter_brain_fuck is not UNSET:
            field_dict["counterBrainFuck"] = counter_brain_fuck
        if counter_cake is not UNSET:
            field_dict["counterCake"] = counter_cake
        if counter_easy is not UNSET:
            field_dict["counterEasy"] = counter_easy
        if counter_ex_hard is not UNSET:
            field_dict["counterExHard"] = counter_ex_hard
        if counter_hard is not UNSET:
            field_dict["counterHard"] = counter_hard
        if counter_medium is not UNSET:
            field_dict["counterMedium"] = counter_medium
        if counter_too_easy is not UNSET:
            field_dict["counterTooEasy"] = counter_too_easy
        if counter_too_hard is not UNSET:
            field_dict["counterTooHard"] = counter_too_hard
        if counter_very_easy is not UNSET:
            field_dict["counterVeryEasy"] = counter_very_easy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        counter_bit_hard = d.pop("counterBitHard", UNSET)

        counter_brain_fuck = d.pop("counterBrainFuck", UNSET)

        counter_cake = d.pop("counterCake", UNSET)

        counter_easy = d.pop("counterEasy", UNSET)

        counter_ex_hard = d.pop("counterExHard", UNSET)

        counter_hard = d.pop("counterHard", UNSET)

        counter_medium = d.pop("counterMedium", UNSET)

        counter_too_easy = d.pop("counterTooEasy", UNSET)

        counter_too_hard = d.pop("counterTooHard", UNSET)

        counter_very_easy = d.pop("counterVeryEasy", UNSET)

        difficulty_chart_type_1 = cls(
            counter_bit_hard=counter_bit_hard,
            counter_brain_fuck=counter_brain_fuck,
            counter_cake=counter_cake,
            counter_easy=counter_easy,
            counter_ex_hard=counter_ex_hard,
            counter_hard=counter_hard,
            counter_medium=counter_medium,
            counter_too_easy=counter_too_easy,
            counter_too_hard=counter_too_hard,
            counter_very_easy=counter_very_easy,
        )

        difficulty_chart_type_1.additional_properties = d
        return difficulty_chart_type_1

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

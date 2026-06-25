from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedbackForChart")


@_attrs_define
class FeedbackForChart:
    """
    Attributes:
        counter_cake (int | Unset):
        counter_very_easy (int | Unset):
        counter_easy (int | Unset):
        counter_too_easy (int | Unset):
        counter_medium (int | Unset):
        counter_bit_hard (int | Unset):
        counter_hard (int | Unset):
        counter_too_hard (int | Unset):
        counter_ex_hard (int | Unset):
        counter_brain_fuck (int | Unset):
    """

    counter_cake: int | Unset = UNSET
    counter_very_easy: int | Unset = UNSET
    counter_easy: int | Unset = UNSET
    counter_too_easy: int | Unset = UNSET
    counter_medium: int | Unset = UNSET
    counter_bit_hard: int | Unset = UNSET
    counter_hard: int | Unset = UNSET
    counter_too_hard: int | Unset = UNSET
    counter_ex_hard: int | Unset = UNSET
    counter_brain_fuck: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counter_cake = self.counter_cake

        counter_very_easy = self.counter_very_easy

        counter_easy = self.counter_easy

        counter_too_easy = self.counter_too_easy

        counter_medium = self.counter_medium

        counter_bit_hard = self.counter_bit_hard

        counter_hard = self.counter_hard

        counter_too_hard = self.counter_too_hard

        counter_ex_hard = self.counter_ex_hard

        counter_brain_fuck = self.counter_brain_fuck

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counter_cake is not UNSET:
            field_dict["counterCake"] = counter_cake
        if counter_very_easy is not UNSET:
            field_dict["counterVeryEasy"] = counter_very_easy
        if counter_easy is not UNSET:
            field_dict["counterEasy"] = counter_easy
        if counter_too_easy is not UNSET:
            field_dict["counterTooEasy"] = counter_too_easy
        if counter_medium is not UNSET:
            field_dict["counterMedium"] = counter_medium
        if counter_bit_hard is not UNSET:
            field_dict["counterBitHard"] = counter_bit_hard
        if counter_hard is not UNSET:
            field_dict["counterHard"] = counter_hard
        if counter_too_hard is not UNSET:
            field_dict["counterTooHard"] = counter_too_hard
        if counter_ex_hard is not UNSET:
            field_dict["counterExHard"] = counter_ex_hard
        if counter_brain_fuck is not UNSET:
            field_dict["counterBrainFuck"] = counter_brain_fuck

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        counter_cake = d.pop("counterCake", UNSET)

        counter_very_easy = d.pop("counterVeryEasy", UNSET)

        counter_easy = d.pop("counterEasy", UNSET)

        counter_too_easy = d.pop("counterTooEasy", UNSET)

        counter_medium = d.pop("counterMedium", UNSET)

        counter_bit_hard = d.pop("counterBitHard", UNSET)

        counter_hard = d.pop("counterHard", UNSET)

        counter_too_hard = d.pop("counterTooHard", UNSET)

        counter_ex_hard = d.pop("counterExHard", UNSET)

        counter_brain_fuck = d.pop("counterBrainFuck", UNSET)

        feedback_for_chart = cls(
            counter_cake=counter_cake,
            counter_very_easy=counter_very_easy,
            counter_easy=counter_easy,
            counter_too_easy=counter_too_easy,
            counter_medium=counter_medium,
            counter_bit_hard=counter_bit_hard,
            counter_hard=counter_hard,
            counter_too_hard=counter_too_hard,
            counter_ex_hard=counter_ex_hard,
            counter_brain_fuck=counter_brain_fuck,
        )

        feedback_for_chart.additional_properties = d
        return feedback_for_chart

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

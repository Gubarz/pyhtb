from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FAQItem")


@_attrs_define
class FAQItem:
    """Schema definition for Faq Item

    Attributes:
        answer (str | Unset):  Example: Individual Pro Labs subscriptions do not come with a write-up for users. Only
            our Enterprise-level Pro Labs subscriptions provide a write-up to the lab masters for documentation, training,
            and research purposes..
        generic (bool | Unset):  Example: True.
        question (str | Unset):  Example: Do Pro Lab subscriptions provide a write-up?.
    """

    answer: str | Unset = UNSET
    generic: bool | Unset = UNSET
    question: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer = self.answer

        generic = self.generic

        question = self.question

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if answer is not UNSET:
            field_dict["answer"] = answer
        if generic is not UNSET:
            field_dict["generic"] = generic
        if question is not UNSET:
            field_dict["question"] = question

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        answer = d.pop("answer", UNSET)

        generic = d.pop("generic", UNSET)

        question = d.pop("question", UNSET)

        faq_item = cls(
            answer=answer,
            generic=generic,
            question=question,
        )

        faq_item.additional_properties = d
        return faq_item

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

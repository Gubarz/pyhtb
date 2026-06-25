from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatrixInfo")


@_attrs_define
class MatrixInfo:
    """
    Attributes:
        ctf (float | Unset):
        custom (float | Unset):
        cve (float | Unset):
        enum (float | Unset):
        real (float | Unset):
    """

    ctf: float | Unset = UNSET
    custom: float | Unset = UNSET
    cve: float | Unset = UNSET
    enum: float | Unset = UNSET
    real: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ctf = self.ctf

        custom = self.custom

        cve = self.cve

        enum = self.enum

        real = self.real

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ctf is not UNSET:
            field_dict["ctf"] = ctf
        if custom is not UNSET:
            field_dict["custom"] = custom
        if cve is not UNSET:
            field_dict["cve"] = cve
        if enum is not UNSET:
            field_dict["enum"] = enum
        if real is not UNSET:
            field_dict["real"] = real

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ctf = d.pop("ctf", UNSET)

        custom = d.pop("custom", UNSET)

        cve = d.pop("cve", UNSET)

        enum = d.pop("enum", UNSET)

        real = d.pop("real", UNSET)

        matrix_info = cls(
            ctf=ctf,
            custom=custom,
            cve=cve,
            enum=enum,
            real=real,
        )

        matrix_info.additional_properties = d
        return matrix_info

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_rank import NewRank


T = TypeVar("T", bound="RankUpdate")


@_attrs_define
class RankUpdate:
    """
    Attributes:
        changed (bool | Unset):
        new_rank (NewRank | Unset):
    """

    changed: bool | Unset = UNSET
    new_rank: NewRank | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        new_rank: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_rank, Unset):
            new_rank = self.new_rank.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed is not UNSET:
            field_dict["changed"] = changed
        if new_rank is not UNSET:
            field_dict["newRank"] = new_rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_rank import NewRank

        d = dict(src_dict)
        changed = d.pop("changed", UNSET)

        _new_rank = d.pop("newRank", UNSET)
        new_rank: NewRank | Unset
        if isinstance(_new_rank, Unset):
            new_rank = UNSET
        else:
            new_rank = NewRank.from_dict(_new_rank)

        rank_update = cls(
            changed=changed,
            new_rank=new_rank,
        )

        rank_update.additional_properties = d
        return rank_update

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

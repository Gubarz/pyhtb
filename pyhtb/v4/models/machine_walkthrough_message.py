from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machine_walkthrough_message_official import (
        MachineWalkthroughMessageOfficial,
    )
    from ..models.machine_walkthrough_message_writeups_item import (
        MachineWalkthroughMessageWriteupsItem,
    )
    from ..models.machine_walkthrough_video import MachineWalkthroughVideo


T = TypeVar("T", bound="MachineWalkthroughMessage")


@_attrs_define
class MachineWalkthroughMessage:
    """
    Attributes:
        official (MachineWalkthroughMessageOfficial | Unset):
        under_review (None | str | Unset):
        video (MachineWalkthroughVideo | Unset):
        writeups (list[MachineWalkthroughMessageWriteupsItem] | Unset):
    """

    official: MachineWalkthroughMessageOfficial | Unset = UNSET
    under_review: None | str | Unset = UNSET
    video: MachineWalkthroughVideo | Unset = UNSET
    writeups: list[MachineWalkthroughMessageWriteupsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        official: dict[str, Any] | Unset = UNSET
        if not isinstance(self.official, Unset):
            official = self.official.to_dict()

        under_review: None | str | Unset
        if isinstance(self.under_review, Unset):
            under_review = UNSET
        else:
            under_review = self.under_review

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        writeups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.writeups, Unset):
            writeups = []
            for (
                componentsschemas_machine_walkthrough_message_writeups_items_item_data
            ) in self.writeups:
                componentsschemas_machine_walkthrough_message_writeups_items_item = componentsschemas_machine_walkthrough_message_writeups_items_item_data.to_dict()
                writeups.append(
                    componentsschemas_machine_walkthrough_message_writeups_items_item
                )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if official is not UNSET:
            field_dict["official"] = official
        if under_review is not UNSET:
            field_dict["under_review"] = under_review
        if video is not UNSET:
            field_dict["video"] = video
        if writeups is not UNSET:
            field_dict["writeups"] = writeups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.machine_walkthrough_message_official import (
            MachineWalkthroughMessageOfficial,
        )
        from ..models.machine_walkthrough_message_writeups_item import (
            MachineWalkthroughMessageWriteupsItem,
        )
        from ..models.machine_walkthrough_video import MachineWalkthroughVideo

        d = dict(src_dict)
        _official = d.pop("official", UNSET)
        official: MachineWalkthroughMessageOfficial | Unset
        if isinstance(_official, Unset):
            official = UNSET
        else:
            official = MachineWalkthroughMessageOfficial.from_dict(_official)

        def _parse_under_review(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        under_review = _parse_under_review(d.pop("under_review", UNSET))

        _video = d.pop("video", UNSET)
        video: MachineWalkthroughVideo | Unset
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = MachineWalkthroughVideo.from_dict(_video)

        _writeups = d.pop("writeups", UNSET)
        writeups: list[MachineWalkthroughMessageWriteupsItem] | Unset = UNSET
        if _writeups is not UNSET:
            writeups = []
            for (
                componentsschemas_machine_walkthrough_message_writeups_items_item_data
            ) in _writeups:
                componentsschemas_machine_walkthrough_message_writeups_items_item = MachineWalkthroughMessageWriteupsItem.from_dict(
                    componentsschemas_machine_walkthrough_message_writeups_items_item_data
                )

                writeups.append(
                    componentsschemas_machine_walkthrough_message_writeups_items_item
                )

        machine_walkthrough_message = cls(
            official=official,
            under_review=under_review,
            video=video,
            writeups=writeups,
        )

        machine_walkthrough_message.additional_properties = d
        return machine_walkthrough_message

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

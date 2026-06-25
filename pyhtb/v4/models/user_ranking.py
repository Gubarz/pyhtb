from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserRanking")


@_attrs_define
class UserRanking:
    """
    Attributes:
        challenges (int | Unset):
        created_at (datetime.datetime | Unset):
        endgame (int | Unset):
        fc (int | Unset):
        fortress (int | Unset):
        fr (int | Unset):
        fu (int | Unset):
        id (int | Unset):
        ownership (str | Unset):
        points (int | Unset):
        pro (int | Unset):
        rank (int | Unset):
        respect (int | Unset):
        roots (int | Unset):
        sr (int | Unset):
        su (int | Unset):
        tr (int | Unset):
        tu (int | Unset):
        updated_at (datetime.datetime | Unset):
        user_id (int | Unset):
        users (int | Unset):
    """

    challenges: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    endgame: int | Unset = UNSET
    fc: int | Unset = UNSET
    fortress: int | Unset = UNSET
    fr: int | Unset = UNSET
    fu: int | Unset = UNSET
    id: int | Unset = UNSET
    ownership: str | Unset = UNSET
    points: int | Unset = UNSET
    pro: int | Unset = UNSET
    rank: int | Unset = UNSET
    respect: int | Unset = UNSET
    roots: int | Unset = UNSET
    sr: int | Unset = UNSET
    su: int | Unset = UNSET
    tr: int | Unset = UNSET
    tu: int | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    user_id: int | Unset = UNSET
    users: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenges = self.challenges

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        endgame = self.endgame

        fc = self.fc

        fortress = self.fortress

        fr = self.fr

        fu = self.fu

        id = self.id

        ownership = self.ownership

        points = self.points

        pro = self.pro

        rank = self.rank

        respect = self.respect

        roots = self.roots

        sr = self.sr

        su = self.su

        tr = self.tr

        tu = self.tu

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenges is not UNSET:
            field_dict["challenges"] = challenges
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if endgame is not UNSET:
            field_dict["endgame"] = endgame
        if fc is not UNSET:
            field_dict["fc"] = fc
        if fortress is not UNSET:
            field_dict["fortress"] = fortress
        if fr is not UNSET:
            field_dict["fr"] = fr
        if fu is not UNSET:
            field_dict["fu"] = fu
        if id is not UNSET:
            field_dict["id"] = id
        if ownership is not UNSET:
            field_dict["ownership"] = ownership
        if points is not UNSET:
            field_dict["points"] = points
        if pro is not UNSET:
            field_dict["pro"] = pro
        if rank is not UNSET:
            field_dict["rank"] = rank
        if respect is not UNSET:
            field_dict["respect"] = respect
        if roots is not UNSET:
            field_dict["roots"] = roots
        if sr is not UNSET:
            field_dict["sr"] = sr
        if su is not UNSET:
            field_dict["su"] = su
        if tr is not UNSET:
            field_dict["tr"] = tr
        if tu is not UNSET:
            field_dict["tu"] = tu
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenges = d.pop("challenges", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        endgame = d.pop("endgame", UNSET)

        fc = d.pop("fc", UNSET)

        fortress = d.pop("fortress", UNSET)

        fr = d.pop("fr", UNSET)

        fu = d.pop("fu", UNSET)

        id = d.pop("id", UNSET)

        ownership = d.pop("ownership", UNSET)

        points = d.pop("points", UNSET)

        pro = d.pop("pro", UNSET)

        rank = d.pop("rank", UNSET)

        respect = d.pop("respect", UNSET)

        roots = d.pop("roots", UNSET)

        sr = d.pop("sr", UNSET)

        su = d.pop("su", UNSET)

        tr = d.pop("tr", UNSET)

        tu = d.pop("tu", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        user_id = d.pop("user_id", UNSET)

        users = d.pop("users", UNSET)

        user_ranking = cls(
            challenges=challenges,
            created_at=created_at,
            endgame=endgame,
            fc=fc,
            fortress=fortress,
            fr=fr,
            fu=fu,
            id=id,
            ownership=ownership,
            points=points,
            pro=pro,
            rank=rank,
            respect=respect,
            roots=roots,
            sr=sr,
            su=su,
            tr=tr,
            tu=tu,
            updated_at=updated_at,
            user_id=user_id,
            users=users,
        )

        user_ranking.additional_properties = d
        return user_ranking

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_data_machine_type_0 import ConnectionDataMachineType0


T = TypeVar("T", bound="UserInfo")


@_attrs_define
class UserInfo:
    """Schema definition for User Info

    Attributes:
        avatar (str | Unset):  Example: string.
        beta_tester (int | Unset):
        can_access_dedilab (bool | Unset):
        can_access_vip (bool | Unset):  Example: True.
        can_delete_avatar (bool | Unset):
        currency (str | Unset):  Example: USD.
        dunning_exists (bool | Unset):
        email (str | Unset):  Example: string.
        has_app_tokens (bool | Unset):  Example: True.
        has_reviewed_platform (bool | Unset):
        has_team_invitation (bool | Unset):
        id (int | Unset):
        identifier (str | Unset):  Example: string.
        is_bg_moderator (bool | Unset):
        is_chat_banned (bool | Unset):
        is_dedicated_vip (bool | Unset):  Example: True.
        is_moderator (bool | Unset):
        is_server_vip (bool | Unset):
        is_vip (bool | Unset):
        is_sso_connected (bool | Unset):  Example: True.
        name (str | Unset):  Example: string.
        onboarding_tutorial_complete (int | Unset):  Example: 1.
        opt_in (int | Unset):
        rank_id (int | Unset):  Example: 3.
        server_id (int | Unset):
        subscription_plan (str | Unset):  Example: string.
        team (ConnectionDataMachineType0 | None | Unset):
        timezone (str | Unset):  Example: string.
        university (None | str | Unset):
        verified (bool | Unset):  Example: True.
        subscription_type (str | Unset):
        account_id (str | Unset):
    """

    avatar: str | Unset = UNSET
    beta_tester: int | Unset = UNSET
    can_access_dedilab: bool | Unset = UNSET
    can_access_vip: bool | Unset = UNSET
    can_delete_avatar: bool | Unset = UNSET
    currency: str | Unset = UNSET
    dunning_exists: bool | Unset = UNSET
    email: str | Unset = UNSET
    has_app_tokens: bool | Unset = UNSET
    has_reviewed_platform: bool | Unset = UNSET
    has_team_invitation: bool | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    is_bg_moderator: bool | Unset = UNSET
    is_chat_banned: bool | Unset = UNSET
    is_dedicated_vip: bool | Unset = UNSET
    is_moderator: bool | Unset = UNSET
    is_server_vip: bool | Unset = UNSET
    is_vip: bool | Unset = UNSET
    is_sso_connected: bool | Unset = UNSET
    name: str | Unset = UNSET
    onboarding_tutorial_complete: int | Unset = UNSET
    opt_in: int | Unset = UNSET
    rank_id: int | Unset = UNSET
    server_id: int | Unset = UNSET
    subscription_plan: str | Unset = UNSET
    team: ConnectionDataMachineType0 | None | Unset = UNSET
    timezone: str | Unset = UNSET
    university: None | str | Unset = UNSET
    verified: bool | Unset = UNSET
    subscription_type: str | Unset = UNSET
    account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_data_machine_type_0 import ConnectionDataMachineType0

        avatar = self.avatar

        beta_tester = self.beta_tester

        can_access_dedilab = self.can_access_dedilab

        can_access_vip = self.can_access_vip

        can_delete_avatar = self.can_delete_avatar

        currency = self.currency

        dunning_exists = self.dunning_exists

        email = self.email

        has_app_tokens = self.has_app_tokens

        has_reviewed_platform = self.has_reviewed_platform

        has_team_invitation = self.has_team_invitation

        id = self.id

        identifier = self.identifier

        is_bg_moderator = self.is_bg_moderator

        is_chat_banned = self.is_chat_banned

        is_dedicated_vip = self.is_dedicated_vip

        is_moderator = self.is_moderator

        is_server_vip = self.is_server_vip

        is_vip = self.is_vip

        is_sso_connected = self.is_sso_connected

        name = self.name

        onboarding_tutorial_complete = self.onboarding_tutorial_complete

        opt_in = self.opt_in

        rank_id = self.rank_id

        server_id = self.server_id

        subscription_plan = self.subscription_plan

        team: dict[str, Any] | None | Unset
        if isinstance(self.team, Unset):
            team = UNSET
        elif isinstance(self.team, ConnectionDataMachineType0):
            team = self.team.to_dict()
        else:
            team = self.team

        timezone = self.timezone

        university: None | str | Unset
        if isinstance(self.university, Unset):
            university = UNSET
        else:
            university = self.university

        verified = self.verified

        subscription_type = self.subscription_type

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if beta_tester is not UNSET:
            field_dict["beta_tester"] = beta_tester
        if can_access_dedilab is not UNSET:
            field_dict["canAccessDedilab"] = can_access_dedilab
        if can_access_vip is not UNSET:
            field_dict["canAccessVIP"] = can_access_vip
        if can_delete_avatar is not UNSET:
            field_dict["can_delete_avatar"] = can_delete_avatar
        if currency is not UNSET:
            field_dict["currency"] = currency
        if dunning_exists is not UNSET:
            field_dict["dunning_exists"] = dunning_exists
        if email is not UNSET:
            field_dict["email"] = email
        if has_app_tokens is not UNSET:
            field_dict["hasAppTokens"] = has_app_tokens
        if has_reviewed_platform is not UNSET:
            field_dict["hasReviewedPlatform"] = has_reviewed_platform
        if has_team_invitation is not UNSET:
            field_dict["hasTeamInvitation"] = has_team_invitation
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if is_bg_moderator is not UNSET:
            field_dict["isBGModerator"] = is_bg_moderator
        if is_chat_banned is not UNSET:
            field_dict["isChatBanned"] = is_chat_banned
        if is_dedicated_vip is not UNSET:
            field_dict["isDedicatedVip"] = is_dedicated_vip
        if is_moderator is not UNSET:
            field_dict["isModerator"] = is_moderator
        if is_server_vip is not UNSET:
            field_dict["isServerVIP"] = is_server_vip
        if is_vip is not UNSET:
            field_dict["isVip"] = is_vip
        if is_sso_connected is not UNSET:
            field_dict["is_sso_connected"] = is_sso_connected
        if name is not UNSET:
            field_dict["name"] = name
        if onboarding_tutorial_complete is not UNSET:
            field_dict["onboarding_tutorial_complete"] = onboarding_tutorial_complete
        if opt_in is not UNSET:
            field_dict["opt_in"] = opt_in
        if rank_id is not UNSET:
            field_dict["rank_id"] = rank_id
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if subscription_plan is not UNSET:
            field_dict["subscription_plan"] = subscription_plan
        if team is not UNSET:
            field_dict["team"] = team
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if university is not UNSET:
            field_dict["university"] = university
        if verified is not UNSET:
            field_dict["verified"] = verified
        if subscription_type is not UNSET:
            field_dict["subscriptionType"] = subscription_type
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_data_machine_type_0 import ConnectionDataMachineType0

        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        beta_tester = d.pop("beta_tester", UNSET)

        can_access_dedilab = d.pop("canAccessDedilab", UNSET)

        can_access_vip = d.pop("canAccessVIP", UNSET)

        can_delete_avatar = d.pop("can_delete_avatar", UNSET)

        currency = d.pop("currency", UNSET)

        dunning_exists = d.pop("dunning_exists", UNSET)

        email = d.pop("email", UNSET)

        has_app_tokens = d.pop("hasAppTokens", UNSET)

        has_reviewed_platform = d.pop("hasReviewedPlatform", UNSET)

        has_team_invitation = d.pop("hasTeamInvitation", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        is_bg_moderator = d.pop("isBGModerator", UNSET)

        is_chat_banned = d.pop("isChatBanned", UNSET)

        is_dedicated_vip = d.pop("isDedicatedVip", UNSET)

        is_moderator = d.pop("isModerator", UNSET)

        is_server_vip = d.pop("isServerVIP", UNSET)

        is_vip = d.pop("isVip", UNSET)

        is_sso_connected = d.pop("is_sso_connected", UNSET)

        name = d.pop("name", UNSET)

        onboarding_tutorial_complete = d.pop("onboarding_tutorial_complete", UNSET)

        opt_in = d.pop("opt_in", UNSET)

        rank_id = d.pop("rank_id", UNSET)

        server_id = d.pop("server_id", UNSET)

        subscription_plan = d.pop("subscription_plan", UNSET)

        def _parse_team(data: object) -> ConnectionDataMachineType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_connection_data_machine_type_0 = (
                    ConnectionDataMachineType0.from_dict(data)
                )

                return componentsschemas_connection_data_machine_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionDataMachineType0 | None | Unset, data)

        team = _parse_team(d.pop("team", UNSET))

        timezone = d.pop("timezone", UNSET)

        def _parse_university(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        university = _parse_university(d.pop("university", UNSET))

        verified = d.pop("verified", UNSET)

        subscription_type = d.pop("subscriptionType", UNSET)

        account_id = d.pop("account_id", UNSET)

        user_info = cls(
            avatar=avatar,
            beta_tester=beta_tester,
            can_access_dedilab=can_access_dedilab,
            can_access_vip=can_access_vip,
            can_delete_avatar=can_delete_avatar,
            currency=currency,
            dunning_exists=dunning_exists,
            email=email,
            has_app_tokens=has_app_tokens,
            has_reviewed_platform=has_reviewed_platform,
            has_team_invitation=has_team_invitation,
            id=id,
            identifier=identifier,
            is_bg_moderator=is_bg_moderator,
            is_chat_banned=is_chat_banned,
            is_dedicated_vip=is_dedicated_vip,
            is_moderator=is_moderator,
            is_server_vip=is_server_vip,
            is_vip=is_vip,
            is_sso_connected=is_sso_connected,
            name=name,
            onboarding_tutorial_complete=onboarding_tutorial_complete,
            opt_in=opt_in,
            rank_id=rank_id,
            server_id=server_id,
            subscription_plan=subscription_plan,
            team=team,
            timezone=timezone,
            university=university,
            verified=verified,
            subscription_type=subscription_type,
            account_id=account_id,
        )

        user_info.additional_properties = d
        return user_info

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

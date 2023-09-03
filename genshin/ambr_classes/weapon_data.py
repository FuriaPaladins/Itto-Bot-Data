from dataclasses import dataclass
from typing import Optional, Dict, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Affix:
    name: Optional[str] = None
    upgrade: Optional[Dict[str, str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Affix':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        upgrade = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("upgrade"))
        return Affix(name, upgrade)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.upgrade is not None:
            result["upgrade"] = from_union([lambda x: from_dict(from_str, x), from_none], self.upgrade)
        return result


@dataclass
class AddProps:
    fight_prop_base_attack: Optional[float] = None
    fight_prop_critical: Optional[int] = None
    fight_prop_critical_hurt: Optional[int] = None
    fight_prop_charge_efficiency: Optional[int] = None
    fight_prop_element_mastery: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AddProps':
        assert isinstance(obj, dict)
        fight_prop_base_attack = from_union([from_float, from_none], obj.get("FIGHT_PROP_BASE_ATTACK"))
        fight_prop_critical = from_union([from_int, from_none], obj.get("FIGHT_PROP_CRITICAL"))
        fight_prop_critical_hurt = from_union([from_int, from_none], obj.get("FIGHT_PROP_CRITICAL_HURT"))
        fight_prop_charge_efficiency = from_union([from_int, from_none], obj.get("FIGHT_PROP_CHARGE_EFFICIENCY"))
        fight_prop_element_mastery = from_union([from_int, from_none], obj.get("FIGHT_PROP_ELEMENT_MASTERY"))
        return AddProps(fight_prop_base_attack, fight_prop_critical, fight_prop_critical_hurt, fight_prop_charge_efficiency, fight_prop_element_mastery)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.fight_prop_base_attack is not None:
            result["FIGHT_PROP_BASE_ATTACK"] = from_union([to_float, from_none], self.fight_prop_base_attack)
        if self.fight_prop_critical is not None:
            result["FIGHT_PROP_CRITICAL"] = from_union([from_int, from_none], self.fight_prop_critical)
        if self.fight_prop_critical_hurt is not None:
            result["FIGHT_PROP_CRITICAL_HURT"] = from_union([from_int, from_none], self.fight_prop_critical_hurt)
        if self.fight_prop_charge_efficiency is not None:
            result["FIGHT_PROP_CHARGE_EFFICIENCY"] = from_union([from_int, from_none], self.fight_prop_charge_efficiency)
        if self.fight_prop_element_mastery is not None:
            result["FIGHT_PROP_ELEMENT_MASTERY"] = from_union([from_int, from_none], self.fight_prop_element_mastery)
        return result


@dataclass
class Promote:
    unlock_max_level: Optional[int] = None
    promote_level: Optional[int] = None
    cost_items: Optional[Dict[str, int]] = None
    add_props: Optional[AddProps] = None
    required_player_level: Optional[int] = None
    coin_cost: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Promote':
        assert isinstance(obj, dict)
        unlock_max_level = from_union([from_int, from_none], obj.get("unlockMaxLevel"))
        promote_level = from_union([from_int, from_none], obj.get("promoteLevel"))
        cost_items = from_union([lambda x: from_dict(from_int, x), from_none], obj.get("costItems"))
        add_props = from_union([AddProps.from_dict, from_none], obj.get("addProps"))
        required_player_level = from_union([from_int, from_none], obj.get("requiredPlayerLevel"))
        coin_cost = from_union([from_int, from_none], obj.get("coinCost"))
        return Promote(unlock_max_level, promote_level, cost_items, add_props, required_player_level, coin_cost)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.unlock_max_level is not None:
            result["unlockMaxLevel"] = from_union([from_int, from_none], self.unlock_max_level)
        if self.promote_level is not None:
            result["promoteLevel"] = from_union([from_int, from_none], self.promote_level)
        if self.cost_items is not None:
            result["costItems"] = from_union([lambda x: from_dict(from_int, x), from_none], self.cost_items)
        if self.add_props is not None:
            result["addProps"] = from_union([lambda x: to_class(AddProps, x), from_none], self.add_props)
        if self.required_player_level is not None:
            result["requiredPlayerLevel"] = from_union([from_int, from_none], self.required_player_level)
        if self.coin_cost is not None:
            result["coinCost"] = from_union([from_int, from_none], self.coin_cost)
        return result


@dataclass
class Prop:
    prop_type: Optional[str] = None
    init_value: Optional[float] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Prop':
        assert isinstance(obj, dict)
        prop_type = from_union([from_str, from_none], obj.get("propType"))
        init_value = from_union([from_float, from_none], obj.get("initValue"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Prop(prop_type, init_value, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.prop_type is not None:
            result["propType"] = from_union([from_str, from_none], self.prop_type)
        if self.init_value is not None:
            result["initValue"] = from_union([to_float, from_none], self.init_value)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class Upgrade:
    awaken_cost: Optional[List[int]] = None
    prop: Optional[List[Prop]] = None
    promote: Optional[List[Promote]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Upgrade':
        assert isinstance(obj, dict)
        awaken_cost = from_union([lambda x: from_list(from_int, x), from_none], obj.get("awakenCost"))
        prop = from_union([lambda x: from_list(Prop.from_dict, x), from_none], obj.get("prop"))
        promote = from_union([lambda x: from_list(Promote.from_dict, x), from_none], obj.get("promote"))
        return Upgrade(awaken_cost, prop, promote)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.awaken_cost is not None:
            result["awakenCost"] = from_union([lambda x: from_list(from_int, x), from_none], self.awaken_cost)
        if self.prop is not None:
            result["prop"] = from_union([lambda x: from_list(lambda x: to_class(Prop, x), x), from_none], self.prop)
        if self.promote is not None:
            result["promote"] = from_union([lambda x: from_list(lambda x: to_class(Promote, x), x), from_none], self.promote)
        return result


@dataclass
class Data:
    id: Optional[int] = None
    rank: Optional[int] = None
    type: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    story_id: Optional[int] = None
    affix: Optional[Dict[str, Affix]] = None
    route: Optional[str] = None
    upgrade: Optional[Upgrade] = None
    ascension: Optional[Dict[str, int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        rank = from_union([from_int, from_none], obj.get("rank"))
        type = from_union([from_str, from_none], obj.get("type"))
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        story_id = from_union([from_int, from_none], obj.get("storyId"))
        affix = from_union([from_none, lambda x: from_dict(Affix.from_dict, x)], obj.get("affix"))
        route = from_union([from_str, from_none], obj.get("route"))
        upgrade = from_union([Upgrade.from_dict, from_none], obj.get("upgrade"))
        ascension = from_union([lambda x: from_dict(from_int, x), from_none], obj.get("ascension"))
        return Data(id, rank, type, name, description, icon, story_id, affix, route, upgrade, ascension)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.rank is not None:
            result["rank"] = from_union([from_int, from_none], self.rank)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.icon is not None:
            result["icon"] = from_union([from_str, from_none], self.icon)
        if self.story_id is not None:
            result["storyId"] = from_union([from_int, from_none], self.story_id)
        if self.affix is not None:
            result["affix"] = from_union([from_none, lambda x: from_dict(lambda x: to_class(Affix, x), x)], self.affix)
        if self.route is not None:
            result["route"] = from_union([from_str, from_none], self.route)
        if self.upgrade is not None:
            result["upgrade"] = from_union([lambda x: to_class(Upgrade, x), from_none], self.upgrade)
        if self.ascension is not None:
            result["ascension"] = from_union([lambda x: from_dict(from_int, x), from_none], self.ascension)
        return result


@dataclass
class WeaponData:
    response: Optional[int] = None
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WeaponData':
        assert isinstance(obj, dict)
        response = from_union([from_int, from_none], obj.get("response"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return WeaponData(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.response is not None:
            result["response"] = from_union([from_int, from_none], self.response)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def weapon_data_from_dict(s: Any) -> WeaponData:
    return WeaponData.from_dict(s)


def weapon_data_to_dict(x: WeaponData) -> Any:
    return to_class(WeaponData, x)

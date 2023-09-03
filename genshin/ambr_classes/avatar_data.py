from dataclasses import dataclass
from typing import Optional, Any, List, Dict, Union, TypeVar, Type, cast, Callable
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


@dataclass
class Constellation:
    name: str
    description: str
    icon: str
    id: Optional[int] = None
    type: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Constellation':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        icon = from_str(obj.get("icon"))
        id = from_union([from_int, from_none], obj.get("id"))
        type = from_union([from_int, from_none], obj.get("type"))
        return Constellation(name, description, icon, id, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["icon"] = from_str(self.icon)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.type is not None:
            result["type"] = from_union([from_int, from_none], self.type)
        return result


@dataclass
class Cv:
    en: str
    chs: str
    jp: str
    kr: str

    @staticmethod
    def from_dict(obj: Any) -> 'Cv':
        assert isinstance(obj, dict)
        en = from_str(obj.get("EN"))
        chs = from_str(obj.get("CHS"))
        jp = from_str(obj.get("JP"))
        kr = from_str(obj.get("KR"))
        return Cv(en, chs, jp, kr)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EN"] = from_str(self.en)
        result["CHS"] = from_str(self.chs)
        result["JP"] = from_str(self.jp)
        result["KR"] = from_str(self.kr)
        return result


@dataclass
class Fetter:
    title: str
    detail: str
    constellation: str
    native: str
    cv: Cv

    @staticmethod
    def from_dict(obj: Any) -> 'Fetter':
        assert isinstance(obj, dict)
        title = from_str(obj.get("title"))
        detail = from_str(obj.get("detail"))
        constellation = from_str(obj.get("constellation"))
        native = from_str(obj.get("native"))
        cv = Cv.from_dict(obj.get("cv"))
        return Fetter(title, detail, constellation, native, cv)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_str(self.title)
        result["detail"] = from_str(self.detail)
        result["constellation"] = from_str(self.constellation)
        result["native"] = from_str(self.native)
        result["cv"] = to_class(Cv, self.cv)
        return result


@dataclass
class SpecialFood:
    id: int
    name: str
    rank: int
    effect_icon: str
    icon: str

    @staticmethod
    def from_dict(obj: Any) -> 'SpecialFood':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        rank = from_int(obj.get("rank"))
        effect_icon = from_str(obj.get("effectIcon"))
        icon = from_str(obj.get("icon"))
        return SpecialFood(id, name, rank, effect_icon, icon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["rank"] = from_int(self.rank)
        result["effectIcon"] = from_str(self.effect_icon)
        result["icon"] = from_str(self.icon)
        return result


@dataclass
class Other:
    name_card: Constellation
    special_food: Optional[SpecialFood] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Other':
        assert isinstance(obj, dict)
        name_card = Constellation.from_dict(obj.get("nameCard"))
        special_food = from_union([SpecialFood.from_dict, from_none], obj.get("specialFood"))
        return Other(name_card, special_food)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nameCard"] = to_class(Constellation, self.name_card)
        result["specialFood"] = from_union([lambda x: to_class(SpecialFood, x), from_none], self.special_food)
        return result


@dataclass
class PromoteValue:
    level: int
    description: List[str]
    params: List[float]
    cost_items: Optional[Dict[str, int]] = None
    coin_cost: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PromoteValue':
        assert isinstance(obj, dict)
        level = from_int(obj.get("level"))
        description = from_list(from_str, obj.get("description"))
        params = from_list(from_float, obj.get("params"))
        cost_items = from_union([from_none, lambda x: from_dict(from_int, x)], obj.get("costItems"))
        coin_cost = from_union([from_int, from_none], obj.get("coinCost"))
        return PromoteValue(level, description, params, cost_items, coin_cost)

    def to_dict(self) -> dict:
        result: dict = {}
        result["level"] = from_int(self.level)
        result["description"] = from_list(from_str, self.description)
        result["params"] = from_list(to_float, self.params)
        result["costItems"] = from_union([from_none, lambda x: from_dict(from_int, x)], self.cost_items)
        result["coinCost"] = from_union([from_int, from_none], self.coin_cost)
        return result


@dataclass
class Talent:
    name: str
    description: str
    icon: str
    type: Optional[int] = None
    promote: Optional[Dict[str, PromoteValue]] = None
    cooldown: Optional[float] = None
    cost: Optional[int] = None
    id: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Talent':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        icon = from_str(obj.get("icon"))
        type = from_union([from_int, from_none], obj.get("type"))
        promote = from_union([lambda x: from_dict(PromoteValue.from_dict, x), from_none], obj.get("promote"))
        cooldown = from_union([from_float, from_none], obj.get("cooldown"))
        cost = from_union([from_int, from_none], obj.get("cost"))
        id = from_union([from_int, from_none], obj.get("id"))
        return Talent(name, description, icon, type, promote, cooldown, cost, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["icon"] = from_str(self.icon)
        if self.type is not None:
            result["type"] = from_union([from_int, from_none], self.type)
        if self.promote is not None:
            result["promote"] = from_union([lambda x: from_dict(lambda x: to_class(PromoteValue, x), x), from_none], self.promote)
        if self.cooldown is not None:
            result["cooldown"] = from_union([to_float, from_none], self.cooldown)
        if self.cost is not None:
            result["cost"] = from_union([from_int, from_none], self.cost)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        return result


@dataclass
class AddProps:
    fight_prop_base_hp: float
    fight_prop_base_defense: float
    fight_prop_base_attack: float
    fight_prop_heal_add: Optional[float] = None
    fight_prop_critical_hurt: Optional[float] = None
    fight_prop_elec_add_hurt: Optional[float] = None
    fight_prop_charge_efficiency: Optional[float] = None
    fight_prop_attack_percent: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AddProps':
        assert isinstance(obj, dict)
        fight_prop_base_hp = from_float(obj.get("FIGHT_PROP_BASE_HP"))
        fight_prop_base_defense = from_float(obj.get("FIGHT_PROP_BASE_DEFENSE"))
        fight_prop_base_attack = from_float(obj.get("FIGHT_PROP_BASE_ATTACK"))
        fight_prop_heal_add = from_union([from_float, from_none], obj.get("FIGHT_PROP_HEAL_ADD"))
        fight_prop_critical_hurt = from_union([from_float, from_none], obj.get("FIGHT_PROP_CRITICAL_HURT"))
        fight_prop_elec_add_hurt = from_union([from_float, from_none], obj.get("FIGHT_PROP_ELEC_ADD_HURT"))
        fight_prop_charge_efficiency = from_union([from_float, from_none], obj.get("FIGHT_PROP_CHARGE_EFFICIENCY"))
        fight_prop_attack_percent = from_union([from_float, from_none], obj.get("FIGHT_PROP_ATTACK_PERCENT"))
        return AddProps(fight_prop_base_hp, fight_prop_base_defense, fight_prop_base_attack, fight_prop_heal_add, fight_prop_critical_hurt, fight_prop_elec_add_hurt, fight_prop_charge_efficiency, fight_prop_attack_percent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["FIGHT_PROP_BASE_HP"] = to_float(self.fight_prop_base_hp)
        result["FIGHT_PROP_BASE_DEFENSE"] = to_float(self.fight_prop_base_defense)
        result["FIGHT_PROP_BASE_ATTACK"] = to_float(self.fight_prop_base_attack)
        if self.fight_prop_heal_add is not None:
            result["FIGHT_PROP_HEAL_ADD"] = from_union([to_float, from_none], self.fight_prop_heal_add)
        if self.fight_prop_critical_hurt is not None:
            result["FIGHT_PROP_CRITICAL_HURT"] = from_union([to_float, from_none], self.fight_prop_critical_hurt)
        if self.fight_prop_elec_add_hurt is not None:
            result["FIGHT_PROP_ELEC_ADD_HURT"] = from_union([to_float, from_none], self.fight_prop_elec_add_hurt)
        if self.fight_prop_charge_efficiency is not None:
            result["FIGHT_PROP_CHARGE_EFFICIENCY"] = from_union([to_float, from_none], self.fight_prop_charge_efficiency)
        if self.fight_prop_attack_percent is not None:
            result["FIGHT_PROP_ATTACK_PERCENT"] = from_union([to_float, from_none], self.fight_prop_attack_percent)
        return result


@dataclass
class PromoteElement:
    unlock_max_level: int
    promote_level: int
    cost_items: Optional[Dict[str, int]] = None
    add_props: Optional[AddProps] = None
    required_player_level: Optional[int] = None
    coin_cost: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PromoteElement':
        assert isinstance(obj, dict)
        unlock_max_level = from_int(obj.get("unlockMaxLevel"))
        promote_level = from_int(obj.get("promoteLevel"))
        cost_items = from_union([from_none, lambda x: from_dict(from_int, x)], obj.get("costItems"))
        add_props = from_union([AddProps.from_dict, from_none], obj.get("addProps"))
        required_player_level = from_union([from_int, from_none], obj.get("requiredPlayerLevel"))
        coin_cost = from_union([from_int, from_none], obj.get("coinCost"))
        return PromoteElement(unlock_max_level, promote_level, cost_items, add_props, required_player_level, coin_cost)

    def to_dict(self) -> dict:
        result: dict = {}
        result["unlockMaxLevel"] = from_int(self.unlock_max_level)
        result["promoteLevel"] = from_int(self.promote_level)
        if self.cost_items is not None:
            result["costItems"] = from_union([from_none, lambda x: from_dict(from_int, x)], self.cost_items)
        if self.add_props is not None:
            result["addProps"] = from_union([lambda x: to_class(AddProps, x), from_none], self.add_props)
        if self.required_player_level is not None:
            result["requiredPlayerLevel"] = from_union([from_int, from_none], self.required_player_level)
        if self.coin_cost is not None:
            result["coinCost"] = from_union([from_int, from_none], self.coin_cost)
        return result


class PropType(Enum):
    FIGHT_PROP_BASE_ATTACK = "FIGHT_PROP_BASE_ATTACK"
    FIGHT_PROP_BASE_DEFENSE = "FIGHT_PROP_BASE_DEFENSE"
    FIGHT_PROP_BASE_HP = "FIGHT_PROP_BASE_HP"


@dataclass
class Prop:
    prop_type: PropType
    init_value: float
    type: str

    @staticmethod
    def from_dict(obj: Any) -> 'Prop':
        assert isinstance(obj, dict)
        prop_type = PropType(obj.get("propType"))
        init_value = from_float(obj.get("initValue"))
        type = from_str(obj.get("type"))
        return Prop(prop_type, init_value, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["propType"] = to_enum(PropType, self.prop_type)
        result["initValue"] = to_float(self.init_value)
        result["type"] = from_str(self.type)
        return result


@dataclass
class Upgrade:
    prop: List[Prop]
    promote: List[PromoteElement]

    @staticmethod
    def from_dict(obj: Any) -> 'Upgrade':
        assert isinstance(obj, dict)
        prop = from_list(Prop.from_dict, obj.get("prop"))
        promote = from_list(PromoteElement.from_dict, obj.get("promote"))
        return Upgrade(prop, promote)

    def to_dict(self) -> dict:
        result: dict = {}
        result["prop"] = from_list(lambda x: to_class(Prop, x), self.prop)
        result["promote"] = from_list(lambda x: to_class(PromoteElement, x), self.promote)
        return result


@dataclass
class Data:
    id: Union[int, str]
    rank: int
    name: str
    element: str
    weapon_type: str
    icon: str
    birthday: List[int]
    release: int
    route: str
    fetter: Fetter
    upgrade: Upgrade
    ascension: Dict[str, int]
    talent: Dict[str, Talent]
    constellation: Dict[str, Constellation]
    other: Optional[Other] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_str], obj.get("id"))
        rank = from_int(obj.get("rank"))
        name = from_str(obj.get("name"))
        element = from_str(obj.get("element"))
        weapon_type = from_str(obj.get("weaponType"))
        icon = from_str(obj.get("icon"))
        birthday = from_list(from_int, obj.get("birthday"))
        release = from_int(obj.get("release"))
        route = from_str(obj.get("route"))
        fetter = Fetter.from_dict(obj.get("fetter"))
        upgrade = Upgrade.from_dict(obj.get("upgrade"))
        ascension = from_dict(from_int, obj.get("ascension"))
        talent = from_dict(Talent.from_dict, obj.get("talent"))
        constellation = from_dict(Constellation.from_dict, obj.get("constellation"))
        other = from_union([Other.from_dict, from_none], obj.get("other"))
        return Data(id, rank, name, element, weapon_type, icon, birthday, release, route, fetter, upgrade, ascension, talent, constellation, other)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_str], self.id)
        result["rank"] = from_int(self.rank)
        result["name"] = from_str(self.name)
        result["element"] = from_str(self.element)
        result["weaponType"] = from_str(self.weapon_type)
        result["icon"] = from_str(self.icon)
        result["birthday"] = from_list(from_int, self.birthday)
        result["release"] = from_int(self.release)
        result["route"] = from_str(self.route)
        result["fetter"] = to_class(Fetter, self.fetter)
        result["upgrade"] = to_class(Upgrade, self.upgrade)
        result["ascension"] = from_dict(from_int, self.ascension)
        result["talent"] = from_dict(lambda x: to_class(Talent, x), self.talent)
        result["constellation"] = from_dict(lambda x: to_class(Constellation, x), self.constellation)
        result["other"] = from_union([lambda x: to_class(Other, x), from_none], self.other)
        return result


@dataclass
class AvatarData:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'AvatarData':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return AvatarData(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def avatar_data_from_dict(s: Any) -> AvatarData:
    return AvatarData.from_dict(s)


def avatar_data_to_dict(x: AvatarData) -> Any:
    return to_class(AvatarData, x)

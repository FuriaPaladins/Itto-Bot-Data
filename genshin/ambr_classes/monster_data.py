from dataclasses import dataclass
from typing import Optional, List, Any, Dict, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Affix:
    name: Optional[str] = None
    description: Optional[str] = None
    ability_name: Optional[List[str]] = None
    is_common: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Affix':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        ability_name = from_union([lambda x: from_list(from_str, x), from_none], obj.get("abilityName"))
        is_common = from_union([from_bool, from_none], obj.get("isCommon"))
        return Affix(name, description, ability_name, is_common)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.ability_name is not None:
            result["abilityName"] = from_union([lambda x: from_list(from_str, x), from_none], self.ability_name)
        if self.is_common is not None:
            result["isCommon"] = from_union([from_bool, from_none], self.is_common)
        return result


@dataclass
class HPDrop:
    id: Optional[int] = None
    hp_percent: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HPDrop':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        hp_percent = from_union([from_int, from_none], obj.get("hpPercent"))
        return HPDrop(id, hp_percent)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.hp_percent is not None:
            result["hpPercent"] = from_union([from_int, from_none], self.hp_percent)
        return result


class PropType(Enum):
    FIGHT_PROP_BASE_ATTACK = "FIGHT_PROP_BASE_ATTACK"
    FIGHT_PROP_BASE_DEFENSE = "FIGHT_PROP_BASE_DEFENSE"
    FIGHT_PROP_BASE_HP = "FIGHT_PROP_BASE_HP"


class PropTypeEnum(Enum):
    GROW_CURVE_ATTACK = "GROW_CURVE_ATTACK"
    GROW_CURVE_ATTACK_2 = "GROW_CURVE_ATTACK_2"
    GROW_CURVE_DEFENSE = "GROW_CURVE_DEFENSE"
    GROW_CURVE_HP = "GROW_CURVE_HP"
    GROW_CURVE_HP_2 = "GROW_CURVE_HP_2"
    GROW_CURVE_HP_LITTLEMONSTER = "GROW_CURVE_HP_LITTLEMONSTER"


@dataclass
class Prop:
    prop_type: Optional[PropType] = None
    init_value: Optional[float] = None
    type: Optional[PropTypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Prop':
        assert isinstance(obj, dict)
        prop_type = from_union([PropType, from_none], obj.get("propType"))
        init_value = from_union([from_float, from_none], obj.get("initValue"))
        type = from_union([PropTypeEnum, from_none], obj.get("type"))
        return Prop(prop_type, init_value, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.prop_type is not None:
            result["propType"] = from_union([lambda x: to_enum(PropType, x), from_none], self.prop_type)
        if self.init_value is not None:
            result["initValue"] = from_union([to_float, from_none], self.init_value)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(PropTypeEnum, x), from_none], self.type)
        return result


@dataclass
class Resistance:
    fire_sub_hurt: Optional[float] = None
    grass_sub_hurt: Optional[float] = None
    water_sub_hurt: Optional[float] = None
    elec_sub_hurt: Optional[float] = None
    wind_sub_hurt: Optional[float] = None
    ice_sub_hurt: Optional[float] = None
    rock_sub_hurt: Optional[float] = None
    physical_sub_hurt: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Resistance':
        assert isinstance(obj, dict)
        fire_sub_hurt = from_union([from_float, from_none], obj.get("fireSubHurt"))
        grass_sub_hurt = from_union([from_float, from_none], obj.get("grassSubHurt"))
        water_sub_hurt = from_union([from_float, from_none], obj.get("waterSubHurt"))
        elec_sub_hurt = from_union([from_float, from_none], obj.get("elecSubHurt"))
        wind_sub_hurt = from_union([from_float, from_none], obj.get("windSubHurt"))
        ice_sub_hurt = from_union([from_float, from_none], obj.get("iceSubHurt"))
        rock_sub_hurt = from_union([from_float, from_none], obj.get("rockSubHurt"))
        physical_sub_hurt = from_union([from_float, from_none], obj.get("physicalSubHurt"))
        return Resistance(fire_sub_hurt, grass_sub_hurt, water_sub_hurt, elec_sub_hurt, wind_sub_hurt, ice_sub_hurt, rock_sub_hurt, physical_sub_hurt)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.fire_sub_hurt is not None:
            result["fireSubHurt"] = from_union([to_float, from_none], self.fire_sub_hurt)
        if self.grass_sub_hurt is not None:
            result["grassSubHurt"] = from_union([to_float, from_none], self.grass_sub_hurt)
        if self.water_sub_hurt is not None:
            result["waterSubHurt"] = from_union([to_float, from_none], self.water_sub_hurt)
        if self.elec_sub_hurt is not None:
            result["elecSubHurt"] = from_union([to_float, from_none], self.elec_sub_hurt)
        if self.wind_sub_hurt is not None:
            result["windSubHurt"] = from_union([to_float, from_none], self.wind_sub_hurt)
        if self.ice_sub_hurt is not None:
            result["iceSubHurt"] = from_union([to_float, from_none], self.ice_sub_hurt)
        if self.rock_sub_hurt is not None:
            result["rockSubHurt"] = from_union([to_float, from_none], self.rock_sub_hurt)
        if self.physical_sub_hurt is not None:
            result["physicalSubHurt"] = from_union([to_float, from_none], self.physical_sub_hurt)
        return result


@dataclass
class Reward:
    rank: Optional[int] = None
    icon: Optional[str] = None
    count: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Reward':
        assert isinstance(obj, dict)
        rank = from_union([from_int, from_none], obj.get("rank"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        count = from_union([from_str, from_none], obj.get("count"))
        return Reward(rank, icon, count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.rank is not None:
            result["rank"] = from_union([from_int, from_none], self.rank)
        if self.icon is not None:
            result["icon"] = from_union([from_str, from_none], self.icon)
        if self.count is not None:
            result["count"] = from_union([from_str, from_none], self.count)
        return result


class EntryType(Enum):
    MONSTER_BOSS = "MONSTER_BOSS"
    MONSTER_ENV_ANIMAL = "MONSTER_ENV_ANIMAL"
    MONSTER_FISH = "MONSTER_FISH"
    MONSTER_ORDINARY = "MONSTER_ORDINARY"


@dataclass
class Entry:
    id: Optional[int] = None
    type: Optional[EntryType] = None
    affix: Optional[List[Affix]] = None
    hp_drops: Optional[List[HPDrop]] = None
    prop: Optional[List[Prop]] = None
    resistance: Optional[Resistance] = None
    reward: Optional[Dict[str, Reward]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Entry':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        type = from_union([EntryType, from_none], obj.get("type"))
        affix = from_union([from_none, lambda x: from_list(Affix.from_dict, x)], obj.get("affix"))
        hp_drops = from_union([lambda x: from_list(HPDrop.from_dict, x), from_none], obj.get("hpDrops"))
        prop = from_union([lambda x: from_list(Prop.from_dict, x), from_none], obj.get("prop"))
        resistance = from_union([Resistance.from_dict, from_none], obj.get("resistance"))
        reward = from_union([lambda x: from_dict(Reward.from_dict, x), from_none], obj.get("reward"))
        return Entry(id, type, affix, hp_drops, prop, resistance, reward)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(EntryType, x), from_none], self.type)
        if self.affix is not None:
            result["affix"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Affix, x), x)], self.affix)
        if self.hp_drops is not None:
            result["hpDrops"] = from_union([lambda x: from_list(lambda x: to_class(HPDrop, x), x), from_none], self.hp_drops)
        if self.prop is not None:
            result["prop"] = from_union([lambda x: from_list(lambda x: to_class(Prop, x), x), from_none], self.prop)
        if self.resistance is not None:
            result["resistance"] = from_union([lambda x: to_class(Resistance, x), from_none], self.resistance)
        if self.reward is not None:
            result["reward"] = from_union([lambda x: from_dict(lambda x: to_class(Reward, x), x), from_none], self.reward)
        return result


@dataclass
class Tip:
    images: Optional[List[str]] = None
    description: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tip':
        assert isinstance(obj, dict)
        images = from_union([lambda x: from_list(from_str, x), from_none], obj.get("images"))
        description = from_union([from_str, from_none], obj.get("description"))
        return Tip(images, description)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.images is not None:
            result["images"] = from_union([lambda x: from_list(from_str, x), from_none], self.images)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        return result


@dataclass
class Data:
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    icon: Optional[str] = None
    route: Optional[str] = None
    title: Optional[str] = None
    special_name: Optional[str] = None
    description: Optional[str] = None
    entries: Optional[Dict[str, Entry]] = None
    tips: Optional[Dict[str, Tip]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        route = from_union([from_str, from_none], obj.get("route"))
        title = from_union([from_none, from_str], obj.get("title"))
        special_name = from_union([from_none, from_str], obj.get("specialName"))
        description = from_union([from_str, from_none], obj.get("description"))
        entries = from_union([lambda x: from_dict(Entry.from_dict, x), from_none], obj.get("entries"))
        tips = from_union([from_none, lambda x: from_dict(Tip.from_dict, x)], obj.get("tips"))
        return Data(id, name, type, icon, route, title, special_name, description, entries, tips)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.icon is not None:
            result["icon"] = from_union([from_str, from_none], self.icon)
        if self.route is not None:
            result["route"] = from_union([from_str, from_none], self.route)
        if self.title is not None:
            result["title"] = from_union([from_none, from_str], self.title)
        if self.special_name is not None:
            result["specialName"] = from_union([from_none, from_str], self.special_name)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.entries is not None:
            result["entries"] = from_union([lambda x: from_dict(lambda x: to_class(Entry, x), x), from_none], self.entries)
        if self.tips is not None:
            result["tips"] = from_union([from_none, lambda x: from_dict(lambda x: to_class(Tip, x), x)], self.tips)
        return result


@dataclass
class Monsters:
    response: Optional[int] = None
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Monsters':
        assert isinstance(obj, dict)
        response = from_union([from_int, from_none], obj.get("response"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return Monsters(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.response is not None:
            result["response"] = from_union([from_int, from_none], self.response)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def monsters_from_dict(s: Any) -> Monsters:
    return Monsters.from_dict(s)


def monsters_to_dict(x: Monsters) -> Any:
    return to_class(Monsters, x)

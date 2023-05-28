from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Any, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Element(Enum):
    ELECTRIC = "Electric"
    FIRE = "Fire"
    GRASS = "Grass"
    ICE = "Ice"
    ROCK = "Rock"
    WATER = "Water"
    WIND = "Wind"


class WeaponType(Enum):
    WEAPON_BOW = "WEAPON_BOW"
    WEAPON_CATALYST = "WEAPON_CATALYST"
    WEAPON_CLAYMORE = "WEAPON_CLAYMORE"
    WEAPON_POLE = "WEAPON_POLE"
    WEAPON_SWORD_ONE_HAND = "WEAPON_SWORD_ONE_HAND"


@dataclass
class Item:
    id: str
    rank: int
    name: str
    element: Element
    weapon_type: WeaponType
    icon: str
    birthday: List[int]
    release: str
    route: str
    beta: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_str(str(obj.get("id")))
        rank = from_int(obj.get("rank"))
        name = from_str(obj.get("name"))
        element = Element(obj.get("element"))
        weapon_type = WeaponType(obj.get("weaponType"))
        icon = from_str(obj.get("icon"))
        birthday = from_list(from_int, obj.get("birthday"))
        release = from_str(str(obj.get("release")))
        route = from_str(obj.get("route"))
        beta = from_union([from_bool, from_none], obj.get("beta"))
        return Item(id, rank, name, element, weapon_type, icon, birthday, release, route, beta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["rank"] = from_int(self.rank)
        result["name"] = from_str(self.name)
        result["element"] = to_enum(Element, self.element)
        result["weaponType"] = to_enum(WeaponType, self.weapon_type)
        result["icon"] = from_str(self.icon)
        result["birthday"] = from_list(from_int, self.birthday)
        result["release"] = from_str(self.release)
        result["route"] = from_str(self.route)
        if self.beta is not None:
            result["beta"] = from_union([from_bool, from_none], self.beta)
        return result


@dataclass
class Types:
    weapon_sword_one_hand: str
    weapon_catalyst: str
    weapon_claymore: str
    weapon_bow: str
    weapon_pole: str

    @staticmethod
    def from_dict(obj: Any) -> 'Types':
        assert isinstance(obj, dict)
        weapon_sword_one_hand = from_str(obj.get("WEAPON_SWORD_ONE_HAND"))
        weapon_catalyst = from_str(obj.get("WEAPON_CATALYST"))
        weapon_claymore = from_str(obj.get("WEAPON_CLAYMORE"))
        weapon_bow = from_str(obj.get("WEAPON_BOW"))
        weapon_pole = from_str(obj.get("WEAPON_POLE"))
        return Types(weapon_sword_one_hand, weapon_catalyst, weapon_claymore, weapon_bow, weapon_pole)

    def to_dict(self) -> dict:
        result: dict = {}
        result["WEAPON_SWORD_ONE_HAND"] = from_str(self.weapon_sword_one_hand)
        result["WEAPON_CATALYST"] = from_str(self.weapon_catalyst)
        result["WEAPON_CLAYMORE"] = from_str(self.weapon_claymore)
        result["WEAPON_BOW"] = from_str(self.weapon_bow)
        result["WEAPON_POLE"] = from_str(self.weapon_pole)
        return result


@dataclass
class Data:
    types: Types
    items: Dict[str, Item]

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        types = Types.from_dict(obj.get("types"))
        items = from_dict(Item.from_dict, obj.get("items"))
        return Data(types, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["types"] = to_class(Types, self.types)
        result["items"] = from_dict(lambda x: to_class(Item, x), self.items)
        return result


@dataclass
class AvatarBase:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'AvatarBase':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return AvatarBase(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def avatar_base_from_dict(s: Any) -> AvatarBase:
    return AvatarBase.from_dict(s)


def avatar_base_to_dict(x: AvatarBase) -> Any:
    return to_class(AvatarBase, x)

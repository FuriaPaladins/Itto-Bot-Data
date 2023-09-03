from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, Dict, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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


class TypeEnum(Enum):
    WEAPON_BOW = "WEAPON_BOW"
    WEAPON_CATALYST = "WEAPON_CATALYST"
    WEAPON_CLAYMORE = "WEAPON_CLAYMORE"
    WEAPON_POLE = "WEAPON_POLE"
    WEAPON_SWORD_ONE_HAND = "WEAPON_SWORD_ONE_HAND"


@dataclass
class Item:
    id: int
    rank: int
    type: TypeEnum
    name: str
    icon: str
    route: str
    beta: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        rank = from_int(obj.get("rank"))
        type = TypeEnum(obj.get("type"))
        name = from_str(obj.get("name"))
        icon = from_str(obj.get("icon"))
        route = from_str(obj.get("route"))
        beta = from_union([from_bool, from_none], obj.get("beta"))
        return Item(id, rank, type, name, icon, route, beta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["rank"] = from_int(self.rank)
        result["type"] = to_enum(TypeEnum, self.type)
        result["name"] = from_str(self.name)
        result["icon"] = from_str(self.icon)
        result["route"] = from_str(self.route)
        if self.beta is not None:
            result["beta"] = from_union([from_bool, from_none], self.beta)
        return result


@dataclass
class Types:
    weapon_sword_one_hand: str
    weapon_claymore: str
    weapon_pole: str
    weapon_catalyst: str
    weapon_bow: str

    @staticmethod
    def from_dict(obj: Any) -> 'Types':
        assert isinstance(obj, dict)
        weapon_sword_one_hand = from_str(obj.get("WEAPON_SWORD_ONE_HAND"))
        weapon_claymore = from_str(obj.get("WEAPON_CLAYMORE"))
        weapon_pole = from_str(obj.get("WEAPON_POLE"))
        weapon_catalyst = from_str(obj.get("WEAPON_CATALYST"))
        weapon_bow = from_str(obj.get("WEAPON_BOW"))
        return Types(weapon_sword_one_hand, weapon_claymore, weapon_pole, weapon_catalyst, weapon_bow)

    def to_dict(self) -> dict:
        result: dict = {}
        result["WEAPON_SWORD_ONE_HAND"] = from_str(self.weapon_sword_one_hand)
        result["WEAPON_CLAYMORE"] = from_str(self.weapon_claymore)
        result["WEAPON_POLE"] = from_str(self.weapon_pole)
        result["WEAPON_CATALYST"] = from_str(self.weapon_catalyst)
        result["WEAPON_BOW"] = from_str(self.weapon_bow)
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
class WeaponBase:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'WeaponBase':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return WeaponBase(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def weapon_base_from_dict(s: Any) -> WeaponBase:
    return WeaponBase.from_dict(s)


def weapon_base_to_dict(x: WeaponBase) -> Any:
    return to_class(WeaponBase, x)

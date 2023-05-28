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


class Achievement(Enum):
    ACHIEVEMENT = "achievement"
    BATTLE_PASS = "battlePass"
    BOND = "bond"
    EVENT = "event"
    OTHER = "other"
    REPUTATION = "reputation"


@dataclass
class Item:
    id: int
    name: str
    type: Achievement
    rank: int
    icon: str
    route: str
    beta: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        type = Achievement(obj.get("type"))
        rank = from_int(obj.get("rank"))
        icon = from_str(obj.get("icon"))
        route = from_str(obj.get("route"))
        beta = from_union([from_bool, from_none], obj.get("beta"))
        return Item(id, name, type, rank, icon, route, beta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["type"] = to_enum(Achievement, self.type)
        result["rank"] = from_int(self.rank)
        result["icon"] = from_str(self.icon)
        result["route"] = from_str(self.route)
        if self.beta is not None:
            result["beta"] = from_union([from_bool, from_none], self.beta)
        return result


@dataclass
class Types:
    other: Achievement
    battle_pass: Achievement
    bond: Achievement
    achievement: Achievement
    reputation: Achievement
    event: Achievement

    @staticmethod
    def from_dict(obj: Any) -> 'Types':
        assert isinstance(obj, dict)
        other = Achievement(obj.get("other"))
        battle_pass = Achievement(obj.get("battlePass"))
        bond = Achievement(obj.get("bond"))
        achievement = Achievement(obj.get("achievement"))
        reputation = Achievement(obj.get("reputation"))
        event = Achievement(obj.get("event"))
        return Types(other, battle_pass, bond, achievement, reputation, event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["other"] = to_enum(Achievement, self.other)
        result["battlePass"] = to_enum(Achievement, self.battle_pass)
        result["bond"] = to_enum(Achievement, self.bond)
        result["achievement"] = to_enum(Achievement, self.achievement)
        result["reputation"] = to_enum(Achievement, self.reputation)
        result["event"] = to_enum(Achievement, self.event)
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
class Namecard:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'Namecard':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return Namecard(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def namecard_from_dict(s: Any) -> Namecard:
    return Namecard.from_dict(s)


def namecard_to_dict(x: Namecard) -> Any:
    return to_class(Namecard, x)

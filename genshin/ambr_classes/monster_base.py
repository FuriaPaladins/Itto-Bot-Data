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
    ABYSS = "ABYSS"
    ANIMAL = "ANIMAL"
    AUTOMATRON = "AUTOMATRON"
    AVIARY = "AVIARY"
    BEAST = "BEAST"
    BOSS = "BOSS"
    CRITTER = "CRITTER"
    ELEMENTAL = "ELEMENTAL"
    FATUI = "FATUI"
    FISH = "FISH"
    HILICHURL = "HILICHURL"
    HUMAN = "HUMAN"


@dataclass
class Item:
    id: int
    name: str
    type: TypeEnum
    icon: str
    route: str
    beta: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        type = TypeEnum(obj.get("type"))
        icon = from_str(obj.get("icon"))
        route = from_str(obj.get("route"))
        beta = from_union([from_bool, from_none], obj.get("beta"))
        return Item(id, name, type, icon, route, beta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["type"] = to_enum(TypeEnum, self.type)
        result["icon"] = from_str(self.icon)
        result["route"] = from_str(self.route)
        if self.beta is not None:
            result["beta"] = from_union([from_bool, from_none], self.beta)
        return result


@dataclass
class Types:
    elemental: str
    hilichurl: str
    abyss: str
    fatui: str
    automatron: str
    human: str
    beast: str
    boss: str
    aviary: str
    animal: str
    fish: str
    critter: str

    @staticmethod
    def from_dict(obj: Any) -> 'Types':
        assert isinstance(obj, dict)
        elemental = from_str(obj.get("ELEMENTAL"))
        hilichurl = from_str(obj.get("HILICHURL"))
        abyss = from_str(obj.get("ABYSS"))
        fatui = from_str(obj.get("FATUI"))
        automatron = from_str(obj.get("AUTOMATRON"))
        human = from_str(obj.get("HUMAN"))
        beast = from_str(obj.get("BEAST"))
        boss = from_str(obj.get("BOSS"))
        aviary = from_str(obj.get("AVIARY"))
        animal = from_str(obj.get("ANIMAL"))
        fish = from_str(obj.get("FISH"))
        critter = from_str(obj.get("CRITTER"))
        return Types(elemental, hilichurl, abyss, fatui, automatron, human, beast, boss, aviary, animal, fish, critter)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ELEMENTAL"] = from_str(self.elemental)
        result["HILICHURL"] = from_str(self.hilichurl)
        result["ABYSS"] = from_str(self.abyss)
        result["FATUI"] = from_str(self.fatui)
        result["AUTOMATRON"] = from_str(self.automatron)
        result["HUMAN"] = from_str(self.human)
        result["BEAST"] = from_str(self.beast)
        result["BOSS"] = from_str(self.boss)
        result["AVIARY"] = from_str(self.aviary)
        result["ANIMAL"] = from_str(self.animal)
        result["FISH"] = from_str(self.fish)
        result["CRITTER"] = from_str(self.critter)
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
class MonsterBase:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'MonsterBase':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return MonsterBase(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def monster_base_from_dict(s: Any) -> MonsterBase:
    return MonsterBase.from_dict(s)


def monster_base_to_dict(x: MonsterBase) -> Any:
    return to_class(MonsterBase, x)

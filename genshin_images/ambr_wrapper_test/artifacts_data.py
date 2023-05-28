from dataclasses import dataclass
from typing import Any, Optional, List, Dict, TypeVar, Type, cast, Callable


T = TypeVar("T")


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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


@dataclass
class Equip:
    name: str
    description: str
    max_level: int
    icon: str

    @staticmethod
    def from_dict(obj: Any) -> 'Equip':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        max_level = from_int(obj.get("maxLevel"))
        icon = from_str(obj.get("icon"))
        return Equip(name, description, max_level, icon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["maxLevel"] = from_int(self.max_level)
        result["icon"] = from_str(self.icon)
        return result


@dataclass
class Suit:
    equip_dress: Equip
    equip_bracer: Optional[Equip] = None
    equip_necklace: Optional[Equip] = None
    equip_shoes: Optional[Equip] = None
    equip_ring: Optional[Equip] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Suit':
        assert isinstance(obj, dict)
        equip_dress = Equip.from_dict(obj.get("EQUIP_DRESS"))
        equip_bracer = from_union([Equip.from_dict, from_none], obj.get("EQUIP_BRACER"))
        equip_necklace = from_union([Equip.from_dict, from_none], obj.get("EQUIP_NECKLACE"))
        equip_shoes = from_union([Equip.from_dict, from_none], obj.get("EQUIP_SHOES"))
        equip_ring = from_union([Equip.from_dict, from_none], obj.get("EQUIP_RING"))
        return Suit(equip_dress, equip_bracer, equip_necklace, equip_shoes, equip_ring)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EQUIP_DRESS"] = to_class(Equip, self.equip_dress)
        if self.equip_bracer is not None:
            result["EQUIP_BRACER"] = from_union([lambda x: to_class(Equip, x), from_none], self.equip_bracer)
        if self.equip_necklace is not None:
            result["EQUIP_NECKLACE"] = from_union([lambda x: to_class(Equip, x), from_none], self.equip_necklace)
        if self.equip_shoes is not None:
            result["EQUIP_SHOES"] = from_union([lambda x: to_class(Equip, x), from_none], self.equip_shoes)
        if self.equip_ring is not None:
            result["EQUIP_RING"] = from_union([lambda x: to_class(Equip, x), from_none], self.equip_ring)
        return result


@dataclass
class Data:
    id: int
    name: str
    level_list: List[int]
    affix_list: Dict[str, str]
    icon: str
    route: str
    suit: Suit

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        level_list = from_list(from_int, obj.get("levelList"))
        affix_list = from_dict(from_str, obj.get("affixList"))
        icon = from_str(obj.get("icon"))
        route = from_str(obj.get("route"))
        suit = Suit.from_dict(obj.get("suit"))
        return Data(id, name, level_list, affix_list, icon, route, suit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["levelList"] = from_list(from_int, self.level_list)
        result["affixList"] = from_dict(from_str, self.affix_list)
        result["icon"] = from_str(self.icon)
        result["route"] = from_str(self.route)
        result["suit"] = to_class(Suit, self.suit)
        return result


@dataclass
class ArtifactsData:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'ArtifactsData':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return ArtifactsData(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def artifacts_data_from_dict(s: Any) -> ArtifactsData:
    return ArtifactsData.from_dict(s)


def artifacts_data_to_dict(x: ArtifactsData) -> Any:
    return to_class(ArtifactsData, x)

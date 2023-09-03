from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Data:
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    rank: Optional[int] = None
    icon: Optional[str] = None
    route: Optional[str] = None
    description: Optional[str] = None
    description_special: Optional[str] = None
    source: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        rank = from_union([from_int, from_none], obj.get("rank"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        route = from_union([from_str, from_none], obj.get("route"))
        description = from_union([from_str, from_none], obj.get("description"))
        description_special = from_union([from_str, from_none], obj.get("descriptionSpecial"))
        source = from_union([from_none, from_str], obj.get("source"))
        return Data(id, name, type, rank, icon, route, description, description_special, source)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.rank is not None:
            result["rank"] = from_union([from_int, from_none], self.rank)
        if self.icon is not None:
            result["icon"] = from_union([from_str, from_none], self.icon)
        if self.route is not None:
            result["route"] = from_union([from_str, from_none], self.route)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.description_special is not None:
            result["descriptionSpecial"] = from_union([from_str, from_none], self.description_special)
        if self.source is not None:
            result["source"] = from_union([from_none, from_str], self.source)
        return result


@dataclass
class NamecardIndividual:
    response: Optional[int] = None
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NamecardIndividual':
        assert isinstance(obj, dict)
        response = from_union([from_int, from_none], obj.get("response"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return NamecardIndividual(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.response is not None:
            result["response"] = from_union([from_int, from_none], self.response)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def namecard_individual_from_dict(s: Any) -> NamecardIndividual:
    return NamecardIndividual.from_dict(s)


def namecard_individual_to_dict(x: NamecardIndividual) -> Any:
    return to_class(NamecardIndividual, x)

from dataclasses import dataclass
from typing import Optional, Any, Dict, List, Union, TypeVar, Callable, Type, cast
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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class The70101:
    icon: Optional[str] = None
    count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'The70101':
        assert isinstance(obj, dict)
        icon = from_union([from_str, from_none], obj.get("icon"))
        count = from_union([from_int, from_none], obj.get("count"))
        return The70101(icon, count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.icon is not None:
            result["icon"] = from_union([from_str, from_none], self.icon)
        if self.count is not None:
            result["count"] = from_union([from_int, from_none], self.count)
        return result


@dataclass
class RecipeClass:
    the_70101: Optional[Dict[str, The70101]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RecipeClass':
        assert isinstance(obj, dict)
        the_70101 = from_union([lambda x: from_dict(The70101.from_dict, x), from_none], obj.get("70101"))
        return RecipeClass(the_70101)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.the_70101 is not None:
            result["70101"] = from_union([lambda x: from_dict(lambda x: to_class(The70101, x), x), from_none], self.the_70101)
        return result


class Day(Enum):
    FRIDAY = "friday"
    MONDAY = "monday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    THURSDAY = "thursday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"


class TypeEnum(Enum):
    DOMAIN = "domain"
    SINGLE = "single"


@dataclass
class Source:
    name: Optional[str] = None
    type: Optional[TypeEnum] = None
    days: Optional[List[Day]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Source':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([TypeEnum, from_none], obj.get("type"))
        days = from_union([lambda x: from_list(Day, x), from_none], obj.get("days"))
        return Source(name, type, days)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type)
        if self.days is not None:
            result["days"] = from_union([lambda x: from_list(lambda x: to_enum(Day, x), x), from_none], self.days)
        return result


@dataclass
class Data:
    recipe: Optional[Union[bool, RecipeClass]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    map_mark: Optional[bool] = None
    source: Optional[List[Source]] = None
    icon: Optional[str] = None
    rank: Optional[int] = None
    route: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        recipe = from_union([from_bool, RecipeClass.from_dict, from_none], obj.get("recipe"))
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        type = from_union([from_str, from_none], obj.get("type"))
        map_mark = from_union([from_bool, from_none], obj.get("mapMark"))
        source = from_union([lambda x: from_list(Source.from_dict, x), from_none], obj.get("source"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        rank = from_union([from_int, from_none], obj.get("rank"))
        route = from_union([from_str, from_none], obj.get("route"))
        return Data(recipe, name, description, type, map_mark, source, icon, rank, route)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.recipe is not None:
            result["recipe"] = from_union([from_bool, lambda x: to_class(RecipeClass, x), from_none], self.recipe)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.map_mark is not None:
            result["mapMark"] = from_union([from_bool, from_none], self.map_mark)
        if self.source is not None:
            result["source"] = from_union([lambda x: from_list(lambda x: to_class(Source, x), x), from_none], self.source)
        if self.icon is not None:
            result["icon"] = from_union([from_str, from_none], self.icon)
        if self.rank is not None:
            result["rank"] = from_union([from_int, from_none], self.rank)
        if self.route is not None:
            result["route"] = from_union([from_str, from_none], self.route)
        return result


@dataclass
class Materials:
    response: Optional[int] = None
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Materials':
        assert isinstance(obj, dict)
        response = from_union([from_int, from_none], obj.get("response"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return Materials(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.response is not None:
            result["response"] = from_union([from_int, from_none], self.response)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result

def materials_from_dict(s: Any) -> Materials:
    return Materials.from_dict(s)


def materials_to_dict(x: Materials) -> Any:
    return to_class(Materials, x)

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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


@dataclass
class Input:
    icon: str
    count: int

    @staticmethod
    def from_dict(obj: Any) -> 'Input':
        assert isinstance(obj, dict)
        icon = from_str(obj.get("icon"))
        count = from_int(obj.get("count"))
        return Input(icon, count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["icon"] = from_str(self.icon)
        result["count"] = from_int(self.count)
        return result


@dataclass
class Recipe:
    exp: int
    time: int
    input: Dict[str, Input]

    @staticmethod
    def from_dict(obj: Any) -> 'Recipe':
        assert isinstance(obj, dict)
        exp = from_int(obj.get("exp"))
        time = from_int(obj.get("time"))
        input = from_dict(Input.from_dict, obj.get("input"))
        return Recipe(exp, time, input)

    def to_dict(self) -> dict:
        result: dict = {}
        result["exp"] = from_int(self.exp)
        result["time"] = from_int(self.time)
        result["input"] = from_dict(lambda x: to_class(Input, x), self.input)
        return result


@dataclass
class Tip:
    images: List[str]
    description: str

    @staticmethod
    def from_dict(obj: Any) -> 'Tip':
        assert isinstance(obj, dict)
        images = from_list(from_str, obj.get("images"))
        description = from_str(obj.get("description"))
        return Tip(images, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["images"] = from_list(from_str, self.images)
        result["description"] = from_str(self.description)
        return result


@dataclass
class Data:
    id: int
    name: str
    rank: int
    icon: str
    route: str
    categories: List[str]
    types: List[str]
    description: str
    cost: Optional[int] = None
    comfort: Optional[int] = None
    recipe: Optional[Recipe] = None
    tips: Optional[Dict[str, Tip]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        rank = from_int(obj.get("rank"))
        icon = from_str(obj.get("icon"))
        route = from_str(obj.get("route"))
        categories = from_list(from_str, obj.get("categories"))
        types = from_list(from_str, obj.get("types"))
        description = from_str(obj.get("description"))
        cost = from_union([from_none, from_int], obj.get("cost"))
        comfort = from_union([from_none, from_int], obj.get("comfort"))
        recipe = from_union([Recipe.from_dict, from_none], obj.get("recipe"))
        tips = from_union([from_none, lambda x: from_dict(Tip.from_dict, x)], obj.get("tips"))
        return Data(id, name, rank, icon, route, categories, types, description, cost, comfort, recipe, tips)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["rank"] = from_int(self.rank)
        result["icon"] = from_str(self.icon)
        result["route"] = from_str(self.route)
        result["categories"] = from_list(from_str, self.categories)
        result["types"] = from_list(from_str, self.types)
        result["description"] = from_str(self.description)
        result["cost"] = from_union([from_none, from_int], self.cost)
        result["comfort"] = from_union([from_none, from_int], self.comfort)
        result["recipe"] = from_union([lambda x: to_class(Recipe, x), from_none], self.recipe)
        result["tips"] = from_union([from_none, lambda x: from_dict(lambda x: to_class(Tip, x), x)], self.tips)
        return result


@dataclass
class FurnitureData:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'FurnitureData':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return FurnitureData(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def furniture_data_from_dict(s: Any) -> FurnitureData:
    return FurnitureData.from_dict(s)


def furniture_data_to_dict(x: FurnitureData) -> Any:
    return to_class(FurnitureData, x)

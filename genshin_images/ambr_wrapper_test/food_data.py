from dataclasses import dataclass
from typing import Any, Union, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class Effect:
    the_0: str

    @staticmethod
    def from_dict(obj: Any) -> 'Effect':
        assert isinstance(obj, dict)
        the_0 = from_str(obj.get("0"))
        return Effect(the_0)

    def to_dict(self) -> dict:
        result: dict = {}
        result["0"] = from_str(self.the_0)
        return result


@dataclass
class RecipeClass:
    effect_icon: str
    effect: Effect

    @staticmethod
    def from_dict(obj: Any) -> 'RecipeClass':
        assert isinstance(obj, dict)
        effect_icon = from_str(obj.get("effectIcon"))
        effect = Effect.from_dict(obj.get("effect"))
        return RecipeClass(effect_icon, effect)

    def to_dict(self) -> dict:
        result: dict = {}
        result["effectIcon"] = from_str(self.effect_icon)
        result["effect"] = to_class(Effect, self.effect)
        return result


@dataclass
class Source:
    name: str
    type: str

    @staticmethod
    def from_dict(obj: Any) -> 'Source':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        type = from_str(obj.get("type"))
        return Source(name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["type"] = from_str(self.type)
        return result


@dataclass
class Data:
    name: str
    description: str
    type: str
    recipe: Union[RecipeClass, bool]
    map_mark: bool
    source: List[Source]
    icon: str
    rank: int
    route: str

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        type = from_str(obj.get("type"))
        recipe = from_union([RecipeClass.from_dict, from_bool], obj.get("recipe"))
        map_mark = from_bool(obj.get("mapMark"))
        source = from_list(Source.from_dict, obj.get("source"))
        icon = from_str(obj.get("icon"))
        rank = from_int(obj.get("rank"))
        route = from_str(obj.get("route"))
        return Data(name, description, type, recipe, map_mark, source, icon, rank, route)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["type"] = from_str(self.type)
        result["recipe"] = from_union([lambda x: to_class(RecipeClass, x), from_bool], self.recipe)
        result["mapMark"] = from_bool(self.map_mark)
        result["source"] = from_list(lambda x: to_class(Source, x), self.source)
        result["icon"] = from_str(self.icon)
        result["rank"] = from_int(self.rank)
        result["route"] = from_str(self.route)
        return result


@dataclass
class FoodData:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'FoodData':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return FoodData(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def food_data_from_dict(s: Any) -> FoodData:
    return FoodData.from_dict(s)


def food_data_to_dict(x: FoodData) -> Any:
    return to_class(FoodData, x)

from dataclasses import dataclass
from typing import List, Dict, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Item:
    id: int
    name: str
    level_list: List[int]
    affix_list: Dict[str, str]
    icon: str
    route: str
    sort_order: int

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        level_list = from_list(from_int, obj.get("levelList"))
        affix_list = from_dict(from_str, obj.get("affixList"))
        icon = from_str(obj.get("icon"))
        route = from_str(obj.get("route"))
        sort_order = from_int(obj.get("sortOrder"))
        return Item(id, name, level_list, affix_list, icon, route, sort_order)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["levelList"] = from_list(from_int, self.level_list)
        result["affixList"] = from_dict(from_str, self.affix_list)
        result["icon"] = from_str(self.icon)
        result["route"] = from_str(self.route)
        result["sortOrder"] = from_int(self.sort_order)
        return result


@dataclass
class Data:
    items: Dict[str, Item]

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        items = from_dict(Item.from_dict, obj.get("items"))
        return Data(items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_dict(lambda x: to_class(Item, x), self.items)
        return result


@dataclass
class ArtifactsBase:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'ArtifactsBase':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return ArtifactsBase(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def artifacts_base_from_dict(s: Any) -> ArtifactsBase:
    return ArtifactsBase.from_dict(s)


def artifacts_base_to_dict(x: ArtifactsBase) -> Any:
    return to_class(ArtifactsBase, x)

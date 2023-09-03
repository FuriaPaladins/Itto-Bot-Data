from dataclasses import dataclass
from typing import Any, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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
    rank: int
    icon: str
    route: str

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        rank = from_int(obj.get("rank"))
        icon = from_str(obj.get("icon"))
        route = from_str(obj.get("route"))
        return Item(id, name, rank, icon, route)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["rank"] = from_int(self.rank)
        result["icon"] = from_str(self.icon)
        result["route"] = from_str(self.route)
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
class BookBase:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'BookBase':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return BookBase(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def book_base_from_dict(s: Any) -> BookBase:
    return BookBase.from_dict(s)


def book_base_to_dict(x: BookBase) -> Any:
    return to_class(BookBase, x)

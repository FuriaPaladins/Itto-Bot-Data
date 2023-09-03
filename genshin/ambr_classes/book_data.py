from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Volume:
    id: int
    name: str
    description: str
    story_id: int

    @staticmethod
    def from_dict(obj: Any) -> 'Volume':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        story_id = int(from_str(obj.get("storyId")))
        return Volume(id, name, description, story_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["storyId"] = from_str(str(self.story_id))
        return result


@dataclass
class Data:
    id: int
    name: str
    rank: int
    icon: str
    volume: List[Volume]
    route: str

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        rank = from_int(obj.get("rank"))
        icon = from_str(obj.get("icon"))
        volume = from_list(Volume.from_dict, obj.get("volume"))
        route = from_str(obj.get("route"))
        return Data(id, name, rank, icon, volume, route)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["rank"] = from_int(self.rank)
        result["icon"] = from_str(self.icon)
        result["volume"] = from_list(lambda x: to_class(Volume, x), self.volume)
        result["route"] = from_str(self.route)
        return result


@dataclass
class BookData:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'BookData':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return BookData(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def book_data_from_dict(s: Any) -> BookData:
    return BookData.from_dict(s)


def book_data_to_dict(x: BookData) -> Any:
    return to_class(BookData, x)

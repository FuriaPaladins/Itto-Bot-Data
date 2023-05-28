from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, Dict, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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
    AQ = "aq"
    EQ = "eq"
    IQ = "iq"
    LQ = "lq"
    OQ = "oq"
    WQ = "wq"


@dataclass
class Item:
    id: Optional[int] = None
    type: Optional[TypeEnum] = None
    chapter_num: Optional[str] = None
    chapter_title: Optional[str] = None
    chapter_icon: Optional[str] = None
    chapter_image_title: Optional[str] = None
    route: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        type = from_union([TypeEnum, from_none], obj.get("type"))
        chapter_num = from_union([from_none, from_str], obj.get("chapterNum"))
        chapter_title = from_union([from_str, from_none], obj.get("chapterTitle"))
        chapter_icon = from_union([from_none, from_str], obj.get("chapterIcon"))
        chapter_image_title = from_union([from_none, from_str], obj.get("chapterImageTitle"))
        route = from_union([from_str, from_none], obj.get("route"))
        return Item(id, type, chapter_num, chapter_title, chapter_icon, chapter_image_title, route)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.type is not None:
            result["type"] = from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type)
        if self.chapter_num is not None:
            result["chapterNum"] = from_union([from_none, from_str], self.chapter_num)
        if self.chapter_title is not None:
            result["chapterTitle"] = from_union([from_str, from_none], self.chapter_title)
        if self.chapter_icon is not None:
            result["chapterIcon"] = from_union([from_none, from_str], self.chapter_icon)
        if self.chapter_image_title is not None:
            result["chapterImageTitle"] = from_union([from_none, from_str], self.chapter_image_title)
        if self.route is not None:
            result["route"] = from_union([from_str, from_none], self.route)
        return result


@dataclass
class Data:
    items: Optional[Dict[str, Item]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_dict(Item.from_dict, x), from_none], obj.get("items"))
        return Data(items)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.items is not None:
            result["items"] = from_union([lambda x: from_dict(lambda x: to_class(Item, x), x), from_none], self.items)
        return result


@dataclass
class QuestBase:
    response: Optional[int] = None
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuestBase':
        assert isinstance(obj, dict)
        response = from_union([from_int, from_none], obj.get("response"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return QuestBase(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.response is not None:
            result["response"] = from_union([from_int, from_none], self.response)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def quest_base_from_dict(s: Any) -> QuestBase:
    return QuestBase.from_dict(s)


def quest_base_to_dict(x: QuestBase) -> Any:
    return to_class(QuestBase, x)

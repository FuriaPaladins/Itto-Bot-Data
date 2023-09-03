from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, Union, List, Dict, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


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


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


class InfoType(Enum):
    AQ = "aq"
    IQ = "iq"
    OQ = "oq"
    WQ = "wq"


@dataclass
class DataInfo:
    id: int
    type: InfoType
    chapter_title: str
    route: str
    chapter_num: Optional[str] = None
    chapter_icon: Optional[str] = None
    chapter_image_title: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataInfo':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        type = InfoType(obj.get("type"))
        chapter_title = from_str(obj.get("chapterTitle"))
        route = from_str(obj.get("route"))
        chapter_num = from_union([from_none, from_str], obj.get("chapterNum"))
        chapter_icon = from_union([from_none, from_str], obj.get("chapterIcon"))
        chapter_image_title = from_union([from_none, from_str], obj.get("chapterImageTitle"))
        return DataInfo(id, type, chapter_title, route, chapter_num, chapter_icon, chapter_image_title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["type"] = to_enum(InfoType, self.type)
        result["chapterTitle"] = from_str(self.chapter_title)
        result["route"] = from_str(self.route)
        result["chapterNum"] = from_union([from_none, from_str], self.chapter_num)
        result["chapterIcon"] = from_union([from_none, from_str], self.chapter_icon)
        result["chapterImageTitle"] = from_union([from_none, from_str], self.chapter_image_title)
        return result


@dataclass
class StoryListInfo:
    title: str
    description: str

    @staticmethod
    def from_dict(obj: Any) -> 'StoryListInfo':
        assert isinstance(obj, dict)
        title = from_str(obj.get("title"))
        description = from_str(obj.get("description"))
        return StoryListInfo(title, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_str(self.title)
        result["description"] = from_str(self.description)
        return result


class TypeType(Enum):
    ITEM = "item"


@dataclass
class Reward:
    id: int
    icon: str
    type: Union[int, TypeType]
    rank: int
    count: int

    @staticmethod
    def from_dict(obj: Any) -> 'Reward':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        icon = from_str(obj.get("icon"))
        type = from_union([from_int, TypeType], obj.get("type"))
        rank = from_int(obj.get("rank"))
        count = from_int(obj.get("count"))
        return Reward(id, icon, type, rank, count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["icon"] = from_str(self.icon)
        result["type"] = from_union([from_int, lambda x: to_enum(TypeType, x)], self.type)
        result["rank"] = from_int(self.rank)
        result["count"] = from_int(self.count)
        return result


class Role(Enum):
    AGENT = "Agent"
    AMBER = "Amber"
    ANASTASIA = "Anastasia"
    BAIZHU = "Baizhu"
    BARBARA = "Barbara"
    BOLAI = "Bolai"
    CHANGSHENG = "Changsheng"
    CHANGSHUN = "Changshun"
    CHARLES = "Charles"
    CHILDE = "Childe"
    CLOUD_RETAINER = "Cloud Retainer"
    CONFUSED_BYSTANDER = "Confused Bystander"
    CRICKET_REFEREE = "Cricket Referee"
    CROWD = "Crowd"
    CYRUS = "Cyrus"
    DILUC = "Diluc"
    DR_LIVINGSTONE = "Dr. Livingstone"
    DUSKY_MING = "Dusky Ming"
    EKATERINA = "Ekaterina"
    EMPTY = "???"
    FATUI_GUARD = "Fatui Guard"
    FRECKLE_HUANG = "Freckle Huang"
    GANYU = "Ganyu"
    GOTELINDE = "Gotelinde"
    GRACE = "Grace"
    GRANNY_SHAN = "Granny Shan"
    GREEN_FELLOW = "Green Fellow"
    GUANHAI = "Guanhai"
    IRON_TONGUE_TIAN = "Iron Tongue Tian"
    IVANOVICH = "Ivanovich"
    JEAN = "Jean"
    KAEYA = "Kaeya"
    LAN = "Lan"
    LINLANG = "Linlang"
    LISA = "Lisa"
    LI_DANG = "Li Dang"
    LI_DING = "Li Ding"
    LYNN = "Lynn"
    MADAME_PING = "Madame Ping"
    MILES = "Miles"
    MILLELITH_SERGEANT = "Millelith Sergeant"
    MILLELITH_SOLDIER = "Millelith Soldier"
    MOON_CARVER = "Moon Carver"
    MOUNTAIN_SHAPER = "Mountain Shaper"
    NIMROD = "Nimrod"
    OTTO = "Otto"
    PAIMON = "Paimon"
    QIMING = "Qiming"
    QIQI = "Qiqi"
    SARA = "Sara"
    SHITOU = "Shitou"
    SLIME_BREEDER = "Slime Breeder"
    SMILEY_YANXIAO = "Smiley Yanxiao"
    STATUE_OF_THE_SEVEN = "Statue of The Seven"
    TRAVELER = "Traveler"
    TUNNER = "Tunner"
    VENTI = "Venti"
    VERR_GOLDET = "Verr Goldet"
    WHITE_SNAKE = "White Snake"
    XIAO = "Xiao"
    YING_ER = "Ying'er"
    ZHONGLI = "Zhongli"


class NextEnum(Enum):
    FINISH = "finish"


@dataclass
class Text:
    text: str
    next: Optional[Union[int, NextEnum]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Text':
        assert isinstance(obj, dict)
        text = from_str(obj.get("text"))
        next = from_union([from_none, from_int, NextEnum], obj.get("next"))
        return Text(text, next)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_str(self.text)
        result["next"] = from_union([from_none, from_int, lambda x: to_enum(NextEnum, x)], self.next)
        return result


class ItemType(Enum):
    MULTI_DIALOG = "MultiDialog"
    SINGLE_DIALOG = "SingleDialog"
    TEXT_CENTER = "TextCenter"
    TEXT_LEFT = "TextLeft"


@dataclass
class Item:
    type: ItemType
    text: List[Text]
    role: Optional[Role] = None
    next: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        type = ItemType(obj.get("type"))
        text = from_list(Text.from_dict, obj.get("text"))
        role = from_union([from_none, Role], obj.get("role"))
        next = from_union([from_int, from_none], obj.get("next"))
        return Item(type, text, role, next)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(ItemType, self.type)
        result["text"] = from_list(lambda x: to_class(Text, x), self.text)
        result["role"] = from_union([from_none, lambda x: to_enum(Role, x)], self.role)
        result["next"] = from_union([from_int, from_none], self.next)
        return result


@dataclass
class Story:
    title: str
    order: Optional[int] = None
    items: Optional[Dict[str, Item]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Story':
        assert isinstance(obj, dict)
        title = from_str(obj.get("title"))
        order = from_union([from_int, from_none], obj.get("order"))
        items = from_union([lambda x: from_dict(Item.from_dict, x), from_none], obj.get("items"))
        return Story(title, order, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_str(self.title)
        if self.order is not None:
            result["order"] = from_union([from_int, from_none], self.order)
        result["items"] = from_union([lambda x: from_dict(lambda x: to_class(Item, x), x), from_none], self.items)
        return result


@dataclass
class StoryList:
    id: int
    info: StoryListInfo
    story: Dict[str, Story]
    reward: Optional[Dict[str, Reward]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StoryList':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        info = StoryListInfo.from_dict(obj.get("info"))
        story = from_dict(Story.from_dict, obj.get("story"))
        reward = from_union([from_none, lambda x: from_dict(Reward.from_dict, x)], obj.get("reward"))
        return StoryList(id, info, story, reward)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["info"] = to_class(StoryListInfo, self.info)
        result["story"] = from_dict(lambda x: to_class(Story, x), self.story)
        result["reward"] = from_union([from_none, lambda x: from_dict(lambda x: to_class(Reward, x), x)], self.reward)
        return result


@dataclass
class Data:
    info: DataInfo
    story_list: Dict[str, StoryList]

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        info = DataInfo.from_dict(obj.get("info"))
        story_list = from_dict(StoryList.from_dict, obj.get("storyList"))
        return Data(info, story_list)

    def to_dict(self) -> dict:
        result: dict = {}
        result["info"] = to_class(DataInfo, self.info)
        result["storyList"] = from_dict(lambda x: to_class(StoryList, x), self.story_list)
        return result


@dataclass
class QuestData:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'QuestData':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return QuestData(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def quest_data_from_dict(s: Any) -> QuestData:
    return QuestData.from_dict(s)


def quest_data_to_dict(x: QuestData) -> Any:
    return to_class(QuestData, x)

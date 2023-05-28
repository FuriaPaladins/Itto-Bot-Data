from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Any, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


class Category(Enum):
    ANIMAL = "animal"
    BUILDING = "building"
    COURTYARD = "courtyard"
    DECORATION = "decoration"
    LANDFORM = "landform"
    LANDSCAPE = "landscape"
    LARGE_FURNISHING = "largeFurnishing"
    MAIN_BUILDING = "mainBuilding"
    ORNAMENTS = "ornaments"
    OUTDOOR_FURNISHING = "outdoorFurnishing"
    SMALL_FURNISHING = "smallFurnishing"
    WALL_DECOR = "wallDecor"


@dataclass
class Item:
    id: int
    name: str
    rank: int
    icon: str
    route: str
    categories: List[Category]
    types: List[str]
    cost: Optional[int] = None
    comfort: Optional[int] = None
    beta: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        rank = from_int(obj.get("rank"))
        icon = from_str(obj.get("icon"))
        route = from_str(obj.get("route"))
        categories = from_list(Category, obj.get("categories"))
        types = from_list(from_str, obj.get("types"))
        cost = from_union([from_none, from_int], obj.get("cost"))
        comfort = from_union([from_none, from_int], obj.get("comfort"))
        beta = from_union([from_bool, from_none], obj.get("beta"))
        return Item(id, name, rank, icon, route, categories, types, cost, comfort, beta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["rank"] = from_int(self.rank)
        result["icon"] = from_str(self.icon)
        result["route"] = from_str(self.route)
        result["categories"] = from_list(lambda x: to_enum(Category, x), self.categories)
        result["types"] = from_list(from_str, self.types)
        result["cost"] = from_union([from_none, from_int], self.cost)
        result["comfort"] = from_union([from_none, from_int], self.comfort)
        if self.beta is not None:
            result["beta"] = from_union([from_bool, from_none], self.beta)
        return result


@dataclass
class TypeCategories:
    animal: str
    decoration: str
    landform: str
    large_furnishing: str
    small_furnishing: str
    ornaments: str
    wall_decor: str
    building: str
    courtyard: str
    main_building: str
    outdoor_furnishing: str
    landscape: str

    @staticmethod
    def from_dict(obj: Any) -> 'TypeCategories':
        assert isinstance(obj, dict)
        animal = from_str(obj.get("animal"))
        decoration = from_str(obj.get("decoration"))
        landform = from_str(obj.get("landform"))
        large_furnishing = from_str(obj.get("largeFurnishing"))
        small_furnishing = from_str(obj.get("smallFurnishing"))
        ornaments = from_str(obj.get("ornaments"))
        wall_decor = from_str(obj.get("wallDecor"))
        building = from_str(obj.get("building"))
        courtyard = from_str(obj.get("courtyard"))
        main_building = from_str(obj.get("mainBuilding"))
        outdoor_furnishing = from_str(obj.get("outdoorFurnishing"))
        landscape = from_str(obj.get("landscape"))
        return TypeCategories(animal, decoration, landform, large_furnishing, small_furnishing, ornaments, wall_decor, building, courtyard, main_building, outdoor_furnishing, landscape)

    def to_dict(self) -> dict:
        result: dict = {}
        result["animal"] = from_str(self.animal)
        result["decoration"] = from_str(self.decoration)
        result["landform"] = from_str(self.landform)
        result["largeFurnishing"] = from_str(self.large_furnishing)
        result["smallFurnishing"] = from_str(self.small_furnishing)
        result["ornaments"] = from_str(self.ornaments)
        result["wallDecor"] = from_str(self.wall_decor)
        result["building"] = from_str(self.building)
        result["courtyard"] = from_str(self.courtyard)
        result["mainBuilding"] = from_str(self.main_building)
        result["outdoorFurnishing"] = from_str(self.outdoor_furnishing)
        result["landscape"] = from_str(self.landscape)
        return result


@dataclass
class Types:
    type_categories: TypeCategories
    type_list: Dict[str, str]
    type_icons: Dict[str, str]

    @staticmethod
    def from_dict(obj: Any) -> 'Types':
        assert isinstance(obj, dict)
        type_categories = TypeCategories.from_dict(obj.get("typeCategories"))
        type_list = from_dict(from_str, obj.get("typeList"))
        type_icons = from_dict(from_str, obj.get("typeIcons"))
        return Types(type_categories, type_list, type_icons)

    def to_dict(self) -> dict:
        result: dict = {}
        result["typeCategories"] = to_class(TypeCategories, self.type_categories)
        result["typeList"] = from_dict(from_str, self.type_list)
        result["typeIcons"] = from_dict(from_str, self.type_icons)
        return result


@dataclass
class Data:
    types: Types
    items: Dict[str, Item]

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        types = Types.from_dict(obj.get("types"))
        items = from_dict(Item.from_dict, obj.get("items"))
        return Data(types, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["types"] = to_class(Types, self.types)
        result["items"] = from_dict(lambda x: to_class(Item, x), self.items)
        return result


@dataclass
class FurnitureBase:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'FurnitureBase':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return FurnitureBase(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def furniture_base_from_dict(s: Any) -> FurnitureBase:
    return FurnitureBase.from_dict(s)


def furniture_base_to_dict(x: FurnitureBase) -> Any:
    return to_class(FurnitureBase, x)

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, Dict, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class AtkAdd(Enum):
    UI_BUFF_ITEM_ATK_ADD = "UI_Buff_Item_Atk_Add"
    UI_BUFF_ITEM_ATK_CRIT_RATE = "UI_Buff_Item_Atk_CritRate"
    UI_BUFF_ITEM_CLIMATE_HEAT = "UI_Buff_Item_Climate_Heat"
    UI_BUFF_ITEM_DEF_ADD = "UI_Buff_Item_Def_Add"
    UI_BUFF_ITEM_OTHER_SP_ADD = "UI_Buff_Item_Other_SPAdd"
    UI_BUFF_ITEM_OTHER_SP_REDUCE_CONSUME = "UI_Buff_Item_Other_SPReduceConsume"
    UI_BUFF_ITEM_RECOVERY_HP_ADD = "UI_Buff_Item_Recovery_HpAdd"
    UI_BUFF_ITEM_RECOVERY_HP_ADD_ALL = "UI_Buff_Item_Recovery_HpAddAll"
    UI_BUFF_ITEM_RECOVERY_REVIVE = "UI_Buff_Item_Recovery_Revive"


class TypeEnum(Enum):
    FOOD = "food"


@dataclass
class Item:
    id: int
    name: str
    type: TypeEnum
    recipe: bool
    map_mark: bool
    icon: str
    rank: int
    route: str
    effect_icon: Optional[AtkAdd] = None
    beta: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        type = TypeEnum(obj.get("type"))
        recipe = from_bool(obj.get("recipe"))
        map_mark = from_bool(obj.get("mapMark"))
        icon = from_str(obj.get("icon"))
        rank = from_int(obj.get("rank"))
        route = from_str(obj.get("route"))
        effect_icon = from_union([AtkAdd, from_none], obj.get("effectIcon"))
        beta = from_union([from_bool, from_none], obj.get("beta"))
        return Item(id, name, type, recipe, map_mark, icon, rank, route, effect_icon, beta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["type"] = to_enum(TypeEnum, self.type)
        result["recipe"] = from_bool(self.recipe)
        result["mapMark"] = from_bool(self.map_mark)
        result["icon"] = from_str(self.icon)
        result["rank"] = from_int(self.rank)
        result["route"] = from_str(self.route)
        if self.effect_icon is not None:
            result["effectIcon"] = from_union([lambda x: to_enum(AtkAdd, x), from_none], self.effect_icon)
        if self.beta is not None:
            result["beta"] = from_union([from_bool, from_none], self.beta)
        return result


@dataclass
class Types:
    recovery_hp_add: AtkAdd
    recovery_revive: AtkAdd
    recovery_hp_add_all: AtkAdd
    other_sp_reduce_consume: AtkAdd
    atk_crit_rate: AtkAdd
    def_add: AtkAdd
    other_sp_add: AtkAdd
    atk_add: AtkAdd
    climate_heat: AtkAdd
    no_effect: None

    @staticmethod
    def from_dict(obj: Any) -> 'Types':
        assert isinstance(obj, dict)
        recovery_hp_add = AtkAdd(obj.get("recoveryHpAdd"))
        recovery_revive = AtkAdd(obj.get("recoveryRevive"))
        recovery_hp_add_all = AtkAdd(obj.get("recoveryHpAddAll"))
        other_sp_reduce_consume = AtkAdd(obj.get("otherSPReduceConsume"))
        atk_crit_rate = AtkAdd(obj.get("atkCritRate"))
        def_add = AtkAdd(obj.get("defAdd"))
        other_sp_add = AtkAdd(obj.get("otherSPAdd"))
        atk_add = AtkAdd(obj.get("atkAdd"))
        climate_heat = AtkAdd(obj.get("climateHeat"))
        no_effect = from_none(obj.get("noEffect"))
        return Types(recovery_hp_add, recovery_revive, recovery_hp_add_all, other_sp_reduce_consume, atk_crit_rate, def_add, other_sp_add, atk_add, climate_heat, no_effect)

    def to_dict(self) -> dict:
        result: dict = {}
        result["recoveryHpAdd"] = to_enum(AtkAdd, self.recovery_hp_add)
        result["recoveryRevive"] = to_enum(AtkAdd, self.recovery_revive)
        result["recoveryHpAddAll"] = to_enum(AtkAdd, self.recovery_hp_add_all)
        result["otherSPReduceConsume"] = to_enum(AtkAdd, self.other_sp_reduce_consume)
        result["atkCritRate"] = to_enum(AtkAdd, self.atk_crit_rate)
        result["defAdd"] = to_enum(AtkAdd, self.def_add)
        result["otherSPAdd"] = to_enum(AtkAdd, self.other_sp_add)
        result["atkAdd"] = to_enum(AtkAdd, self.atk_add)
        result["climateHeat"] = to_enum(AtkAdd, self.climate_heat)
        result["noEffect"] = from_none(self.no_effect)
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
class BaseFood:
    response: int
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'BaseFood':
        assert isinstance(obj, dict)
        response = from_int(obj.get("response"))
        data = Data.from_dict(obj.get("data"))
        return BaseFood(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = from_int(self.response)
        result["data"] = to_class(Data, self.data)
        return result


def base_food_from_dict(s: Any) -> BaseFood:
    return BaseFood.from_dict(s)


def base_food_to_dict(x: BaseFood) -> Any:
    return to_class(BaseFood, x)

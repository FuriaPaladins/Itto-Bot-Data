from dataclasses import dataclass
from typing import Optional, Any, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Item:
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    recipe: Optional[bool] = None
    map_mark: Optional[bool] = None
    icon: Optional[str] = None
    rank: Optional[int] = None
    route: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        recipe = from_union([from_bool, from_none], obj.get("recipe"))
        map_mark = from_union([from_bool, from_none], obj.get("mapMark"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        rank = from_union([from_int, from_none], obj.get("rank"))
        route = from_union([from_str, from_none], obj.get("route"))
        return Item(id, name, type, recipe, map_mark, icon, rank, route)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.recipe is not None:
            result["recipe"] = from_union([from_bool, from_none], self.recipe)
        if self.map_mark is not None:
            result["mapMark"] = from_union([from_bool, from_none], self.map_mark)
        if self.icon is not None:
            result["icon"] = from_union([from_str, from_none], self.icon)
        if self.rank is not None:
            result["rank"] = from_union([from_int, from_none], self.rank)
        if self.route is not None:
            result["route"] = from_union([from_str, from_none], self.route)
        return result


@dataclass
class Types:
    forging_ore: Optional[str] = None
    cooking_ingredient: Optional[str] = None
    material: Optional[str] = None
    local_specialty_mondstadt: Optional[str] = None
    local_specialty_liyue: Optional[str] = None
    local_specialty_inazuma: Optional[str] = None
    local_specialty_sumeru: Optional[str] = None
    potion: Optional[str] = None
    character_level_up_material: Optional[str] = None
    character_ascension_material: Optional[str] = None
    weapon_ascension_material: Optional[str] = None
    characterand_weapon_enhancement_material: Optional[str] = None
    quest_item: Optional[str] = None
    character_talent_material: Optional[str] = None
    adventure_item: Optional[str] = None
    consumable: Optional[str] = None
    gadget: Optional[str] = None
    system_access: Optional[str] = None
    increases_friendship: Optional[str] = None
    special_currency: Optional[str] = None
    common_currency: Optional[str] = None
    superior_voucher: Optional[str] = None
    common_voucher: Optional[str] = None
    limited_wishing_item: Optional[str] = None
    wishing_item: Optional[str] = None
    city_states_sigil: Optional[str] = None
    character_exp_material: Optional[str] = None
    weapon_enhancement_material: Optional[str] = None
    challenge_result_item: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Types':
        assert isinstance(obj, dict)
        forging_ore = from_union([from_str, from_none], obj.get("forgingOre"))
        cooking_ingredient = from_union([from_str, from_none], obj.get("cookingIngredient"))
        material = from_union([from_str, from_none], obj.get("material"))
        local_specialty_mondstadt = from_union([from_str, from_none], obj.get("localSpecialtyMondstadt"))
        local_specialty_liyue = from_union([from_str, from_none], obj.get("localSpecialtyLiyue"))
        local_specialty_inazuma = from_union([from_str, from_none], obj.get("localSpecialtyInazuma"))
        local_specialty_sumeru = from_union([from_str, from_none], obj.get("localSpecialtySumeru"))
        potion = from_union([from_str, from_none], obj.get("potion"))
        character_level_up_material = from_union([from_str, from_none], obj.get("characterLevelUpMaterial"))
        character_ascension_material = from_union([from_str, from_none], obj.get("characterAscensionMaterial"))
        weapon_ascension_material = from_union([from_str, from_none], obj.get("weaponAscensionMaterial"))
        characterand_weapon_enhancement_material = from_union([from_str, from_none], obj.get("characterandWeaponEnhancementMaterial"))
        quest_item = from_union([from_str, from_none], obj.get("questItem"))
        character_talent_material = from_union([from_str, from_none], obj.get("characterTalentMaterial"))
        adventure_item = from_union([from_str, from_none], obj.get("adventureItem"))
        consumable = from_union([from_str, from_none], obj.get("consumable"))
        gadget = from_union([from_str, from_none], obj.get("gadget"))
        system_access = from_union([from_str, from_none], obj.get("systemAccess"))
        increases_friendship = from_union([from_str, from_none], obj.get("increasesFriendship"))
        special_currency = from_union([from_str, from_none], obj.get("specialCurrency"))
        common_currency = from_union([from_str, from_none], obj.get("commonCurrency"))
        superior_voucher = from_union([from_str, from_none], obj.get("superiorVoucher"))
        common_voucher = from_union([from_str, from_none], obj.get("commonVoucher"))
        limited_wishing_item = from_union([from_str, from_none], obj.get("limitedWishingItem"))
        wishing_item = from_union([from_str, from_none], obj.get("wishingItem"))
        city_states_sigil = from_union([from_str, from_none], obj.get("cityStatesSigil"))
        character_exp_material = from_union([from_str, from_none], obj.get("characterEXPMaterial"))
        weapon_enhancement_material = from_union([from_str, from_none], obj.get("weaponEnhancementMaterial"))
        challenge_result_item = from_union([from_str, from_none], obj.get("challengeResultItem"))
        return Types(forging_ore, cooking_ingredient, material, local_specialty_mondstadt, local_specialty_liyue, local_specialty_inazuma, local_specialty_sumeru, potion, character_level_up_material, character_ascension_material, weapon_ascension_material, characterand_weapon_enhancement_material, quest_item, character_talent_material, adventure_item, consumable, gadget, system_access, increases_friendship, special_currency, common_currency, superior_voucher, common_voucher, limited_wishing_item, wishing_item, city_states_sigil, character_exp_material, weapon_enhancement_material, challenge_result_item)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.forging_ore is not None:
            result["forgingOre"] = from_union([from_str, from_none], self.forging_ore)
        if self.cooking_ingredient is not None:
            result["cookingIngredient"] = from_union([from_str, from_none], self.cooking_ingredient)
        if self.material is not None:
            result["material"] = from_union([from_str, from_none], self.material)
        if self.local_specialty_mondstadt is not None:
            result["localSpecialtyMondstadt"] = from_union([from_str, from_none], self.local_specialty_mondstadt)
        if self.local_specialty_liyue is not None:
            result["localSpecialtyLiyue"] = from_union([from_str, from_none], self.local_specialty_liyue)
        if self.local_specialty_inazuma is not None:
            result["localSpecialtyInazuma"] = from_union([from_str, from_none], self.local_specialty_inazuma)
        if self.local_specialty_sumeru is not None:
            result["localSpecialtySumeru"] = from_union([from_str, from_none], self.local_specialty_sumeru)
        if self.potion is not None:
            result["potion"] = from_union([from_str, from_none], self.potion)
        if self.character_level_up_material is not None:
            result["characterLevelUpMaterial"] = from_union([from_str, from_none], self.character_level_up_material)
        if self.character_ascension_material is not None:
            result["characterAscensionMaterial"] = from_union([from_str, from_none], self.character_ascension_material)
        if self.weapon_ascension_material is not None:
            result["weaponAscensionMaterial"] = from_union([from_str, from_none], self.weapon_ascension_material)
        if self.characterand_weapon_enhancement_material is not None:
            result["characterandWeaponEnhancementMaterial"] = from_union([from_str, from_none], self.characterand_weapon_enhancement_material)
        if self.quest_item is not None:
            result["questItem"] = from_union([from_str, from_none], self.quest_item)
        if self.character_talent_material is not None:
            result["characterTalentMaterial"] = from_union([from_str, from_none], self.character_talent_material)
        if self.adventure_item is not None:
            result["adventureItem"] = from_union([from_str, from_none], self.adventure_item)
        if self.consumable is not None:
            result["consumable"] = from_union([from_str, from_none], self.consumable)
        if self.gadget is not None:
            result["gadget"] = from_union([from_str, from_none], self.gadget)
        if self.system_access is not None:
            result["systemAccess"] = from_union([from_str, from_none], self.system_access)
        if self.increases_friendship is not None:
            result["increasesFriendship"] = from_union([from_str, from_none], self.increases_friendship)
        if self.special_currency is not None:
            result["specialCurrency"] = from_union([from_str, from_none], self.special_currency)
        if self.common_currency is not None:
            result["commonCurrency"] = from_union([from_str, from_none], self.common_currency)
        if self.superior_voucher is not None:
            result["superiorVoucher"] = from_union([from_str, from_none], self.superior_voucher)
        if self.common_voucher is not None:
            result["commonVoucher"] = from_union([from_str, from_none], self.common_voucher)
        if self.limited_wishing_item is not None:
            result["limitedWishingItem"] = from_union([from_str, from_none], self.limited_wishing_item)
        if self.wishing_item is not None:
            result["wishingItem"] = from_union([from_str, from_none], self.wishing_item)
        if self.city_states_sigil is not None:
            result["cityStatesSigil"] = from_union([from_str, from_none], self.city_states_sigil)
        if self.character_exp_material is not None:
            result["characterEXPMaterial"] = from_union([from_str, from_none], self.character_exp_material)
        if self.weapon_enhancement_material is not None:
            result["weaponEnhancementMaterial"] = from_union([from_str, from_none], self.weapon_enhancement_material)
        if self.challenge_result_item is not None:
            result["challengeResultItem"] = from_union([from_str, from_none], self.challenge_result_item)
        return result


@dataclass
class Data:
    types: Optional[Types] = None
    items: Optional[Dict[str, Item]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        types = from_union([Types.from_dict, from_none], obj.get("types"))
        items = from_union([lambda x: from_dict(Item.from_dict, x), from_none], obj.get("items"))
        return Data(types, items)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.types is not None:
            result["types"] = from_union([lambda x: to_class(Types, x), from_none], self.types)
        if self.items is not None:
            result["items"] = from_union([lambda x: from_dict(lambda x: to_class(Item, x), x), from_none], self.items)
        return result


@dataclass
class LoadoutCards:
    response: Optional[int] = None
    data: Optional[Data] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LoadoutCards':
        assert isinstance(obj, dict)
        response = from_union([from_int, from_none], obj.get("response"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return LoadoutCards(response, data)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.response is not None:
            result["response"] = from_union([from_int, from_none], self.response)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        return result


def material_base_from_dict(s: Any) -> LoadoutCards:
    return LoadoutCards.from_dict(s)


def material_base_to_dict(x: LoadoutCards) -> Any:
    return to_class(LoadoutCards, x)

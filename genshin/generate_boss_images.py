import os, requests, asyncio, aiohttp_client_cache, aiohttp, json
import random

from PIL import Image, ImageDraw, ImageChops
from aiohttp_client_cache import SQLiteBackend
from rich import print

from ambr_classes.monster_base import monster_base_from_dict
from ambr_classes.avatar_base import avatar_base_from_dict
from ambr_classes.materials_base import material_base_from_dict
from ambr_classes.monster_data import monsters_from_dict

from ambr_classes.avatar_data import avatar_data_from_dict

from fetch_images import GenshinImages, __format_name__


async def make_req(session, url):
    async with session.get(url) as resp:
        return await resp.json()


async def get_boss_data():

    async with aiohttp.ClientSession() as session:
        ## Get the base data for monsters, characters and materials
        async with session.get("https://api.ambr.top/v2/en/monster") as resp:
            base_monsters = monster_base_from_dict((await resp.json()))
        async with session.get("https://api.ambr.top/v2/en/avatar") as resp:
            base_avatars = avatar_base_from_dict((await resp.json()))
        async with session.get("https://api.ambr.top/v2/en/material") as resp:
            base_materials = material_base_from_dict((await resp.json()))

    async with aiohttp_client_cache.CachedSession(cache=SQLiteBackend('ambr_data-bot')) as session:
        ## Sort out and expand all bosses
        bosses = [base_monsters.data.items[i] for i in base_monsters.data.items if
                  base_monsters.data.items[i].type.name == "BOSS"]
        bosses_full = []
        for boss in await asyncio.gather(*[make_req(session, f"https://api.ambr.top/v2/en/monster/{boss.id}") for boss in bosses]):
            bosses_full.append(monsters_from_dict(boss))
        bosses_full = [i.data for i in bosses_full]

        ## Sort out and expand all characters
        characters = [base_avatars.data.items[i] for i in base_avatars.data.items]
        characters_full = []
        for character in characters:
            characters_full.append(avatar_data_from_dict((await make_req(session, f"https://api.ambr.top/v2/en/avatar/{character.id}"))))
        characters_full = [i.data for i in characters_full]

        ## Sort out all the characterLevelUpMaterials:
        materials_full = [base_materials.data.items[i] for i in base_materials.data.items if base_materials.data.items[i].type == "characterLevelUpMaterial" and base_materials.data.items[i].rank == 5]

    ## Now we need to create all the dictionaries.
    ## Find all items which in base_materials have type of characterLevelUpMaterial
    ## Then find all bosses which have the item in their rewards
    ## Then find all characters which have the item in their talent costs
    the_data = []
    for boss in bosses_full:
        the_data.append({'name': boss.name, 'id': boss.id, 'special_name': boss.special_name, 'title': boss.title, 'materials': []})
        boss_material_list = []
        for entry in boss.entries:
            entry = boss.entries[entry]
            if entry.reward is not None:
                boss_material_list.extend(entry.reward)
        boss_material_list = [int(i) for i in boss_material_list]

        for material in materials_full:
            if material.id in boss_material_list:
                character_with_mats = []
                for character in characters_full:
                    character_drops = list(character.talent["0"].promote["9"].cost_items.keys())
                    if str(material.id) in character_drops:
                        if {'name': character.name, 'element': character.element} not in character_with_mats:
                            character_with_mats.append({'name': character.name, 'element': character.element})

                the_data[-1]['materials'].append({'id': material.id, 'name': material.name, 'characters': character_with_mats})

    ## AFTER ALL THE DATA IS COLLECTED
    return the_data


async def generate_boss_image(boss):
    img = Image.open(f".other/bosses/base/{__format_name__(boss['name'])}.png")

    for enum, material in enumerate(boss['materials']):
        location = (182, 380 + (212 * enum))
        mat_img = Image.open(f"materials/character_level-up_material/{__format_name__(material['name'])}.png").convert('RGBA').resize((192, 192))
        img.alpha_composite(mat_img, location)

        for enum_1, character in enumerate(material['characters']):
            location_a = (location[0] + 178) + (144 * enum_1), location[1]+32

            elem_img = Image.open(f"element_icons/{GenshinImages.convert_element(character['element'])}.png").convert('RGBA').resize((128, 128))
            if character['name'] != 'Traveler':
                char_img = Image.open(f"characters/{GenshinImages.convert_element(character['element'])}/{__format_name__(character['name'])}/icon.png").convert('RGBA').resize((128, 128))
            else:
                char_img = Image.open(f"characters/travellers/{random.choice(['aether', 'lumine'])}/icon.png").convert('RGBA').resize((128, 128))
            img.alpha_composite(elem_img, location_a)
            img.alpha_composite(char_img, location_a)

    img.save(f".other/bosses/generated/{__format_name__(boss['name'])}.png")


async def main_boss_data():
    boss_data = await get_boss_data()
    for boss in boss_data:
        await generate_boss_image(boss)

asyncio.run(main_boss_data())

import requests, os, json, re


## Some useful functions
def download_image(url, filename):
    if os.path.exists(filename):
        return
    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)


def create_directory(directory):
    isExist = os.path.exists(directory)
    if not isExist:
        os.makedirs(directory)


def get_weapon_type(base_data, w_type):
    if w_type == "WEAPON_SWORD_ONE_HAND":
        return base_data.data.types.weapon_sword_one_hand
    elif w_type == "WEAPON_CLAYMORE":
        return base_data.data.types.weapon_claymore
    elif w_type == "WEAPON_POLE":
        return base_data.data.types.weapon_pole
    elif w_type == "WEAPON_CATALYST":
        return base_data.data.types.weapon_catalyst
    else:
        return base_data.data.types.weapon_bow


# https://genshin.honeyhunterworld.com/img/i_n15503.webp
# https://genshin.honeyhunterworld.com/img/i_n15503_awaken_icon.webp
# https://genshin.honeyhunterworld.com/img/i_n15503_gacha_icon.webp
def main():
    base_url = "https://api.ambr.top/v2/en/weapon"

    base_data = weapon_base_from_dict(requests.get(base_url).json())
    base_art_url = "https://genshin.honeyhunterworld.com/img/i_n"

    base_directory = "weapons/" if ran_normally else "assets/genshin/weapons/"
    for weapon_t in base_data.data.items:
        use_w = base_data.data.items[weapon_t]
        use_name = re.compile(r"""[.\/'\":]""").sub("", use_w.name).lower().replace(" ", "_")
        create_directory(f"{base_directory}{get_weapon_type(base_data, use_w.type.name).lower()}/{use_name}")

        download_image(f"{base_art_url}{use_w.id}.webp",
                       f"{base_directory}{get_weapon_type(base_data, use_w.type.name).lower()}/{use_name}/icon.png")
        download_image(f"{base_art_url}{use_w.id}_awaken_icon.webp",
                       f"{base_directory}{get_weapon_type(base_data, use_w.type.name).lower()}/{use_name}/awakened_icon.png")
        download_image(f"{base_art_url}{use_w.id}_gacha_icon.webp",
                       f"{base_directory}{get_weapon_type(base_data, use_w.type.name).lower()}/{use_name}/gacha_icon.png")
    return True


if __name__ == '__main__':
    from ambr_classes.weapon_base import weapon_base_from_dict
    ran_normally = True
    main()

else:
    from assets.genshin.ambr_classes.weapon_base import weapon_base_from_dict
    ran_normally = False
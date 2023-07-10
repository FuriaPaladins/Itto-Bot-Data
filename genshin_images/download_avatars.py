from ambr_wrapper_test.avatar_base import avatar_base_from_dict
from ambr_wrapper_test.avatar_data import avatar_data_from_dict
from tqdm import tqdm
import requests, json, os, time
from bs4 import BeautifulSoup as bs

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

class Elements:
    DENDRO = "Dendro"
    ANEMO = "Anemo"
    PYRO = "Pyro"
    GEO = "Geo"
    CRYO = "Cryo"
    HYDRO = "Hydro"
    ELECTRO = "Electro"
    
    def __init__(self, value: str):
        self.value = value
    
    def __repr__(self):
        if self.value == "Grass":
            return Elements.DENDRO
        elif self.value == "Wind":
            return Elements.ANEMO
        elif self.value == "Fire":
            return Elements.PYRO
        elif self.value == "Rock":
            return Elements.GEO
        elif self.value == "Ice":
            return Elements.CRYO
        elif self.value == "Water":
            return Elements.HYDRO
        elif self.value == "Electric":
            return Elements.ELECTRO

    def __str__(self):
        return self.__repr__()

import contextlib
base_url = "https://api.ambr.top/v2/en/avatar"
base_data = avatar_base_from_dict(requests.get(base_url).json())

base_directory = "characters/"

base_asset_directory = "https://api.ambr.top/assets/UI/"
base_honey_directory = "https://genshin.honeyhunterworld.com/img/"
## Scan through everything in base_data.data.items, and show the character with a progressbar
for character_id in tqdm(base_data.data.items):
    char = avatar_data_from_dict(requests.get(f"{base_url}/{character_id}").json()).data
    char_data = requests.get(f"{base_url}/{character_id}").json()
    use_directory = f"{base_directory}{str(Elements(char.element)).lower()}/{char.name}"
    print(f" Downloading Items for: {char.name} ({Elements(char.element)})")
    if char.name == "Traveler":
        continue


    create_directory(f"{base_directory}{str(Elements(char.element)).lower()}/{char.name}")
    ## Character Icon
    download_image(f"{base_asset_directory}{char.icon}.png", f"{use_directory}/icon.png")

    ## Namecard
    namecard_name = char.other.name_card.icon.split("_")[-1]
    # Namecard Icon
    download_image(f"{base_asset_directory}namecard/UI_NameCardIcon_{namecard_name}.png", f"{use_directory}/namecard_icon.png")
    download_image(f"{base_asset_directory}namecard/UI_NameCardPic_{namecard_name}_P.png", f"{use_directory}/namecard_picture.png")
    ## Special Food
    if char.other.special_food is not None:
        download_image(f"{base_asset_directory}/{char.other.special_food.icon}.png", f"{use_directory}/special_food.png")
    ## Gacha Art
    download_image(f"{base_asset_directory}UI_Gacha_AvatarImg_{namecard_name}.png", f"{use_directory}/gacha_art_full.png")

    ## Constellation Icons
    for i in char.constellation:
        download_image(f"{base_asset_directory}{char.constellation[i].icon}.png", f"{use_directory}/constellation_{i}.png")
    ## Talent Icons
    for i in char.talent:
        download_image(f"{base_asset_directory}{char.talent[i].icon}.png", f"{use_directory}/talent_{i}.png")
    
    ## Honeyhunter Stuff
    # Gacha Card
    download_image(f"{base_honey_directory}{namecard_name.lower()}_{str(char.id)[-3:]}_gacha_splash.webp", f"{use_directory}/gacha_art_cropped.png")
    download_image(f"{base_honey_directory}{namecard_name.lower()}_{str(char.id)[-3:]}_gacha_card.webp", f"{use_directory}/gacha_art_card.png")
    # Side Icon
    download_image(f"{base_honey_directory}{namecard_name.lower()}_{str(char.id)[-3:]}_side_icon.webp", f"{use_directory}/icon_side.png")

    ## Wiki Stuff
    with contextlib.suppress(Exception):
        req = requests.get(f"https://genshin-impact.fandom.com/wiki/{char.name}/Media")
        soup = bs(req.text, "html.parser").find_all("img")
        for i in soup:
            if "Portrait" in str(i.get("data-caption")) and "lazyload" not in str(i.get("class")):
                download_image(str(i.get("src")).split("/revision/")[0], f"{use_directory}/portrait.png")
            elif "Constellation" in str(i.get("data-caption")) and "lazyload" not in str(i.get("class")):
                download_image(str(i.get("src")).split("/revision/")[0], f"{use_directory}/constellation.png")
    
    time.sleep(0.15)
    
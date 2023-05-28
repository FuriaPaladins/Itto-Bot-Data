from ambr_wrapper_test.monster_base import monster_base_from_dict
import requests, os, json, re
from tqdm import tqdm


def download_image(url, filename):
    if os.path.exists(filename):
        return
    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)


def create_directory(directory):
    isExist = os.path.exists(directory)
    if not isExist:
        os.makedirs(directory)


base_url = "https://api.ambr.top/v2/en/monster"
base_data = monster_base_from_dict(requests.get(base_url).json())

for i in tqdm(base_data.data.items):
    use_item = base_data.data.items[i]
    test = re.compile(r"""[.\/'\":]""").sub("", use_item.name).lower().replace(" ", "_")
    create_directory(f"monsters/{str(use_item.type.name).lower()}/")
    try:
        download_image(f"https://api.ambr.top/assets/UI/monster/{use_item.icon}.png", f"monsters/{str(use_item.type.name).lower()}/{test}.png")
    except Exception as e:
        download_image(f"https://api.ambr.top/assets/UI/{use_item.icon}.png", f"monsters/{str(use_item.type.name).lower()}/{test}.png")
        
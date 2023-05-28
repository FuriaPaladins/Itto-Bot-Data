from ambr_wrapper_test.furniture_base import furniture_base_from_dict
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

base_url = "https://api.ambr.top/v2/en/furniture"
base_data = furniture_base_from_dict(requests.get(base_url).json())


for i in tqdm(base_data.data.items):
    t = base_data.data.items[i]
    ## re - replace all values: ./'": with nothing
    test = re.compile(r"""[.\/'\":]""").sub("", t.name).lower().replace(" ", "_")
    create_directory(f"furniture/{t.categories[0].name.lower()}")
    try:
        download_image(f"https://api.ambr.top/assets/UI/furniture/{t.icon}.png", f"furniture/{t.categories[0].name.lower()}/{test}.png")
    except:
        download_image(f"https://api.ambr.top/assets/UI/monster/{t.icon}.png", f"furniture/{t.categories[0].name.lower()}/{test}.png")
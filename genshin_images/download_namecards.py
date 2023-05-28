from ambr_wrapper_test.namecard_base import namecard_from_dict
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

base_url = "https://api.ambr.top/v2/en/namecard"
base_data = namecard_from_dict(requests.get(base_url).json())


for i in tqdm(base_data.data.items):
    t = base_data.data.items[i]
    ## re - replace all values: ./'": with nothing
    test = re.compile(r"""[.\/'\":]""").sub("", t.name).lower().replace(" ", "_")
    create_directory(f"namecard/{t.type.name.lower()}")
    download_image(f"https://api.ambr.top/assets/UI/namecard/{t.icon}.png", f"namecard/{t.type.name.lower()}/{test}_icon.png")
    download_image(f"https://api.ambr.top/assets/UI/namecard/{t.icon.replace('Icon', 'Pic')}_P.png", f"namecard/{t.type.name.lower()}/{test}_pic.png")
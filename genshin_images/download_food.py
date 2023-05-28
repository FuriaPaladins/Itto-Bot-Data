from ambr_wrapper_test.food_base import base_food_from_dict
import requests, os, json

def download_image(url, filename):
    if os.path.exists(filename):
        return
    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)

def create_directory(directory):
    isExist = os.path.exists(directory)
    if not isExist:
        os.makedirs(directory)

base_url = "https://api.ambr.top/v2/en/food"
base_data = base_food_from_dict(requests.get(base_url).json())

THING_1 = '"'
THING_2 = "\\"
THING_3 = "'"
create_directory("food/")
for food in base_data.data.items:
    use_data = base_data.data.items[food]
    if use_data.name == "???":
        continue
    print(use_data.name)
    download_image(f"https://api.ambr.top/assets/UI/{use_data.icon}.png", f"food/{str(use_data.name).lower().replace(' ', '_').replace(THING_1, '').replace(THING_2, '').replace(THING_3, '')}.png")
from ambr_wrapper_test.materials_base import material_base_to_dict, material_base_from_dict
from ambr_wrapper_test.materials_data import materials_to_dict, materials_from_dict
from PIL import Image

from tqdm import tqdm
import json, os, requests, arrow, time, re

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

def parse_artifacts(artifact_icon):
    icon = int(artifact_icon.split('_')[-1])
    if icon == 1:
        return "goblet"
    elif icon == 2:
        return "feather"
    elif icon == 3:
        return "crown"
    elif icon == 4:
        return "flower"
    else:
        return "sands"

def generate_atlas(directory):
    image_list = [f"{directory}{i}" for i in os.listdir(directory)]
    if f"{directory}atlas.png" in image_list:
        image_list.remove(f"{directory}atlas.png")
    base_x, base_y = Image.open(image_list[0]).size

    ## Create an xy grid of images
    grid_image = Image.new("RGBA", (base_x * len(image_list), base_y))
    for i, image in enumerate(image_list):
        grid_image.paste(Image.open(image).resize((base_x, base_y)), (i * base_x, 0))

    grid_image.save(f"{directory}atlas.png")

base_url = "https://api.ambr.top/v2/en/material"
base_asset_directory = "https://api.ambr.top/assets/UI/"
base_data = material_base_from_dict(requests.get(base_url).json())

base_directory = "materials/"
for material in base_data.data.items:
    item = materials_from_dict(requests.get(f"{base_url}/{material}").json()).data
    print(f"Downloading {item.name}...")
    create_directory(f"materials/{str(item.type).lower().replace(' ', '_')}/")
    download_image(f"https://api.ambr.top/assets/UI/{item.icon}.png", f"materials/{str(item.type).lower().replace(' ', '_')}/{str(item.name).lower().replace(' ', '_')}.png")
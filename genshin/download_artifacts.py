
from PIL import Image

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


def main():
    base_url = "https://api.ambr.top/v2/en/reliquary"
    base_asset_directory = "https://api.ambr.top/assets/UI/"
    base_data = artifacts_base_from_dict(requests.get(base_url).json())

    base_directory = "artifacts/" if ran_normally else "assets/genshin/artifacts/"
    for artifact_set in base_data.data.items:
        full_set = artifacts_data_from_dict(requests.get(f"{base_url}/{artifact_set}").json()).data
        full_set.name = re.compile(r"""[.\/'\":]""").sub("", full_set.name).lower().replace(" ", "_")
        create_directory(f"{base_directory}{str(full_set.name).lower().replace(' ', '_')}/")
        for i in [full_set.suit.equip_bracer, full_set.suit.equip_dress, full_set.suit.equip_necklace,
                  full_set.suit.equip_ring, full_set.suit.equip_shoes]:
            try:
                download_image(f"{base_asset_directory}reliquary/{i.icon}.png",
                               f"{base_directory}{str(full_set.name).lower().replace(' ', '_')}/{parse_artifacts(i.icon)}.png")
            except:
                pass
        generate_atlas(f"{base_directory}{str(full_set.name).lower().replace(' ', '_')}/")
    return True


if __name__ == "__main__":
    from ambr_classes.artifacts_base import artifacts_base_from_dict
    from ambr_classes.artifacts_data import artifacts_data_from_dict
    ran_normally = True
    main()

else:
    from assets.genshin.ambr_classes.artifacts_base import artifacts_base_from_dict
    from assets.genshin.ambr_classes.artifacts_data import artifacts_data_from_dict
    ran_normally = False


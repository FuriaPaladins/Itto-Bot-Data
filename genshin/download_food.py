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

def main():
    base_url = "https://api.ambr.top/v2/en/food"
    base_data = base_food_from_dict(requests.get(base_url).json())

    THING_1 = '"'
    THING_2 = "\\"
    THING_3 = "'"
    base_directory = "food/" if ran_normally else "assets/genshin/food/"
    create_directory(base_directory)
    for food in base_data.data.items:
        use_data = base_data.data.items[food]
        if use_data.name == "???":
            continue
        download_image(f"https://api.ambr.top/assets/UI/{use_data.icon}.png",
                       f"{base_directory}{str(use_data.name).lower().replace(' ', '_').replace(THING_1, '').replace(THING_2, '').replace(THING_3, '')}.png")
    return True


if __name__ == '__main__':
    from ambr_classes.food_base import base_food_from_dict
    ran_normally = True
    main()

else:
    from assets.genshin.ambr_classes.food_base import base_food_from_dict
    ran_normally = False
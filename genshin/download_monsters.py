
import requests, os, json, re



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
    base_url = "https://api.ambr.top/v2/en/monster"
    base_data = monster_base_from_dict(requests.get(base_url).json())

    base_directory = "monsters/" if ran_normally else "assets/genshin/monsters/"
    for i in base_data.data.items:
        use_item = base_data.data.items[i]
        test = re.compile(r"""[.\/'\":]""").sub("", use_item.name).lower().replace(" ", "_")
        create_directory(f"{base_directory}{str(use_item.type.name).lower()}/")
        try:
            download_image(f"https://api.ambr.top/assets/UI/monster/{use_item.icon}.png",
                           f"{base_directory}{str(use_item.type.name).lower()}/{test}.png")
        except Exception as e:
            download_image(f"https://api.ambr.top/assets/UI/{use_item.icon}.png",
                           f"{base_directory}{str(use_item.type.name).lower()}/{test}.png")
    return True


if __name__ == '__main__':
    from ambr_classes.monster_base import monster_base_from_dict
    ran_normally = True
    main()

else:
    from assets.genshin.ambr_classes.monster_base import monster_base_from_dict
    ran_normally = False

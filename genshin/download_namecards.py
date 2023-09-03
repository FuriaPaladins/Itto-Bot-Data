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
    base_url = "https://api.ambr.top/v2/en/namecard"
    base_data = namecard_from_dict(requests.get(base_url).json())

    base_directory = "namecard/" if ran_normally else "assets/genshin/namecard/"
    for i in base_data.data.items:
        t = base_data.data.items[i]
        ## re - replace all values: ./'": with nothing
        test = re.compile(r"""[.\/'\":]""").sub("", t.name).lower().replace(" ", "_")
        create_directory(f"{base_directory}{t.type.name.lower()}")
        download_image(f"https://api.ambr.top/assets/UI/namecard/{t.icon}.png",
                       f"{base_directory}{t.type.name.lower()}/{test}_icon.png")
        download_image(f"https://api.ambr.top/assets/UI/namecard/{t.icon.replace('Icon', 'Pic')}_P.png",
                       f"{base_directory}{t.type.name.lower()}/{test}_pic.png")
    return True


if __name__ == '__main__':
    from ambr_classes.namecard_base import namecard_from_dict
    ran_normally = True
    main()

else:
    from assets.genshin.ambr_classes.namecard_base import namecard_from_dict
    ran_normally = False
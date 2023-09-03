import asyncio
import os

import requests
import json

def download_image(url, filename):
    if os.path.exists(filename):
        return
    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)


def create_directory(directory):
    isExist = os.path.exists(directory)
    if not isExist:
        os.makedirs(directory)


def replace_many(text, replace):
    for i in replace:
        text = text.replace(i, '')
    return text


async def download_light_cones():
    main_url = "https://api.yatta.top/hsr/v2/en/equipment"
    req = requests.get(main_url).json()

    for item in req['data']['items']:
        item_req = requests.get(f"{main_url}/{item}").json()
        use_dir = f"""light_cones/{replace_many(item_req['data']['types']['pathType']['name'], ['"', "'", '-', ',']).lower().replace(' ', '_')}/{replace_many(item_req['data']['name'], ['"', "'", '-', ',']).lower().replace(' ', '_')}"""
        create_directory(use_dir)

        download_image(f"https://api.yatta.top/hsr/assets/UI/equipment/medium/{item_req['data']['id']}.png", f"{use_dir}/medium.png")
        download_image(f"https://api.yatta.top/hsr/assets/UI/equipment/large/{item_req['data']['id']}.png", f"{use_dir}/large.png")


if __name__ == "__main__":
    asyncio.run(download_light_cones())

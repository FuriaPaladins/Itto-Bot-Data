import asyncio

import aiohttp
import aiohttp_client_cache
import os


async def download_image(image, filename):
    await create_directory(os.path.dirname(filename))
    if os.path.exists(filename):
        return

    print(f"Downloading {filename}")
    with open(filename, 'wb') as f:
        f.write(await image.read())


async def create_directory(directory):
    print(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)


async def download_genshin_images(base_directory=""):
    async with aiohttp_client_cache.CachedSession() as req:
        print("Downloading genshin images")
        m_req = await req.get("https://api.ambr.top/assets/UI/reliquary/UI_RelicIcon_10010_4.png")
        await download_image(m_req, f"{base_directory}test/sands.png")


asyncio.run(download_genshin_images())

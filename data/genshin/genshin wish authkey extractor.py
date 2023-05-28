import genshin
import asyncio
import pyperclip


async def main():
    try:
        genshin_authkey = genshin.utility.get_authkey()
        pyperclip.copy(genshin_authkey)
        print("Copied to clipboard!")
    except Exception:
        genshin_authkey = Exception
    await asyncio.sleep(0.20)
    return genshin_authkey


print("Extracting authkey...")
auth_key = asyncio.run(main())
print(auth_key)
input()

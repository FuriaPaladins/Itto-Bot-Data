"""
This file is used to get cookies from your browser.
Uses the browser_cookie3 library to get your cookies: https://github.com/borisbabic/browser_cookie3
"""

import browser_cookie3
import pyperclip


def get_browser_cookies():
    get_cookies = browser_cookie3.load(domain_name="hoyolab")
    return_cookies = {}
    for cookie in get_cookies:
        if cookie.name == "ltoken" or cookie.name == "ltuid":
            return_cookies[cookie.name] = cookie.value
        if cookie.name == "ltoken_v2" or cookie.name == "ltuid_v2":
            return_cookies[cookie.name[:-3]] = cookie.value

    return f"ltoken={return_cookies.get('ltoken', None)}; ltuid={return_cookies.get('ltuid', None)};"


if __name__ == "__main__":
    try:
        cookies = get_browser_cookies()
    except Exception as e:
        print(f"An error occurred: \n{e}")
        input()
        exit()

    pyperclip.copy(cookies)
    print(f"Your cookie tokens have been copied to your clipboard!\n{cookies}")
    input()

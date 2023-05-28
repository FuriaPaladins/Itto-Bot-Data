from ambr_wrapper_test.book_base import book_base_from_dict
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


base_url = "https://api.ambr.top/v2/en/book"
base_data = book_base_from_dict(requests.get(base_url).json())
QUOTE = '"'
base_directory = "books/"

create_directory(f"{base_directory}")
for book in base_data.data.items:
    use_book = base_data.data.items[book]
    print(f"Downloading: {use_book.name}")
    download_image(f"https://api.ambr.top/assets/UI/{use_book.icon}.png", f"{base_directory}{str(use_book.name).lower().replace(' ', '_').replace(QUOTE, '').replace(':', '').replace(',', '').replace('?', '')}.png")
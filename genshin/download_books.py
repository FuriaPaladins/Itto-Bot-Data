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
    base_url = "https://api.ambr.top/v2/en/book"
    base_data = book_base_from_dict(requests.get(base_url).json())
    QUOTE = '"'
    base_directory = "books/" if ran_normally else "assets/genshin/books/"

    create_directory(f"{base_directory}")
    for book in base_data.data.items:
        use_book = base_data.data.items[book]
        download_image(f"https://api.ambr.top/assets/UI/{use_book.icon}.png",
                       f"{base_directory}{str(use_book.name).lower().replace(' ', '_').replace(QUOTE, '').replace(':', '').replace(',', '').replace('?', '')}.png")
    return True


if __name__ == '__main__':
    from ambr_classes.book_base import book_base_from_dict
    ran_normally = True
    main()

else:
    from assets.genshin.ambr_classes.book_base import book_base_from_dict
    ran_normally = False

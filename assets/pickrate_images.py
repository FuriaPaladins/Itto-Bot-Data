import os
import requests
from PIL import Image, ImageFont, ImageDraw

url = "https://apexlegendsstatus.com/lib/legendtrend-hourly.json"
response = requests.get(url).json()

CHAR_DIR = r"apex/legend_icons/"
CHAR_LIST = [i for i in os.listdir(CHAR_DIR) if '_recoloured' in i]
FONT_48 = ImageFont.truetype(".fonts/CascadiaCode.ttf", 48)
FONT_32 = ImageFont.truetype(".fonts/CascadiaCode.ttf", 32)
FONT_16 = ImageFont.truetype(".fonts/CascadiaCode.ttf", 16)


legend_data = {}
for i in response:
    if i['name'] == 'Date':
        continue

    current_pr = float(i['data'][-1])
    pr_7_days_ago = float(i['data'][-180])
    pr_diff = ((current_pr - pr_7_days_ago) / pr_7_days_ago) * 100

    print(f"{i['name']} ({i['color']}) - {current_pr} -> {pr_diff}")

    img = Image.open("apex/pickrate_snippet.png").convert('RGBA')
    draw = ImageDraw.Draw(img)

    ## Write character name at the top of the icon
    name_box = draw.textbbox((0, 0), i['name'], font=FONT_32)
    draw.text((img.width // 2 - name_box[2] // 2, 24), i['name'], font=FONT_32, fill="white")

    ## Write character winrate to 1 decimal place
    winrate = f"{current_pr:.1f}%"
    winrate_box = draw.textbbox((0, 0), winrate, font=FONT_48)
    draw.text((img.width // 2 - winrate_box[2] // 2, 300), winrate, font=FONT_48, fill="white")

    ## Paste the character icon in the center
    icon = Image.open(f"{CHAR_DIR}{i['name']}_recoloured.png")
    img.paste(icon, (img.width // 2 - icon.width // 2, 85), icon)

    ## Triangle + Pickrate Difference
    triangle = Image.open("apex/negative.png" if pr_diff < 0 else "apex/positive.png")
    diff = f"{pr_diff:.2f}%"
    diff_bbox = draw.textbbox((0, 0), diff, font=FONT_16)
    diff_width = diff_bbox[2] - diff_bbox[0]
    total_width = triangle.width + diff_width
    start_x = (img.width - total_width) / 2

    img.paste(triangle, (int(start_x), 355), triangle)
    start_x += triangle.width
    draw.text((start_x, 352), diff, font=FONT_16, fill="white")

    legend_data[i['name']] = {'image': img, 'pickrate': current_pr}


def generate_atlas(legend_data, sorting_option):
    ## You can sort by pickrate or alphabetically
    if sorting_option == 'pickrate':
        sorted_data = sorted(legend_data.items(), key=lambda x: x[1]['pickrate'], reverse=True)
    else:
        sorted_data = sorted(legend_data.items(), key=lambda x: x[0])

    ## Generate the atlas. 7 columns, X rows. Padding of 16px between each image. Also a border of 32px
    atlas_img = Image.open("apex/pickrate_base.png").convert('RGBA')

    for i, (name, data) in enumerate(sorted_data):
        x = i % 7
        y = i // 7

        ## Calculate the position to paste the image
        x_pos = 32 + x * 272
        y_pos = 32 + y * 400

        atlas_img.alpha_composite(data['image'], (x_pos, y_pos))

    return atlas_img


for sorting_option in ['pickrate', 'alphabetical']:
    atlas = generate_atlas(legend_data, sorting_option)
    atlas.save(f"apex/legend_pickrate_atlas_{sorting_option}.png")
    print(f"Atlas saved as apex/legend_pickrate_atlas_{sorting_option}.png")

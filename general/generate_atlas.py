from PIL import Image
import os

## Add all images in the current directory and subdirectories to a list
# If the image is "large.png", use it. Do not use any other image.
all_files = []
for root, dirs, files in os.walk(input("Enter the directory to generate an atlas for: ")):
    for file in files:
        if file == "icon.png" or file == "awakened_icon.png":
            all_files.append(os.path.join(root, file))

base_x, base_y = Image.open(all_files[0]).size
## Get the rounded up square root of the number of files
square_root = int(len(all_files) ** 0.5) + 1
print(f"Creating atlas with {square_root}x{square_root} images")

## Generate the atlas
atlas = Image.new("RGBA", (base_x * square_root, base_y * square_root))
for i, file in enumerate(all_files):
    atlas.paste(
        Image.open(file),
        (base_x * (i % square_root), base_y * (i // square_root)),
    )
atlas.save("atlas.png", optimize=True)

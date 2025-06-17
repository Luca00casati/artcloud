#!/bin/python3
import os
import shutil
from PIL import Image

header = """
<!doctype html>
<html lang="it">
<head>
<link rel="preload" href="siteres/font/Kredit.otf" as="font" type="font/otf" crossorigin="anonymous">
<link rel="stylesheet" href="style.css" />
<link rel="icon" href="siteres/icon/favicon.svg" type="image/svg+xml" />
<meta charset="UTF-8" />
<meta name="description" content="La Mia Galleria presenta una collezione curata
 di opere d'arte artigianali e creazioni esclusive per amanti dell'estetica e della qualità.">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Galleria delle mie opere artistiche</title>
</head>
<body>
<h1>Galleria delle mie opere artistiche</h1>"""

directory = "opere"
directory_webp = "opere_webp"
dir_files = []
dir_files_webp = []

for filename in os.listdir(directory):
    dir_files.append(filename)

non_png_files = [f for f in dir_files if not f.lower().endswith(".png")]

if non_png_files:
    print("Non PNG file found:")
    print(non_png_files)
    exit(1)

if os.path.exists(directory_webp):
    shutil.rmtree(directory_webp)

os.makedirs(directory_webp)

for filename in os.listdir(directory):
    png_path = os.path.join(directory, filename)

    # Open the image
    with Image.open(png_path) as img:
        # Convert to RGB (to avoid issues with PNGs with transparency)
        img = img.convert("RGB")

        base_name = os.path.splitext(filename)[0]
        webp_path = os.path.join(directory_webp, f"{base_name}.webp")

        img.save(webp_path, "webp")

with open("index.html", "w") as f:
    f.write(header)
    for all in dir_files:
        name_without_ext = os.path.splitext(all)[0]
        f.write(
            f'<img loading="lazy" src="{directory_webp}/{name_without_ext}.webp" alt="{name_without_ext}" />\n'
        )
    f.write("</body>\n</html>")

print("DONE")

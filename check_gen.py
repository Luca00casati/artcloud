#!/bin/python3
import os
from collections import Counter

header = """
<!doctype html>
<html lang="it">
<head>
<link rel="preload" href="siteres/font/Kredit.otf" as="font" type="font/otf" crossorigin="anonymous">
<link rel="stylesheet" href="style.css" />
<link rel="icon" href="siteres/icon/favicon.svg" type="image/svg+xml" />
<meta charset="UTF-8" />
<meta name="description" content="La Mia Galleria presenta una collezione curata di opere d'arte artigianali e creazioni esclusive per amanti dell'estetica e della qualità.">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
"""

link = '''
<nav>
<a href="bello.html">BELLO</a>
<a href="mhe.html">MHE</a>
<a href="brutto.html">BRUTTO</a>
<a href="tutto.html">TUTTO</a>
</nav>
'''

directory = "opere"
directory_avif = "opere_avif"
dir_files = []
dir_files_avif = []

bello_img = [
    "gengar",
    "man",
    "Puccinipaint",
    "charmanderapaint",
    "miku",
    "tauros",
]

brutto_img = [
    "casa1",
    "casa2",
    "casa3",
    "pikachu1",
    "pikachu1color",
    "mew",
    "mewcolors",
]

mhe_img = ["smart", "chr", "focaccina", "bho", "faccia"]

bello_img = [f"{name}.avif" for name in bello_img]
mhe_img = [f"{name}.avif" for name in mhe_img]
brutto_img = [f"{name}.avif" for name in brutto_img]

all_grouped = bello_img + brutto_img + mhe_img
duplicates = [item for item, count in Counter(all_grouped).items() if count > 1]

if duplicates:
    print("Duplicate files found in multiple groups:")
    for d in duplicates:
        print(d)
    exit(1)

# Loop through all files in the directory
for filename in os.listdir(directory):
    dir_files.append(filename)

for filename in os.listdir(directory_avif):
    dir_files_avif.append(filename)

non_png_files = [f for f in dir_files if not f.lower().endswith(".png")]

if non_png_files:
    print("Non PNG file found:")
    print(non_png_files)
    exit(1)

missing_files = [img for img in all_grouped if img not in dir_files_avif]
if missing_files:
    print("missing file:")
    print(missing_files)
    exit(1)

# Combine all categorized files
categorized_files = set(bello_img + brutto_img + mhe_img)

# Filter out categorized files
ungruped_files = [f for f in dir_files_avif if f not in categorized_files]

if ungruped_files:
    print("ungruped file:")
    print(ungruped_files)
    exit(1)

print("CHECK DONE")

with open("tutto.html", "w") as f:
    f.write(header)
    f.write("""<title>Galleria delle mie opere artistiche tutte</title>
    </head>
    <body>
    <h1>Galleria delle mie opere artistiche tutte</h1>""")
    f.write(link)
    for all in all_grouped:
        name_without_ext = os.path.splitext(all)[0]
        f.write(f'<img loading="lazy" src="{directory_avif}/{all}" alt="{name_without_ext}" />\n')
    f.write("</body>\n</html>")

with open("bello.html", "w") as f:
    f.write(header)
    f.write("""
    <title>Galleria delle mie opere artistiche belle</title>
    </head>
    <body>
    <h1>Galleria delle mie opere artistiche belle</h1>""")
    f.write(link)
    for bello in bello_img:
        name_without_ext = os.path.splitext(bello)[0]
        f.write(f'<img loading="lazy" src="{directory_avif}/{bello}" alt="{name_without_ext}" />\n')
    f.write("</body>\n</html>")

with open("mhe.html", "w") as f:
    f.write(header)
    f.write("""
    <title>Galleria delle mie opere artistiche mhe</title>
    </head>
    <body>
    <h1 >Galleria delle mie opere artistiche mhe</h1>""")
    f.write(link)
    for mhe in mhe_img:
        name_without_ext = os.path.splitext(mhe)[0]
        f.write(f'<img loading="lazy" src="{directory_avif}/{mhe}" alt="{name_without_ext}" />\n')
    f.write("</body>\n</html>")

with open("brutto.html", "w") as f:
    f.write(header)
    f.write("""
    <title>Galleria delle mie opere artistiche brutte</title>
    </head>
    <body>
    <h1>Galleria delle mie opere artistiche brutte</h1>""")
    f.write(link)
    for brutto in brutto_img:
        name_without_ext = os.path.splitext(brutto)[0]
        f.write(f'<img loading="lazy" src="{directory_avif}/{brutto}" alt="{name_without_ext}" />\n')
    f.write("</body>\n</html>")

print("DONE GENERATE")
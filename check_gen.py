#!/bin/python3
import os
from collections import Counter

redirect_script = """
    <!-- redirect -->
    <script>
      // If the current path is exactly "/"
      if (window.location.pathname === "/") {
        window.location.replace("/bello.html");
      }
    </script>
"""

header = """
<!doctype html>
<html lang="it">
  <head>
    <script
      src="https://cdn.counter.dev/script.js"
      data-id="6201f173-1697-4253-bf68-83e025b07874"
      data-utcoffset="2"
    ></script>
    <link rel="stylesheet" href="style.css" />
    <link rel="icon" href="siteres/icon/favicon.svg" type="image/svg+xml" />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
"""

directory = "opere"
dir_files = []

bello_img = [
    "gengar.png",
    "man.png",
    "Puccinipaint.png",
    "charmanderapaint.png",
    "miku.png",
    "tauros.png",
]

brutto_img = [
    "casa1.png",
    "casa2.png",
    "casa3.png",
    "pikachu1.png",
    "pikachu1color.png",
    "mew.png",
    "mewcolors.png",
]

mhe_img = ["smart.png", "chr.png", "focaccina.png", "bho.png", "faccia.png"]

all_grouped = bello_img + brutto_img + mhe_img
duplicates = [item for item, count in Counter(all_grouped).items() if count > 1]

if duplicates:
    print("Duplicate files found in multiple groups:")
    for d in duplicates:
        print(d)

# Loop through all files in the directory
for filename in os.listdir(directory):
    dir_files.append(filename)

# Combine all categorized files
categorized_files = set(bello_img + brutto_img + mhe_img)

# Filter out categorized files
ungruped_files = [f for f in dir_files if f not in categorized_files]

if ungruped_files:
    print("ungruped file:")
    print(ungruped_files)

print("CHECK DONE")

with open("index.html", "w") as f:
    f.write(header)
    f.write(redirect_script)
    f.write(
        """
    <title>Galleria delle mie opere artistiche</title>
  </head>

  <body>
    <div class="header">
      <h1 class="overlay-text">Galleria delle mie opere artistiche</h1>
      <a href="bello.html">BELLO</a>
      <a href="mhe.html">MHE</a>
      <a href="brutto.html">BRUTTO</a>
      <a href="index.html">TUTTO</a>
    </div>
    <div class="gallery">
    """
    )
    for all in all_grouped:
        name_without_ext = os.path.splitext(all)[0]
        f.write(f'<img src="{directory}/{all}" alt="{name_without_ext}" />')
    f.write("</div>\n</body>\n</html>")

with open("bello.html", "w") as f:
    f.write(header)
    f.write(
        """
    <title>Galleria delle mie opere artistiche belle</title>
  </head>

  <body>
    <div class="header">
      <h1 class="overlay-text">Galleria delle mie opere artistiche belle</h1>
      <a href="bello.html">BELLO</a>
      <a href="mhe.html">MHE</a>
      <a href="brutto.html">BRUTTO</a>
      <a href="index.html">TUTTO</a>
    </div>
    <div class="gallery">
    """
    )
    for bello in bello_img:
        name_without_ext = os.path.splitext(bello)[0]
        f.write(f'<img src="{directory}/{bello}" alt="{name_without_ext}" />')
    f.write("</div>\n</body>\n</html>")

with open("mhe.html", "w") as f:
    f.write(header)
    f.write(
        """
    <title>Galleria delle mie opere artistiche mhe</title>
  </head>

  <body>
    <div class="header">
      <h1 class="overlay-text">Galleria delle mie opere artistiche mhe</h1>
      <a href="bello.html">BELLO</a>
      <a href="mhe.html">MHE</a>
      <a href="brutto.html">BRUTTO</a>
      <a href="index.html">TUTTO</a>
    </div>
    <div class="gallery">
    """
    )
    for mhe in mhe_img:
        name_without_ext = os.path.splitext(mhe)[0]
        f.write(f'<img src="{directory}/{mhe}" alt="{name_without_ext}" />')
    f.write("</div>\n</body>\n</html>")

with open("brutto.html", "w") as f:
    f.write(header)
    f.write(
        """
    <title>Galleria delle mie opere artistiche brutte</title>
  </head>

  <body>
    <div class="header">
      <h1 class="overlay-text">Galleria delle mie opere artistiche brutte</h1>
      <a href="bello.html">BELLO</a>
      <a href="mhe.html">MHE</a>
      <a href="brutto.html">BRUTTO</a>
      <a href="index.html">TUTTO</a>
    </div>
    <div class="gallery">
    """
    )
    for brutto in brutto_img:
        name_without_ext = os.path.splitext(brutto)[0]
        f.write(f'<img src="{directory}/{brutto}" alt="{name_without_ext}" />')
    f.write("</div>\n</body>\n</html>")

print("DONE GENERATE")
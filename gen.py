#!/bin/python3
import os

header = """
<!doctype html>
<html lang="it">
<head>
<link rel="stylesheet" href="style.css" />
<link rel="icon" href="siteres/icon/favicon.svg" type="image/svg+xml" />
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Galleria</title>
</head>
<body>"""

directory = "opere"
dir_files = []

for filename in os.listdir(directory):
    dir_files.append(filename)

non_png_files = [f for f in dir_files if not f.lower().endswith(".png")]

if non_png_files:
    print("Non PNG file found:")
    print(non_png_files)
    exit(1)

with open("index.html", "w") as f:
    f.write(header)
    for all in dir_files:
        name_without_ext = os.path.splitext(all)[0]
        f.write(
            f'<img loading="lazy" src="{directory}/{name_without_ext}.png" alt="{name_without_ext}" />\n'
        )
    f.write("</body>\n</html>")

print("DONE")

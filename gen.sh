#!/bin/bash

IMG_DIR="opere"
OUT_FILE="index.html"

# Check if image directory exists
if [ ! -d "$IMG_DIR" ]; then
    echo "Error: directory '$IMG_DIR' not found."
    exit 1
fi

# Start HTML
cat > "$OUT_FILE" <<EOF
<!doctype html>
<html lang="it">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="style.css" />
  <link rel="icon" href="siteres/icon/favicon.svg" type="image/svg+xml" />
  <title>la mia galleria</title>
</head>
<body>
EOF

# Loop over all files in the directory (no filtering)
for img in "$IMG_DIR"/*; do
    [ -f "$img" ] || continue  # Skip directories
    filename=$(basename "$img")
    base="${filename%.*}"  # Remove extension for alt
    echo "  <img src=\"$IMG_DIR/$filename\" alt=\"$base\" />" >> "$OUT_FILE"
done

# End HTML
cat >> "$OUT_FILE" <<EOF
</body>
</html>
EOF

echo "DONE: $OUT_FILE generated."


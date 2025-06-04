#!/bin/sh
set -e

mkdir -p opere_avif
for file in opere/*.png; do
  filename=$(basename "$file" .png)
  avifenc "$file" "opere_avif/$filename.avif"
done

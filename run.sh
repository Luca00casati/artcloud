#!/bin/sh
set -e
./convert_avif.sh
python3 check_gen.py
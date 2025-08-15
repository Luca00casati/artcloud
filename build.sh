#!/bin/sh
set -xe
ocamlc main.ml -o gen
./gen

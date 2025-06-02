#!/bin/python3
import os

directory = 'opere'
dir_files = []

bello_img = ['gengar.png',
        'man.png',
        'Puccinipaint.png',
        'charmanderapaint.png',
        'miku.png']

brutto_img = [
    'casa1.png',
        'casa2.png',
        'casa3.png',
       'pikachu1.png',
       'pikachu1color.png',
        'mew.png',
       'mewcolors.png'
]

mhe_img = [
            'smart.png',
        'chr.png',
        'focaccina.png',
        'bho.png',
        'faccia.png'
]

# Loop through all files in the directory
for filename in os.listdir(directory):
    dir_files.append(filename)
    #print(filename)

# Combine all categorized files
categorized_files = set(bello_img + brutto_img + mhe_img)

# Filter out categorized files
ungruped_files = [f for f in dir_files if f not in categorized_files]

if ungruped_files:
    print('ungruped file:')
    print(ungruped_files)

print('DONE')
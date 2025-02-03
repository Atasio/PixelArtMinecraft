#!/bin/env python3

from get_blocks_names import get_blocks_names
from mean_rgb import mean_rgb_from_png
from check_textures import blocks_with_textures_only
from block import Block
from image import Image
from pixel import Pixel
from vecteur import Vecteur
import matplotlib as plt
import numpy as np
import sys


def main():
    imageFilePath = sys.argv[1]
    image = Image.lecture(imageFilePath)
    
    argi = 2
    while (argi < len(sys.argv)):
        match sys.argv[argi]:
            case "-r" | "--resolution":
                length = int(sys.argv[argi+1])
                width = int(sys.argv[argi+2])
                image.changeResolution(length, width)
                argi += 3
            case "-p" | "--point-of-view":
                if (sys.arv[argi + 1] not in ["side", "top", "bottom"]):
                    pov = sys.argv[argi + 1]
                argi += 2
        
    resourcePath = "resource/blocks_textures/"
    blocks_names = get_blocks_names()
    blocks = get_every_blocks(resourcePath, blocks_names)
    newImage = Image(np.empty((16 * image.dim[0], 16 * image.dim[1]), dtype=Pixel))
    i = 0
    j = 0
    for ligne in image.pixels:
        for p in ligne:
            lowest_distance = sys.float_info.max
            fit_block = None
            for b in blocks:
                distance  = Vecteur.distance_entre(p.couleurs, b.mean_rgb_value)
                if (lowest_distance > distance):
                    lowest_distance = distance
                    fit_block = b
            newImage.replace_pixel_by_block(i, j, fit_block)
            j += 1
        i += 1
        j = 0
    
    newImage.show()

def get_every_blocks(directory, blocks_names):
    new_blocks = []
    blocks = blocks_with_textures_only(blocks_names, directory)
    for block_name, block_texture in blocks.items():
        filePath = directory + block_texture + ".png"
        new_blocks.append(Block(block_name, filePath, Image.lecture(filePath).pixels))
    return new_blocks


if __name__ == "__main__":
    main()

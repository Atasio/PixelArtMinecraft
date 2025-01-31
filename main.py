from terminal import *
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
    
    resourcePath = "resource/blocks_textures/"
    blocks_names = get_blocks_names()
    blocks = get_every_blocks(resourcePath, blocks_names)
    
    newImage = np.ndarray()
    for p in image.pixels:
        lowest_distance = sys.maxint
        for b in blocks:
            distance  = p.couleurs.distance_de(b.mean_rgb())
            if (lowest_distance < distance):
                lowest_distance = distance
            
    
    pass

def get_every_blocks(directory, blocks_names):
    new_blocks = []
    blocks = blocks_with_textures_only(blocks_names, directory)
    for block_name, block_texture in blocks.items():
        filePath = directory + block_texture + ".png"
        new_blocks.append(Block(block_name, filePath))


if __name__ == "__main__":
    main()

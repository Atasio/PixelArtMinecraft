#!/bin/env python3

from get_blocks_from_resources import get_blocks_names
from mean_rgb import mean_rgb_from_png
from check_textures import blocks_with_textures_only
from block import Block
from image import Image
from pixel import Pixel
from vecteur import Vecteur
import matplotlib as plt
import numpy as np
import sys
from image_generator import image_generator



def main():
    imageFilePath = sys.argv[1]
    image : Image = Image.lecture(imageFilePath)
    pov = "side"

    argi = 2
    while (argi < len(sys.argv)):
        match sys.argv[argi]:
            case "-r" | "--resolution":
                length = int(sys.argv[argi+1])
                width = int(sys.argv[argi+2])
                image.changeResolution(length, width)
                argi += 3
            case "-p" | "--point-of-view":
                if (sys.argv[argi + 1] in ["side", "top", "bottom"]):
                    pov = sys.argv[argi + 1]
                argi += 2
    
    newImage = image_generator.createPixelArtMinecraft(image, pov)    
    newImage.show()
    




if __name__ == "__main__":
    main()

import sys
from typing import Self
from image import Image
from block import Block
from get_blocks_from_resources import get_blocks_names
from pixel import Pixel
from vecteur import Vecteur
import numpy as np

class image_generator:
    
    def createPixelArtMinecraft(image, pov : str = "side") -> Self :
        resourcePath = "resource/blocks_textures/"
        blocks_names = get_blocks_names()
        blocks = Block.get_every_blocks(resourcePath, blocks_names, pov)
        
        #Transfrom to 0-1 float values if not the case
        if (not isinstance(image.pixels[0][0].couleurs.vals[0], float | np.float16 | np.float32 | np.float64 | np.float128)):
            for i in range(image.pixels.shape[0]):
                for j in range(image.pixels.shape[1]):
                    image.pixels[i,j].couleurs.vals = (image.pixels[i,j].couleurs.vals[0] / 255, image.pixels[i,j].couleurs.vals[1] / 255, image.pixels[i,j].couleurs.vals[2] / 255,)
        
        pixelArtImage = Image(np.empty((16 * image.dim[0], 16 * image.dim[1]), dtype=Pixel))
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
                pixelArtImage.replace_pixel_by_block(i, j, fit_block)
                j += 1
            i += 1
            j = 0
        return pixelArtImage
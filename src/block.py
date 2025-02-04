from image import Image
from check_textures import blocks_with_textures_only
import numpy as np
import os

class Block(Image):

    """Texture d'un block minecraft."""

    def __init__(self, nom: str, texture_path, pixels: np.ndarray = None):
        Image.__init__(self, pixels)
        
        self.texture_path = texture_path
        self.nom = nom
        self.mean_rgb_value = self.mean_rgb()
        
    def __str__(self):
        return self.nom + " " + self.texture_path
    
    def get_every_blocks(directory, blocks_names, pov):
        new_blocks = []
        blocks = blocks_with_textures_only(blocks_names, directory, pov)
        for block_name, block_texture in blocks.items():
            filePath = directory + block_texture + ".png"
            new_blocks.append(Block(block_name, filePath, Image.lecture(filePath).pixels))
        return new_blocks


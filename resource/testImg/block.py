from image import Image
from pixel import Pixel
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


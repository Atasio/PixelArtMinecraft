from image import Image
from pixel import Pixel
import numpy as np
import os

class Block(Image):
    def __init__(self, nom: str, texture_path, pixels: np.ndarray[Pixel] = None):
        if pixels is not None: super(pixels)
        else: super = Image.lecture(texture_path)
        self.texture_path = texture_path
        self.nom = nom
        
    def __str__(self):
        return self.nom + " " + self.texture_path


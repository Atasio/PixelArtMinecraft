from image import Image
from pixel import Pixel
import numpy as np
import os

class Block(Image):
    """Texture d'un block minecraft."""

    RESOURCES_PATH = "./assets/img"

    def __init__(self, nom: str, pixels: np.ndarray[Pixel] = None):
        if pixels is not None: super(pixels)
        else: super = Image.lecture(os.path.join(self.RESOURCES_PATH, nom))
        self.nom = nom


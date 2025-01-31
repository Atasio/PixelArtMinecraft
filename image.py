from typing import List, Self
from pixel import Pixel

from matplotlib.image import imread

import numpy as np

class Image:

    def __init__(self, pixels: np.ndarray):
        self.pixels = pixels
        self.dim = pixels.shape


    def lecture(chemain: str) -> Self:
        raw_image = imread(chemain)
        pixels = np.empty(raw_image.shape, dtype=Pixel)
        for i in range(raw_image.shape[0]):
            for j in range(raw_image.shape[1]):
                pixels[i, j] = Pixel((i, j), raw_image[i, j])
        return Image(pixels)


    def __str__(self):
        return f"Image: dim({self.dim})"


    def __repr__(self):
        return f"Image: dim({self.dim})\n{self.pixels}"


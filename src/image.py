from typing import List, Self
from pixel import Pixel
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
from vecteur import Vecteur

class Image:
    """Représente une image"""

    def __init__(self, pixels: np.ndarray):
        self.pixels = pixels
        self.dim = pixels.shape
        


    def lecture(chemain: str) -> Self:
        """
        Lit l'image et la transforme en tableau de Pixels.
        Permet ensuite de récupérer l'instance de l'image correspondante.

        Args:
            chemain (str): le chemain dans l'arborescence de fichier de l'image à lire.

        Returns:
            Self: l'instance de l'image correspondante
        """
        raw_image = imread(chemain)
        if raw_image.ndim == 2:  # Image en niveaux de gris
        # Répéter la même valeur pour R, G, B
            raw_image = raw_image[:, :, None]  # Ajouter une dimension "RGB"
            raw_image = np.repeat(raw_image, 3, axis=2)  # Répéter pour les 3 canaux RGB
        raw_image = raw_image[:, :, :3]  # Garder seulement les 3 premiers canaux (R, G, B)
        pixels = np.empty((raw_image.shape[0], raw_image.shape[1]), dtype=Pixel)
        for i in range(raw_image.shape[0]):
            for j in range(raw_image.shape[1]):
                pixels[i, j] = Pixel((i, j), Vecteur(*raw_image[i, j]))
        return Image(pixels)

    def mean_rgb(self):
        moyenne = np.array([0.0, 0.0, 0.0])
        for ligne in self.pixels:
            for p in ligne:

                moyenne[0] += p.couleurs.vals[0]
                moyenne[1] += p.couleurs.vals[1]
                moyenne[2] += p.couleurs.vals[2]
        moyenne /= self.pixels.shape[0] * self.pixels.shape[1]
        return Vecteur(*moyenne)
    
    def replace_pixel_by_block(self, i,j, block):
        if (block.pixels.ndim != (16,16)):
            block.pixels = block.pixels[:16,:16]
        self.pixels[(i*16):(i + 1) * 16, (j*16):(j + 1) * 16] = block.pixels
    
    def show(self):
        plt.axis('off')
        tab = []
        for ligne in self.pixels:
            tab.append([])
            for p in ligne:
                tab[-1].append(p.couleurs.vals)
        plt.imshow(tab)
        plt.show()
    
    def changeResolution(self, length, width):
        shape = self.dim
        length0 = shape[0]
        width0 = shape[1]
        ratioL  = length0 / length
        ratioC = width0 / width
        #print("Ratios : ", ratioL, ratioC)
        newImage = np.ndarray(shape=(length, width), dtype=Pixel)
        for row in range(newImage.shape[0]):
            for column in range(newImage.shape[1]):
                newImage[row][column] = self.pixels[(int)(row * ratioL)][(int)(column * ratioC)]
        self.pixels = newImage;
        self.dim = self.pixels.shape
        return self;
        


    def __str__(self):
        return f"Image: dim({self.dim})"


    def __repr__(self):
        return f"Image: dim({self.dim})\n{self.pixels}"


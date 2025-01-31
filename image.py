from typing import List, Self
from pixel import Pixel
from matplotlib.image import imread
import numpy as np

class Image:
    """Représente une image"""

    def __init__(self, pixels: np.ndarray[Pixel]):
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
        if raw_image.ndim == 4:  # RGBA
            raw_image = raw_image[:, :, :3]  # Garder seulement les 3 premiers canaux (R, G, B)
        pixels = np.empty(raw_image.shape, dtype=Pixel)
        for i in range(raw_image.shape[0]):
            for j in range(raw_image.shape[1]):
                pixels[i, j] = Pixel((i, j), raw_image[i, j])
        return Image(pixels)

    def mean_rgb(self):
        moyenne = (0, 0, 0)
        for p in self.pixels:
            moyenne[0] += p.couleurs[0]
        mean_rgb = self.mean(axis=(0, 1))  # Moyenne sur les axes hauteur et largeur
        return mean_rgb


    def __str__(self):
        return f"Image: dim({self.dim})"


    def __repr__(self):
        return f"Image: dim({self.dim})\n{self.pixels}"


import numpy as np
import matplotlib as plt
import matplotlib.pyplot

def mean_rgb_from_png(filePath):
    """
    Calcule la moyenne des valeurs RGB des pixels d'une image PNG.
    
    :param filePath: Chemin du fichier PNG
    :return: Tuple (moyenne_R, moyenne_G, moyenne_B)
    """
    img = matplotlib.pyplot.imread(filePath, "RGB")
    if img.ndim == 2:  # Image en niveaux de gris
        # Répéter la même valeur pour R, G, B
        img = img[:, :, None]  # Ajouter une dimension "RGB"
        img = np.repeat(img, 3, axis=2)  # Répéter pour les 3 canaux RGB
    if img.shape[2] == 4:  # RGBA
        img = img[:, :, :3]  # Garder seulement les 3 premiers canaux (R, G, B)
    mean_rgb = img.mean(axis=(0, 1))  # Moyenne sur les axes hauteur et largeur
        
    return mean_rgb




filePath = "resource/blocks_textures/oak_log.png"
print(mean_rgb_from_png(filePath))
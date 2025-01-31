from vecteur import Vecteur

class Pixel:

    def __init__(self, position: tuple, couleurs: Vecteur):
        self.position = position
        self.couleurs = couleurs


    def __str__(self):
        return f"Pixel({self.position}, {self.couleurs})"


    def __repr__(self):
        return f"Pixel({self.position}, {self.couleurs})"

    
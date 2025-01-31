from typing import Self
from math import sqrt, pow

class Vecteur:
    """Défini un vecteur."""

    def __init__(self, *valeurs):
        self.dim = len(valeurs)
        self.vals = valeurs


    def distance_de(self, vect: Self) -> float:
        """
        Calcule la distance de ce vecteur avec un autre.

        Args:
            vect (Self): le veteur cible

        Raises:
            Exception: si la dimention des deux vecteur n'est pas la même.

        Returns:
            float: la distance de ce vecteur
        """
        return Vecteur.distance_entre(self, vect)


    def distance_entre(a: Self, b: Self) -> float:
        """Calcule la distance entre 2 vecteur

        Args:
            a (Self): le premier vecteur
            b (Self): le second vecteur

        Raises:
            Exception: si la dimention des deux vecteur n'est pas la même.

        Returns:
            float: la distance entre les 2 vecteurs
        """
        if a.dim != b.dim:
            raise Exception("La dimention de a et b doivent être la même.")
        dist = .0
        for v_dim in range(a.dim):
            dist += sqrt(pow(a.vals[v_dim] - b.vals[v_dim], 2))
        return dist


    def __str__(self):
        return f"Vect {self.vals}"

    
    def __repr__(self):
        return f"{self.vals}"

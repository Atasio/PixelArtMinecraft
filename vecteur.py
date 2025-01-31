from typing import Self
from math import sqrt, pow

class Vecteur:

    def __init__(self, *valeurs):
        self.dim = len(valeurs)
        self._l_val = tuple(valeurs)


    def distance_de(self, vect: Self) -> float:
        return Vecteur.distance_entre(self, vect)


    def distance_entre(a: Self, b: Self) -> float:
        if a.dim != b.dim:
            raise Exception("La dimention de a et b doivent être la même.")
        dist = .0
        for v_dim in range(a.dim):
            dist += sqrt(pow(a._l_val[v_dim] - b._l_val[v_dim], 2))
        return dist


    def __str__(self):
        return f"Vect {self._l_val}"

    
    def __repr__(self):
        return f"{self._l_val}"


from abc import ABC, abstractmethod
import math
import unittest


class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} – aire : {self.aire():.2f}"


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


class Triangle(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur


# Extension 1 : Carré
class Carre(Rectangle):
    def __init__(self, cote):
        if cote <= 0:
            raise ValueError("Le côté doit être positif.")
        super().__init__(cote, cote)


# Extension 2 : ColorMixin
class ColorMixin:
    def __init__(self, couleur="blanc"):
        self.couleur = couleur

    def afficher_couleur(self):
        return f"Couleur : {self.couleur}"


class CercleColore(ColorMixin, Cercle):
    def __init__(self, rayon, couleur):
        Cercle.__init__(self, rayon)
        ColorMixin.__init__(self, couleur)

    def __str__(self):
        return f"{super().__str__()} - {self.afficher_couleur()}"


# Extension 3 : Tests unitaires
class TestFormes(unittest.TestCase):

    def test_cercle(self):
        self.assertAlmostEqual(Cercle(3).aire(), 28.2743, places=3)

    def test_rectangle(self):
        self.assertEqual(Rectangle(4, 5).aire(), 20)

    def test_triangle(self):
        self.assertEqual(Triangle(6, 2).aire(), 6)

    def test_carre(self):
        self.assertEqual(Carre(4).aire(), 16)


if __name__ == "__main__":

    formes = [
        Cercle(3),
        Rectangle(4, 5),
        Triangle(6, 2),
        Carre(4)
    ]

    print("=== Les formes ===")
    for forme in formes:
        print(forme)

    print("\n=== Forme colorée ===")
    cercle = CercleColore(3, "rouge")
    print(cercle)

    print("\n=== Tests unitaires ===")
    unittest.main(argv=[""], exit=False)

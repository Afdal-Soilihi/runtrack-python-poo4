import math

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, rayon):
        self.radius = rayon

    def aire(self):
        return math.pi * self.radius**2


# Exemple d'utilisation
rectangle1 = Rectangle(5, 10)
cercle1 = Cercle(3)

resultat_aire_rectangle = rectangle1.aire()
resultat_aire_cercle = cercle1.aire()

print("Aire du rectangle : ", resultat_aire_rectangle)
print("Aire du cercle : ", resultat_aire_cercle)
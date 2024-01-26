class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


# Exemple d'utilisation
rectangle1 = Rectangle(5, 10)
resultat_aire = rectangle1.aire()
print("Aire du rectangle : ", resultat_aire)
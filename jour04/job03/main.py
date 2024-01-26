class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    # Assesseur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.__longueur * self.__largeur * self.__hauteur


# Instanciation de la classe Rectangle
mon_rectangle = Rectangle(5, 8)

# Utilisation des méthodes de la classe Rectangle
print("Périmètre du rectangle :", mon_rectangle.perimetre())
print("Surface du rectangle :", mon_rectangle.surface())

# Modification des attributs avec les mutateurs
mon_rectangle.set_longueur(10)
mon_rectangle.set_largeur(6)

# Affichage des nouvelles valeurs
print("Nouvelle longueur :", mon_rectangle.get_longueur())
print("Nouvelle largeur :", mon_rectangle.get_largeur())

# Instanciation de la classe Parallelepipede
mon_parallelepipede = Parallelepipede(3, 4, 5)

# Utilisation des méthodes de la classe Parallelepipede
print("Volume du parallélépipède :", mon_parallelepipede.volume())
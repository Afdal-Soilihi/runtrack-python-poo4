class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est : {self.age}")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une classe Personne avec l'âge par défaut
personne1 = Personne()
personne1.afficherAge()  # Affiche "L'âge de la personne est : 14"
personne1.bonjour()      # Affiche "Hello"

# Instanciation d'une classe Eleve
eleve1 = Eleve()
eleve1.afficherAge()     # Affiche "J'ai 14 ans"
eleve1.bonjour()         # Affiche "Hello"
eleve1.allerEnCours()    # Affiche "Je vais en cours"

# Instanciation d'une classe Professeur
professeur1 = Professeur(matiereEnseignee="Mathématiques")
professeur1.afficherAge()  # Affiche "L'âge de la personne est : 14"
professeur1.enseigner()    # Affiche "Le cours va commencer"
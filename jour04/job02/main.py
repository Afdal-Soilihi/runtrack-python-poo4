class Personne:
    def __init__(self, age):
        self.age = age

    def bonjour(self):
        print("Hello")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Exemples d'utilisation
eleve1 = Eleve(age=14)
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
eleve1.afficherAge()

professeur1 = Professeur(matiereEnseignee="Informatique", age=40)
professeur1.bonjour()
professeur1.enseigner()
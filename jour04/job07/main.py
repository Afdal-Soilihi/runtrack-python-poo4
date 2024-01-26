import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        return paquet

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        if len(self.paquet) == 0:
            print("Plus de cartes dans le paquet.")
            return None
        carte_tiree = self.paquet.pop()
        return carte_tiree

def calculer_total(main):
    total = 0
    as_present = False

    for carte in main:
        if carte.valeur in ['J', 'Q', 'K']:
            total += 10
        elif carte.valeur == 'A':
            as_present = True
            total += 11
        else:
            total += int(carte.valeur)

    # Gestion des As
    while total > 21 and as_present:
        total -= 10
        as_present = False

    return total

def afficher_main(main, titre):
    print(f"{titre}:")
    for carte in main:
        print(f"   {carte.valeur} de {carte.couleur}")

# Initialisation du jeu
jeu = Jeu()
jeu.melanger_paquet()

# Distribution des cartes
main_joueur = [jeu.tirer_carte(), jeu.tirer_carte()]
main_croupier = [jeu.tirer_carte(), jeu.tirer_carte()]

# Affichage des cartes distribuées
afficher_main(main_joueur, "Main du joueur")
afficher_main(main_croupier, "Main du croupier")

# Tour du joueur
while True:
    choix = input("Voulez-vous prendre une carte (p) ou passer (n) ? ")
    if choix.lower() == 'p':
        nouvelle_carte = jeu.tirer_carte()
        main_joueur.append(nouvelle_carte)
        afficher_main(main_joueur, "Nouvelle main du joueur")
        total_joueur = calculer_total(main_joueur)

        if total_joueur > 21:
            print("Vous avez dépassé 21. Vous perdez.")
            break
    elif choix.lower() == 'n':
        break
    else:
        print("Choix non valide. Veuillez entrer 'p' pour prendre une carte ou 'n' pour passer.")

# Tour du croupier
total_croupier = calculer_total(main_croupier)

while total_croupier < 17:
    nouvelle_carte_croupier = jeu.tirer_carte()
    main_croupier.append(nouvelle_carte_croupier)
    total_croupier = calculer_total(main_croupier)

# Affichage des mains finales
afficher_main(main_joueur, "Main finale du joueur")
afficher_main(main_croupier, "Main finale du croupier")

# Résultat
if total_joueur > 21:
    print("Vous avez dépassé 21. Vous perdez.")
elif total_croupier > 21 or total_joueur > total_croupier:
    print("Vous gagnez !")
elif total_joueur == total_croupier:
    print("Égalité.")
else:
    print("Le croupier gagne.")
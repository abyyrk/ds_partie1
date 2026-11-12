
livres = [
    {
        "id": 1,
        "titre": "Python",
        "auteur": "abyyr",
        "categorie": "Informatique",
        "annee": 2024,
        "total": 3
    },
    {
        "id": 2,
        "titre": "Java",
        "auteur": "rim",
        "categorie": "Informatique",
        "annee": 2023,
        "total": 2
    },
    {
        "id": 3,
        "titre": "Math",
        "auteur": "sami",
        "categorie": "Science",
        "annee": 2022,
        "total": 2
    }
]
def ajouter_livre():
    try:
        id_livre = int(input("ID du livre : "))
    except ValueError:
        print("ID invalide !")
        return

    for livre in livres:
        if livre["id"] == id_livre:
            print("ID deja utilise !")
            return

    titre = input("Titre : ")
    auteur = input("Auteur : ")
    categorie = input("Categorie : ")

    try:
        annee = int(input("Annee : "))
        total = int(input("Nombre d'exemplaires : "))
    except ValueError:
        print("Veuillez entrer un nombre valide !")
        return
    if total < 0:
        print("Quantite invalide !")
        return

    nouveau_livre = {
        "id": id_livre,
        "titre": titre,
        "auteur": auteur,
        "categorie": categorie,
        "annee": annee,
        "total": total
    }

    livres.append(nouveau_livre)
    print("Livre ajoute avec succes !")
def afficher_livres():
    if len(livres) == 0:
        print("Aucun livre disponible")
        return

    print("\n===== LISTE DES LIVRES =====")

    for livre in livres:
        print("------------------------")
        print("ID :", livre["id"])
        print("Titre :", livre["titre"])
        print("Auteur :", livre["auteur"])
        print("Categorie :", livre["categorie"])
        print("Annee :", livre["annee"])
        print("Exemplaires :", livre["total"])

def quitter():
    print("Au revoir !")
while True:
    print("\n================================")
    print("    BIBLIOTHEQUE INTELLIGENTE")
    print("================================")
    print("1. Ajouter un livre")
    print("2. Afficher les livres")
    print("0. Quitter")
    choix = input("\nVotre choix : ")
    if choix == "1":
        ajouter_livre()
    elif choix == "2":
        afficher_livres()
    elif choix == "0":
        quitter()
        break
    else:
        print("Choix invalide")

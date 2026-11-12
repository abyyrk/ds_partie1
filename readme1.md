# Bibliothèque Intelligente

## 1. Présentation du projet

Bibliothèque Intelligente est une application développée en Python qui permet de gérer une liste de livres à travers une interface simple dans le terminal.

Ce projet utilise les notions de base de Python : les variables, les listes, les dictionnaires, les conditions, les boucles et les fonctions.

## 2. Fonctionnalités

L'application propose quatre fonctionnalités principales :

**1. Ajouter un livre**
- Saisir l'identifiant du livre.
- Saisir le titre, l'auteur et la catégorie.
- Indiquer l'année de publication.
- Indiquer le nombre d'exemplaires.
- Vérifier que l'identifiant n'existe pas déjà.
- Refuser une quantité négative.

**2. Afficher les livres**
- Afficher tous les livres enregistrés.
- Afficher leurs informations.
- Afficher un message si la liste est vide.

**3. Rechercher un livre**
- Rechercher un livre par titre.
- Rechercher par auteur.
- Rechercher par catégorie.
- Rechercher par identifiant.

**0. Quitter**
- Fermer le programme avec un message de confirmation.

## 3. Technologies utilisées

- Langage : Python 3
- Éditeur : Visual Studio Code (VS Code)
- Gestion des versions : Git
- Hébergement du code : GitHub

## 4. Structure du projet

```text
Bibliotheque-Intelligente/
│
├── main.py
└── README.md
```

- `main.py` : contient le programme Python.
- `README.md` : contient la documentation du projet.

## 5. Exécution du programme

1. Ouvrir Visual Studio Code.
2. Ouvrir le dossier du projet.
3. Ouvrir le fichier `main.py`.
4. Cliquer sur le bouton **Run Python File**.
5. Le menu principal apparaît dans le terminal.
6. Choisir une option pour utiliser l'application.

## 6. Exemple d'utilisation

```text
================================
    BIBLIOTHEQUE INTELLIGENTE
================================
1. Ajouter un livre
2. Afficher les livres
3. Rechercher un livre
0. Quitter

Votre choix : 1

ID du livre : 4
Titre : Algorithmique
Auteur : Ahmed
Categorie : Informatique
Annee : 2025
Nombre d'exemplaires : 3

Livre ajoute avec succes !
```
## 7. Étapes de réalisation
1. Création du fichier `main.py`.
2. Création de la liste initiale des livres.
3. Développement de la fonction d'ajout.
4. Développement de la fonction d'affichage.
5. Développement de la fonction de recherche.
6. Création du menu principal avec une boucle `while`.
7. Ajout des vérifications pour éviter les erreurs de saisie.
8. Création du fichier `README.md`.
9. Gestion des versions avec Git et publication sur GitHub.
## 8. Gestion du projet avec Git et GitHub
Git permet de suivre les modifications apportées au projet.
Les principales commandes utilisées sont :
- `git init` : initialiser un dépôt Git.
- `git add` : préparer les fichiers pour un commit.
- `git commit` : enregistrer les modifications.
- `git log` : consulter l'historique des commits.
- `git remote -v` : afficher les dépôts distants configurés.
- `git push` : envoyer les modifications sur GitHub.
## 9. Conclusion
Ce projet permet de mettre en pratique les bases de la programmation Python et de découvrir l'utilisation de Git et GitHub pour gérer et partager le code d'une application.

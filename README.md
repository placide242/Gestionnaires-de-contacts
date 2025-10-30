# Gestion des contacts

Petite application CLI en Python pour ajouter et afficher des contacts.

## Description
Programme console simple qui permet de :
- ajouter un contact (nom, prénom, email, téléphone)
- afficher la liste des contacts en mémoire pendant l'exécution

Le code va évoluer ; ce README sera mis à jour au fur et à mesure.

## Prérequis
- Python 3.8+
- Git (pour le versioning)
- (Optionnel) Environnement virtuel pour isoler les dépendances

## Installation / Mise en place
1. Ouvrir VS Code dans le dossier du projet :
   - Fichier → Ouvrir dossier → sélectionne `gestion des contacts`
2. (Optionnel) Créer et activer un venv :
   - PowerShell :
     ```
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Git Bash / CMD :
     ```
     python -m venv venv
     .\venv\Scripts\activate
     ```

## Exécution
Dans le terminal intégré de VS Code (Ctrl+`), exécuter :
```
python main.py
```
Tu verras un menu :
- 1 : ajouter un contact
- 2 : afficher les contacts
- 3 : quitter

Les contacts sont stockés en mémoire durant l'exécution (non persistants).

## Structure du projet
- main.py — code principal de l'application
- README.md — ce fichier
- .gitignore — recommandé pour exclure venv, caches, et .vscode

## À venir / Évolution
- Persistance (CSV / JSON / base de données)
- Édition / suppression de contacts
- Validation des entrées (email, téléphone)
- Tests unitaires
- Interface graphique ou API web

## Contribution
Des modifications sont bienvenues. Mets à jour le README à chaque ajout de fonctionnalité pour documenter l'évolution.

## Licence
À définir.

# Architecture de l'API Todo

## Rôle
L'application est une API REST simple pour gérer une liste de tâches (todo).

## Composants
- **API Flask** : Gère les requêtes HTTP et les routes
- **Base de données SQLite** : Stocke les tâches
- **Tests pytest** : Vérifie le fonctionnement des endpoints

## Données
La base de données contient une table `todo` avec les champs : 
- `id` (entier, clé primaire)
- `task` (chaîne de 100 caractères, obligatoire)
- `done` (booléen, par défaut False)

## Schéma C4
```mermaid
C4Container
    title Architecture de l'API Todo
    PersonYou User
    Container flask Flask Application, "API Todo", "Python"
    Container db SQLite Database, "Todo DB", "SQLite"

    User --> flask: HTTP requests
    flask --> db: Read/Write operations
```
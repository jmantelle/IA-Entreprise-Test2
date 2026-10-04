## Architecture

### Composants
- **API Flask** : Point d'entrée de l'application
- **Liste de todos** : Stockage en mémoire des données
- **Tests unitaires** : Validation des fonctionnalités

### Données
- Les todos sont stockés dans une liste Python en mémoire
- Chaque todo contient : id (entier), title (chaîne), done (booléen)

### Schéma C4
```mermaid
container
  container TodoAPI
    app Flask
    database Liste de todos (mémoire)
  end
  container Test
    test pytest
  end
end
```
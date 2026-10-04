# Todo API

Petite API REST pour gérer une liste de todos.

## Installation

```bash
pip install flask
```

## Lancement

```bash
python app.py
```

## Endpoints

- `GET /todos` : Liste tous les todos
- `POST /todos` : Créer un todo (body: {"title": "..."})
- `GET /todos/<id>` : Obtenir un todo spécifique
- `PUT /todos/<id>` : Mettre à jour un todo
- `DELETE /todos/<id>` : Supprimer un todo
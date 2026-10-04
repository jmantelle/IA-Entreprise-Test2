import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client

def test_create_todo(client):
    response = client.post('/todos', json={'task': 'Test task'})
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['task'] == 'Test task'
    assert data['done'] is False

def test_get_todos(client):
    client.post('/todos', json={'task': 'Task 1'})
    client.post('/todos', json={'task': 'Task 2'})
    response = client.get('/todos')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2

def test_get_todo(client):
    client.post('/todos', json={'task': 'Task 1'})
    response = client.get('/todos/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['task'] == 'Task 1'

def test_update_todo(client):
    client.post('/todos', json={'task': 'Task 1'})
    response = client.put('/todos/1', json={'task': 'Updated task', 'done': True})
    assert response.status_code == 200
    data = response.get_json()
    assert data['task'] == 'Updated task'
    assert data['done'] is True

def test_delete_todo(client):
    client.post('/todos', json={'task': 'Task 1'})
    response = client.delete('/todos/1')
    assert response.status_code == 204
    response = client.get('/todos/1')
    assert response.status_code == 404
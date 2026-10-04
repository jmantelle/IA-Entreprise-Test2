import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.json == []

def test_create_todo(client):
    response = client.post('/todos', json={'title': 'Test todo'})
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['title'] == 'Test todo'
    assert response.json['done'] is False

def test_get_todo(client):
    client.post('/todos', json={'title': 'Test todo'})
    response = client.get('/todos/1')
    assert response.status_code == 200
    assert response.json['title'] == 'Test todo'

def test_update_todo(client):
    client.post('/todos', json={'title': 'Test todo'})
    response = client.put('/todos/1', json={'title': 'Updated todo', 'done': True})
    assert response.status_code == 200
    assert response.json['title'] == 'Updated todo'
    assert response.json['done'] is True

def test_delete_todo(client):
    client.post('/todos', json={'title': 'Test todo'})
    response = client.delete('/todos/1')
    assert response.status_code == 200
    assert response.json['result'] is True
    response = client.get('/todos/1')
    assert response.status_code == 404
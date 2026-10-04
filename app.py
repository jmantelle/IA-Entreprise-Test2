from flask import Flask, jsonify, request
from uuid import uuid4

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = {
        'id': str(uuid4()),
        'title': data['title'],
        'done': False
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo)

@app.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    if 'title' in data:
        todo['title'] = data['title']
    if 'done' in data:
        todo['done'] = data['done']
    
    return jsonify(todo)

@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
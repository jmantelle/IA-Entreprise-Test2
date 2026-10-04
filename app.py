from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db.init_app(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Todo {self.id}>'

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{'id': t.id, 'task': t.task, 'done': t.done} for t in todos])

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = Todo(task=data['task'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'id': new_todo.id, 'task': new_todo.task, 'done': new_todo.done}), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.get_json()
    todo.task = data.get('task', todo.task)
    todo.done = data.get('done', todo.done)
    db.session.commit()
    return jsonify({'id': todo.id, 'task': todo.task, 'done': todo.done})

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204

@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify({'id': todo.id, 'task': todo.task, 'done': todo.done})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
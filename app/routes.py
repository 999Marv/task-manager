from flask import Blueprint, jsonify, request
from .models import Task

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def get_main():
    return jsonify({"message": "hi"}), 200 

@main.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.all()
    return jsonify([task.__dict__ for task in tasks]),200

@main.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task.create(data['title'], data['description'])
    return jsonify(new_task.__dict__), 201

@main.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.find(task_id)
    if task:
        return jsonify(task.__dict__), 200
    return jsonify({"Error": "Task not found"}), 404

@main.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.find(task_id)
    if not task:
        return jsonify({"Error": "Task not found"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    return jsonify(task.__dict__), 200

@main.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    Task.delete(task_id)
    return jsonify({"message": "Task deleted"}), 204

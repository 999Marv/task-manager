from flask import Blueprint, jsonify, request
from .models import Task, tasks

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def get_main():
    return jsonify({"message": "hi"}), 200 

@main.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.__dict__ for task in tasks]),200

@main.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_id = len(tasks) + 1
    new_task = Task(task_id, data['title'], data['description'])
    tasks.append(new_task)
    return jsonify(new_task.__dict__), 201

@main.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)

    if task:
        return jsonify(task.__dict__), 200
    return jsonify({"Error": "Task not found"}), 404
    

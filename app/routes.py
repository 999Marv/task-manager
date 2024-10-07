from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def get_main():
    return jsonify({"message": "hi"}), 200 

@main.route('/tasks', methods=['GET'])
def get_task():
    return jsonify({"tasks": ["Buy fruit", "cook fruit"]}),200
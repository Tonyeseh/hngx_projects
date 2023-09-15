from flask import Flask, jsonify, request
from models import storage
from models.user import User


app = Flask(__name__)

@app.route("/api", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data and not data.get('name', None):
        return {
            "status": "error"
        }, 400
    new_user = User(name=data.get('name'), email=data.get('email', None))
    new_user.save()
    print(new_user.to_dict())
    return jsonify(new_user.to_dict()), 201

@app.route('/api/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(id):
    """manipulate a user with id id"""
    if request.method == "GET":
        result = storage.get(id)
        if result:
            return jsonify(result.to_dict()), 200
        return {
            "status": "error",
            "message": "invalid ID"
        }, 400
    if request.method == "PUT":
        result = storage.get(id)
        if not result:
            return {
            "status": "error",
            "message": "Invalid ID"
        }, 400
        data = request.get_json()
        if data.get('name', None):
            result.name = data.get('name')
        if data.get('email', None):
            result.email = data.get('email')

        result.save()
        return jsonify(result.to_dict())
    if request.method == "DELETE":
        result = storage.get(id)
        if not result:
            return {
            "status": "error",
            "message": "Invalid ID"
        }, 400
        storage.delete(result)
        storage.save()
        return jsonify({})
    

if __name__ == "__main__":
    app.run()
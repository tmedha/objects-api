from flask import Flask, request, jsonify

import service as s

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, API!"

@app.route("/objects", methods=['GET', 'POST', 'DELETE'])
def objects():
    if request.method == "GET":
        objects = s.get_all_objects()
        return jsonify(objects)
    
    if request.method == "POST":
        value = request.get_json()
        id = s.add_object(value)
        return s.get_object(id), 201
    
    if request.method == "DELETE":
        objects = s.get_all_objects()
        s.delete_all_objects()
        return objects
    
    return "Not Allowed", 405

@app.route("/objects/<int:id>", methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def object(id):
    if request.method == 'GET':
        k = s.get_object(id)
        if k is None:
            return "Not Found", 404
        
        return jsonify(k)
    
    if request.method == "PUT":
        value = request.get_json()
        s.place_object(id, value)
        return jsonify(s.get_object(id))
    
    if request.method == 'PATCH':
        partial_value = request.get_json()
        if s.modify_object(id, partial_value):
            return jsonify(s.get_object(id))
        
        return "Not Found", 404
    
    if request.method == 'DELETE':
        deleting = s.get_object(id)
        if s.delete_object(id):
            return jsonify(deleting)
        
        return "Not Found", 404
    
    return "Not Allowed", 405
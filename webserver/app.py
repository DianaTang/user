import json
from flask import Flask
from flask import request, jsonify
from flask.helpers import make_response
from model.person import Person

app = Flask(__name__)

indexCount =0
persons = []

@app.route("/user", methods = ['POST'])
def add_user():
    global indexCount 
    param_values=request.get_json()
    new_person = Person (indexCount, param_values['first_name'], param_values['last_name'], param_values['client_name'],)
    persons.append (new_person)
    indexCount += 1
    return json.dumps(new_person.__dict__)

@app.route ("/user/all")
def find_all():
    json_string = json.dumps([person.__dict__ for person in persons])
    return json_string

@app.route('/user/<int:id>', methods = ['GET'])
def find_user(id):
    for person in persons:
        if person.id == id:
            return json.dumps (person.__dict__)
    res = make_response (jsonify ({"error" : "Person not found"}), 204)
    return res

@app.route('/user/<int:id>', methods = ['DELETE'])
def delete_user(id):
    for person in persons:
        if person.id == id:
            persons.remove(person)
            res = make_response(jsonify({}), 200)
            return res
    res = make_response (jsonify({"error" : "Person not found"}), 204)
    return res

if __name__ == "__main__":
    app.run()

from flask import Flask
from flask import request, jsonify
from flask.helpers import make_response

app = Flask(__name__)

indexCount =0
persons = []

@app.route("/user", methods = ['POST'])
def add_user():
    personsSize = len(persons)
    param_values=request.get_json()
    persons.append ({
        'id': personsSize,
        'first': param_values['first_name'],
        'last' : param_values['last_name'],
        'company' : param_values['client_name']
    })
    global indexCount 
    indexCount += 1
    return jsonify(persons[personsSize])

@app.route('/user/<int:id>', methods = ['GET'])
def find_user(id):
    results = []
    for person in persons:
        if person['id'] == id:
            results.append(person)
    return jsonify(results)

@app.route('/user/<int:id>', methods = ['DELETE'])
def delete_user(id):
    for person in persons:
        if person['id'] == id:
            persons.remove(person)
            res = make_response(jsonify({}), 200)
            return res
    res = make_response (jsonify({"error" : "Person not found"}), 404)
    return res

if __name__ == "__main__":
    app.run()

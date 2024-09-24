from flask import Flask, make_response, request, jsonify
from uuid import UUID
from http import HTTPStatus
import logging

# Initialize Flask app
app = Flask(__name__)

# Sample data
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    }
]

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Create (POST): Add a new person
@app.route("/person", methods=["POST"])
def add_person():
    try:
        new_person = request.get_json()
    except Exception:
        return {"message": "Malformed JSON provided"}, HTTPStatus.BAD_REQUEST

    required_fields = ['id', 'first_name', 'last_name', 'graduation_year', 'address', 'city', 'zip', 'country', 'avatar']
    if not all(field in new_person for field in required_fields):
        return {"message": "Missing fields in input data"}, HTTPStatus.BAD_REQUEST

    # Add the new person to data
    data.append(new_person)
    return {"message": f"Person with ID {new_person['id']} added"}, HTTPStatus.CREATED

# Read (GET): Fetch a person by their UUID
@app.route("/person/<uuid:id>", methods=["GET"])
def get_person(id: UUID):
    person = next((person for person in data if person['id'] == str(id)), None)
    if person:
        return jsonify(person), HTTPStatus.OK
    return {"message": "Person not found"}, HTTPStatus.NOT_FOUND

# Read (GET): Fetch all persons
@app.route("/persons", methods=["GET"])
def get_all_persons():
    if data:
        return jsonify(data), HTTPStatus.OK
    return {"message": "No persons found"}, HTTPStatus.NO_CONTENT

# Update (PUT): Update a person by UUID
@app.route("/person/<uuid:id>", methods=["PUT"])
def update_person(id: UUID):
    updated_data = request.get_json()

    # Find the person by ID
    person_to_update = next((person for person in data if person['id'] == str(id)), None)
    
    if not person_to_update:
        return {"message": "Person not found"}, HTTPStatus.NOT_FOUND

    # Update fields if present in the request
    for key, value in updated_data.items():
        if key in person_to_update:
            person_to_update[key] = value

    return {"message": "Person updated successfully"}, HTTPStatus.OK

# Delete (DELETE): Delete a person by UUID
@app.route("/person/<uuid:id>", methods=["DELETE"])
def delete_person(id: UUID):
    person_to_delete = next((person for person in data if person['id'] == str(id)), None)
    if person_to_delete:
        data.remove(person_to_delete)
        return {"message": "Person deleted successfully"}, HTTPStatus.OK
    return {"message": "Person not found"}, HTTPStatus.NOT_FOUND

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, HTTPStatus.NOT_FOUND

# Run the Flask app on a specific port
if __name__ == "__main__":
    app.run(debug=True, port=5001)

from services import location_service
from flask import jsonify, request, Blueprint


location_blueprint = Blueprint('location_blueprint', __name__)


@location_blueprint.route("/get-locations")
def get_locations():
    data = location_service.get_locations()

    if data is None:
        return {
            "Error": "Inventory location was not found"
        }, 502

    return jsonify(data)

@location_blueprint.route("/create-location-entry", methods=["POST"])
def create_location_entry():
    user_input = request.get_json()
    data = location_service.create_location_entry(user_input)

    if data is None:
        return {
            "Error": "Location was not created"
        }, 502

    return jsonify(data), 201

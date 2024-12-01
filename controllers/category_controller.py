from services import category_service
from flask import Flask, jsonify, request, Blueprint

category_blueprint = Blueprint('category_blueprint', __name__)


@category_blueprint.route("/get-categories/<location_name>")
def get_categories(location_name):
    data = category_service.get_categories(location_name)

    if data is None:
        return {
            "Error": "Location was not found"
        }, 502

    return jsonify(data)

@category_blueprint.route("/create-category-entry", methods=["POST"])
def create_category_entry():
    user_input = request.get_json()
    data = category_service.create_category_entry(user_input)

    if data is None:
        return {
            "Error": "Category was not created"
        }, 502

    return jsonify(data), 201


# GET: Get all categories by location ID
# POST: Creates a category, needs to take in the location ID

# {
#   LocationName = "CourtneysHouse"
#   CategoryName = "Bathroom"
# }



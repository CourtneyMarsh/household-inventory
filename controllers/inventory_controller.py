from services import inventory_service
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/get-categories/<category_name>")
def get_categories(category_name):
    data = inventory_service.get_categories(category_name)

    if data is None:
        return {
            "Error": "Category was not found"
        }, 502

    return jsonify(data)


@app.route("/get-categories/<category_name>/<inventory>")
def get_inventory(category_name, inventory):
    data = inventory_service.get_inventory(category_name, inventory)

    if data is None:
        return {
            "Error": "Inventory was not found"
        }, 502

    return jsonify(data)


@app.route("/get-categories/<category_name>/<inventory>/<item>")
def get_inventory_item(category_name, inventory, item):
    data = inventory_service.get_inventory_item(category_name, inventory, item)

    if data is None:
        return {
            "Error": "Item was not found"
        }, 502

    return jsonify(data)


@app.route("/create-category-entry", methods=["POST"])
def create_category_entry():
    user_input = request.get_json()
    data = inventory_service.create_category_entry(user_input["CategoryTitle"])

    if data is None:
        return {
            "Error": "Category was not created"
        }, 502

    return jsonify(data), 201

@app.route("/create-item-entry", methods=["POST"])
def create_item_entry():
    user_input = request.get_json()
    data = inventory_service.create_item_entry(user_input["CategoryTitle"], user_input["ItemName"])

    if data is None:
        return {
            "Error": "Item was not added"
        }, 502

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
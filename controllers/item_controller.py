from services import location_service
from flask import Flask, jsonify, request

app = Flask(__name__)


# all items get call for inventory under locations
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
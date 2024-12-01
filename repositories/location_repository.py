import datetime
import firebase_admin
from firebase_admin import credentials


fake_database_inventory = {
    "Inventory": {
        "CourtneysHouse": {
            "Fridge": {
                "Milk": {
                    "Quantity": 1,
                    "PurchasedDate": datetime.date.today(),
                    "ExpirationDate": "Tomorrow"
                }
            },
            "Freezer": {
                "PizzaRolls": {
                    "Quantity": 1,
                    "PurchasedDate": datetime.date.today(),
                    "ExpirationDate": None
                }
            }
        }
    }
}

# Your collection is inventory
# Your document is "Courtneys House" or whatever
# Your document contents fridge, pantry, etc


def get_inventory(category_name, inventory):
    return fake_database_inventory[category_name][inventory]


def get_inventory_item(category_name, inventory, item):
    return fake_database_inventory[category_name][inventory][item]



if __name__ == "__main__":

    cred = credentials.Certificate("path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)


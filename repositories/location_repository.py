import datetime


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

def get_locations():
    data = fake_database_inventory["Inventory"]
    locations = []
    for location in data.keys():
        locations.append(location)

    return locations

def create_location_entry(location_name):
    fake_database_inventory["Inventory"][location_name] = {}
    return get_locations()






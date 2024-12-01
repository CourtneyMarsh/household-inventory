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


def get_categories(location_name):
    data = fake_database_inventory["Inventory"][location_name]
    categories = []
    for category in data.keys():
        categories.append(category)

    return categories

def create_category_entry(location_name, category_name):
    fake_database_inventory["Inventory"][location_name][category_name] = {}
    return get_categories(location_name)


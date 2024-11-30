from repositories.inventory_repository import fake_database_inventory


def validate_category_exists_in_database(category_name):
    if fake_database_inventory.get(category_name):
        return True
    else:
        return False
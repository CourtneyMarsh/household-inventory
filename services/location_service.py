from repositories import location_repository
from utils.validation_util import validate_category_exists_in_database


def get_inventory(category_name, inventory):
    if not validate_category_exists_in_database(category_name):
        return None

    return inventory_repository.get_inventory(category_name, inventory)


def get_inventory_item(category_name, inventory, item):
    if not validate_category_exists_in_database(category_name):
        return None

    return inventory.get_inventory_item(category_name, inventory, item)


def create_item_entry(category_title, item_name):
    if not validate_category_exists_in_database(category_name):
        return None

    return inventory_repository.create_item_entry(category_title, item_name)

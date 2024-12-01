from repositories import category_repository
from utils.validation_util import validate_category_exists_in_database

def get_categories(location_name):
    # if not validate_category_exists_in_database(category_name):
    #     return None
    return category_repository.get_categories(location_name)

def create_category_entry(user_input):
    # if not validate_category_exists_in_database(category_name):
    #     return None
    return category_repository.create_category_entry(user_input["LocationName"], user_input["CategoryName"])


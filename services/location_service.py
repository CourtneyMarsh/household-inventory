from repositories import location_repository
from utils.validation_util import validate_category_exists_in_database

def get_locations():
    # if not validate_location_exists_in_database(location_name):
    #     return None
    return location_repository.get_locations()

def create_location_entry(user_input):
    # if not validate_location_exists_in_database(location_name):
    #     return None
    return location_repository.create_location_entry(user_input["LocationName"])





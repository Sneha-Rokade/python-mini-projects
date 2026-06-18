import json
from utils.logger import log_error

FILE_PATH = "data/contacts.json"

def load_contacts():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        log_error(f"Error loading contacts: {e}")
        return []

def save_contacts(contacts):
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(contacts, file, indent=4)
    except Exception as e:
        log_error(f"Error saving contacts: {e}")
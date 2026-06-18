from utils.file_handler import load_contacts, save_contacts
from utils.logger import log_info
from services.validation_service import is_valid_email, is_valid_phone


def contact_exists(contacts, name):
    return any(contact["name"].lower() == name.lower() for contact in contacts)


def add_contact():
    contacts = load_contacts()

    name = input("Enter Name: ")

    if contact_exists(contacts, name):
        print("Contact already exists!")
        return

    while True:
        phone = input("Enter Phone: ")
        if is_valid_phone(phone):
            break
        print("Invalid Phone Number")

    while True:
        email = input("Enter Email: ")
        if is_valid_email(email):
            break
        print("Invalid Email")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    log_info(f"Added contact: {name}")
    print("Contact added successfully!")


def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("No contacts found")
        return

    for contact in contacts:
        print(contact)


def search_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(contact)
            return

    print("Contact not found")


def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ")

    new_contacts = [
        c for c in contacts if c["name"].lower() != name.lower()
    ]

    if len(new_contacts) == len(contacts):
        print("Contact not found")
    else:
        save_contacts(new_contacts)
        log_info(f"Deleted contact: {name}")
        print("Contact deleted")
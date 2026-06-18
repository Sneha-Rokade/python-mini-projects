from utils.file_handler import load_contacts, save_contacts
from utils.logger import log_info
from services.validation_service import is_valid_email, is_valid_phone


def contact_exists(contacts, name):
    return any(contact["name"].lower() == name.lower() for contact in contacts)


def add_contact():
    try:
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

    except Exception as e:
        print("Something went wrong while adding contact")
        log_error(f"Add error: {e}")


def view_contacts():
    try:
        contacts = load_contacts()

        if not contacts:
            print("No contacts found")
            return

        page_size = 5

        for i in range(0, len(contacts), page_size):
            chunk = contacts[i:i + page_size]

            for contact in chunk:
                print(contact)

            if i + page_size < len(contacts):
                input("\nPress Enter to see more...")

    except Exception as e:
        print("Error viewing contacts")
        log_error(f"View error: {e}")


def search_contact():
    
    try:

        contacts = load_contacts()
        name = input("Enter name to search: ")

        results = [
            contact for contact in contacts
            if name in contact["name"].lower()
        ]

        if results:
            for contact in results:
                print(contact)
        
        else:
            print("No matching contacts found")

    except Exception as e:
         print("Error while searching")
         log_error(f"Search error: {e}")


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

def update_contact():
    try:
        contacts = load_contacts()
        name = input("Enter name to update: ").lower()

        for contact in contacts:
            if contact["name"].lower() == name:

                print("Leave blank if no change")

                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")

                if new_phone:
                    if is_valid_phone(new_phone):
                        contact["phone"] = new_phone
                    else:
                        print("Invalid phone, skipping")

                if new_email:
                    if is_valid_email(new_email):
                        contact["email"] = new_email
                    else:
                        print("Invalid email, skipping")

                save_contacts(contacts)
                log_info(f"Updated contact: {name}")

                print("Contact updated successfully!")
                return

        print("Contact not found")

    except Exception as e:
        print("Error updating contact")
        log_error(f"Update error: {e}")
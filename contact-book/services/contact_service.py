from utils.file_handler import load_contacts, save_contacts
from utils.logger import log_error, log_info
from services.validation_service import is_valid_email, is_valid_phone
from utils.ui import print_contact


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
                print_contact(contact)

            if i + page_size < len(contacts):
                input("\nPress Enter to see more...")

    except Exception as e:
        print("Error viewing contacts")
        log_error(f"View error: {e}")


def search_contact():
    
    try:

        contacts = load_contacts()
        name = input("Enter name to search: ").lower()

        results = [
            contact for contact in contacts
            if name in contact["name"].lower()
        ]

        if results:
            for contact in results:
                print_contact(contact)
        
        else:
            print("No matching contacts found")

    except Exception as e:
         print("Error while searching")
         log_error(f"Search error: {e}")


def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ")

    found = False
    for c in contacts:
        if c["name"].lower() == name.lower():
            found = True
            break
    
    if not found:
        print("Contact not Found")
        return
    
    confirm = input("Are you sure you want to delete? (yes/no): ").lower()

    if confirm != "yes":
        print("Deletion Cancelled!")
        return
    
    new_contacts = [
        c for c in contacts if c["name"].lower() != name.lower()
    ]

    save_contacts(new_contacts)
    log_info(f"Deleted contact: {name}")
    print("Contact deleted successfully!")


def update_contact():
    try:
        contacts = load_contacts()
        name = input("Enter name to update: ").lower()

        for contact in contacts:
            if contact["name"].lower() == name.lower():

                print("\nCurrent Details:")
                print_contact(contact)

                confirm = input("Do you want to update this contact? (yes/no): ").lower()
                if confirm not in ["yes", "y"]:
                    print("Update Cancelled!")
                    return

                new_phone = input("Enter new phone: ").strip()
                while not is_valid_phone(new_phone):
                    print("Invalid phone! Please try again")
                    new_phone = input("Enter new phone: ").strip()

                new_email = input("Enter new email: ").strip()
                while not is_valid_email(new_email):
                    print("Invalid Email Address! Please try again")
                    new_email = input("Enter new email: ").strip()

                contact["phone"] = new_phone
                contact["email"] = new_email

                save_contacts(contacts)
                log_info(f"Updated contact: {name}")

                print("Contact updated successfully!")
                return

        print("Contact not found")

    except Exception as e:
        print("Error updating contact")
        log_error(f"Update error: {e}")
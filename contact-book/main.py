import json

def load_contacts():

    with open(
        "contact.json",
        "r"
    ) as file:

        contacts = json.load(file)

    return contacts

def save_contacts(contacts):
    
    with open(
        "contact.json",
        "w"
    ) as file:
        
        json.dump(
            contacts,
            file,
            indent=4
        )

def add_contacts(contacts):
    
    name = input(
        "Enter Name: "
    )

    phone = input(
        "Enter Phone: "
    )

    email = input(
        "Enter Email: "
    )

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    save_contacts(contacts)

    print("Contact Added Successfully!")

def view_contacts(contacts):
    
    if len(contacts) == 0:

        print("No Contacts Found")

        return
    
    for contact in contacts:

        print("\n------------------------------")

        print(
            f"Name : {contact['name']}"
        )

        print(
            f"Phone : {contact['phone']}"
        )

        print(
            f"Email : {contact['email']}"
        )

        print("---------------------------------")

def search_contacts(contacts):
    
    search_name = input("Enter Name To seaarch : ")

    for contact in contacts:

        if (
            contact["name"].lower()
            ==
            search_name.lower()
        ):
            
            print("\n Contact Found")

            print(
                f"Name  : {contact['name']}"
            )

            print(
                f"Phone : {contact['phone']}"
            )

            print(
                f"Email : {contact['email']}"
            )

            return

    print("Contact Not Found")
        

def update_contacts(contacts):
    
    search_name = input("Enter name to update data : ")

    for contact in contacts:

        if(
            contact["name"].lower()
            ==
            search_name.lower()
        ):
            
            new_phone = input(
                "Enter new Phone : "
            )

            new_email = input(
                "Enter new Email : "
            )

            contact["phone"] = new_phone

            contact["email"] = new_email

            save_contacts(
                contacts
            )

            print(
                "Contact Updated Successfully"
            )

            return
        
    print(
        "Contact Not Found"
    )

def delete_contacts(contacts):
    
    search_name = input(
        "Enter Name to Delete the contact : "
    )

    for contact in contacts:

        if (
            contact["name"].lower()
            ==
            search_name.lower()
        ):
            
            contacts.remove(contact)

            save_contacts(contacts)

            print(
                "Contact deleted successfully!"
            )

            return
        
    print(
        "Contact not Found"
    )

def main():

    contacts = load_contacts()

    # add_contacts(contacts)

    # view_contacts(contacts)

    # search_contacts(contacts)

    # update_contacts(contacts)

    # delete_contacts(contacts)

    # contacts = [
    #     {
    #         "name": "Alex",
    #         "phone": "9595959595",
    #         "email": "alex@gmail.com"
    #     }
    # ]

    # save_contacts(contacts)

    # print("Saved Successfully")

    while True:

        print("\n=======Contact Book==========")

        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input(
            "Enter Choice: "
        )

        if choice == "1":

            add_contacts(contacts)

        elif choice == "2":

            view_contacts(contacts)

        elif choice == "3":

            search_contacts(contacts)

        elif choice == "4":

            update_contacts(contacts)

        elif choice == "5":

            delete_contacts(contacts)

        elif choice == "6":

            print(
                "Thank You!"
            )

            break

        else:

            print("Invalid Choice")



if __name__ == "__main__":
    main()
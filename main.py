from address_book import AddressBook
from contact import Contact
from validate import get_valid_input

address_book_name = input("Enter the address book name: ")
address_book = AddressBook(address_book_name)

while True:
    print("\nOptions:\n1. Add Contact\n2. Edit Contact\n3. Delete Contact\n4. Show Contacts\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        first_name = get_valid_input("Enter the first name: ", "name")  
        last_name = get_valid_input("Enter the last name: ", "name")  
        address = get_valid_input("Enter the address: ", "address")  
        city = get_valid_input("Enter the city: ", "city_state")  
        state = get_valid_input("Enter the state: ", "city_state")  
        zip_code = get_valid_input("Enter the zip code: ", "zip")  
        phone_number = get_valid_input("Enter the phone number: ", "phone")  
        email_id = get_valid_input("Enter the email ID: ", "email")  

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email_id)
        address_book.addContact(contact)
        print("Contact added successfully!")

    elif choice == "2":
        name_to_edit = input("Enter the first or last name of the contact to edit: ")
        contact = address_book.findContact(name_to_edit)

        if contact:
            print(f"Editing contact: {contact}")

            contact.first_name = get_valid_input("Enter new first name: ", "name")
            contact.last_name = get_valid_input("Enter new last name: ", "name")
            contact.address = get_valid_input("Enter new address: ", "address")
            contact.city = get_valid_input("Enter new city: ", "city_state")
            contact.state = get_valid_input("Enter new state: ", "city_state")
            contact.zip_code = get_valid_input("Enter new zip code: ", "zip")
            contact.phone_number = get_valid_input("Enter new phone number: ", "phone")
            contact.email_id = get_valid_input("Enter new email ID: ", "email")

            print("Contact updated successfully!")
        else:
            print(f"Contact with name '{name_to_edit}' not found.")

    elif choice == "3":
        name_to_delete = input("Enter the first or last name of the contact to delete: ")
        address_book.deleteContact(name_to_delete)

    elif choice == "4":
        address_book.getContacts()

    elif choice == "5":
        print("Exiting the Address Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
from address_book_main import AddressBookSearch
from validate import get_valid_input
from contact import Contact

if __name__ == "__main__":
    address_book_search = AddressBookSearch()
    while True:
        print("\nMain Menu:")
        print("1. Create New Address Book")
        print("2. Select Address Book")
        print("3. Show All Address Books")
        print("4. Delete Address Book")
        print("5. Search Person by City/State")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            address_book_search.createAddressBook()

        elif choice == "2":
            selected_book = address_book_search.selectAddressBook()
            if selected_book:
                while True:
                    print(f"\nManaging Address Book: {selected_book.address_book_name}")
                    print("1. Add Contact")
                    print("2. Edit Contact")
                    print("3. Delete Contact")
                    print("4. Show Contacts")
                    print("5. Back to Main Menu")

                    sub_choice = input("Enter your choice: ").strip()

                    if sub_choice == "1":  # Add Contact
                        while True:
                            first_name = get_valid_input("Enter the first name: ", "name")  
                            last_name = get_valid_input("Enter the last name: ", "name")  
                            address = get_valid_input("Enter the address: ", "address")  
                            city = get_valid_input("Enter the city: ", "city_state")  
                            state = get_valid_input("Enter the state: ", "city_state")  
                            zip_code = get_valid_input("Enter the zip code: ", "zip")  
                            phone_number = get_valid_input("Enter the phone number: ", "phone")  
                            email_id = get_valid_input("Enter the email ID: ", "email")  

                            contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email_id)
                            selected_book.addContact(contact)

                            more = input("Do you want to add another contact? (yes/no): ").strip().lower()
                            if more != "yes":
                                break

                    elif sub_choice == "2":  # Edit Contact
                        name_to_edit = input("Enter the first or last name of the contact to edit: ").strip()
                        selected_book.editContact(name_to_edit)

                    elif sub_choice == "3":  # Delete Contact
                        name_to_delete = input("Enter the first or last name of the contact to delete: ").strip()
                        selected_book.deleteContact(name_to_delete)

                    elif sub_choice == "4":  # Show Contacts
                        selected_book.getContacts()

                    elif sub_choice == "5":  # Back to Main Menu
                        break

                    else:
                        print("Invalid choice! Please enter a valid option.")

        elif choice == "3":
            address_book_search.showAllAddressBooks()

        elif choice == "4":
            address_book_search.deleteAddressBook()

        elif choice == "5":  # Search Person by City/State
            while True:
                search_type = input("Search by (city/state): ").strip().lower()
                if search_type in ["city", "state"]:
                    break  
                print("Error: Invalid choice! Please enter 'city' or 'state'.")

            location = input(f"Enter the {search_type} name: ").strip()
            if not location:  
                print("Error: Please enter a valid location name.")
            else:
                address_book_search.searchPersonByCityOrState(location, search_type)

        elif choice == "6":
            print("Exiting Address Book System. Goodbye.")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

from address_book import AddressBook
from contact import Contact
from validate import get_valid_input

class AddressBookMain:
    def __init__(self):
        self.address_books = {}

    def createAddressBook(self):
        address_book_name = input("Enter a name for the new address book: ")

        if address_book_name in self.address_books:
            print("Address book with this name already exists! Try another name.")
        else:
            self.address_books[address_book_name] = AddressBook(address_book_name)
            print(f"Address book '{address_book_name}' created successfully!")

    def selectAddressBook(self):
        if not self.address_books:
            print("No address books available! Create one first.")
            return None

        print("Available Address Books:", ", ".join(self.address_books.keys()))
        selected_name = input("Enter the name of the address book to manage: ")

        return self.address_books.get(selected_name, None)

    def deleteAddressBook(self):
        if not self.address_books:
            print("No address books available to delete.")
            return

        print("Available Address Books:", ", ".join(self.address_books.keys()))
        selected_name = input("Enter the name of the address book to delete: ")

        if selected_name in self.address_books:
            del self.address_books[selected_name]
            print(f"Address book '{selected_name}' deleted successfully!")
        else:
            print(f"Address book '{selected_name}' not found.")

    def showAllAddressBooks(self):
        if not self.address_books:
            print("No address books found.")
        else:
            print("\nExisting Address Books:")
            for book_name in self.address_books:
                print(f"- {book_name}")

    def manageAddressBook(self, address_book):
        while True:
            print(f"\nManaging Address Book: {address_book.address_book_name}")
            print("1. Add Contact")
            print("2. Edit Contact")
            print("3. Delete Contact")
            print("4. Show Contacts")
            print("5. Back to Main Menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
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
                    address_book.addContact(contact)

                    more = input("Do you want to add another contact? (yes/no): ").lower()
                    if more != "yes":
                        break

            elif sub_choice == "2":
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

            elif sub_choice == "3":
                name_to_delete = input("Enter the first or last name of the contact to delete: ")
                address_book.deleteContact(name_to_delete)

            elif sub_choice == "4":
                address_book.getContacts()

            elif sub_choice == "5":
                break

            else:
                print("Invalid choice! Please enter a valid option.")

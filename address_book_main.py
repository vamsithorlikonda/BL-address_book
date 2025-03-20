from address_book import AddressBook

class AddressBookMain:
    def __init__(self):
        self.address_books = {}  # Dictionary to store multiple address books

    def createAddressBook(self):
        """Creates a new Address Book with a unique name"""
        address_book_name = input("Enter a unique name for the new address book: ").strip()

        if address_book_name in self.address_books:
            print("Error: Address book with this name already exists! Try another name.")
        else:
            self.address_books[address_book_name] = AddressBook(address_book_name)
            print(f"Address book '{address_book_name}' created successfully.")

    def selectAddressBook(self):
        """Allows user to select an existing Address Book"""
        if not self.address_books:
            print("No address books available! Create one first.")
            return None

        print("\nAvailable Address Books:", ", ".join(self.address_books.keys()))
        selected_name = input("Enter the name of the address book to manage: ").strip()

        if selected_name in self.address_books:
            return self.address_books[selected_name]
        else:
            print(f"Error: Address book '{selected_name}' not found.")
            return None

    def deleteAddressBook(self):
        """Deletes an Address Book"""
        if not self.address_books:
            print("No address books available to delete.")
            return

        print("\nAvailable Address Books:", ", ".join(self.address_books.keys()))
        selected_name = input("Enter the name of the address book to delete: ").strip()

        if selected_name in self.address_books:
            del self.address_books[selected_name]
            print(f"Address book '{selected_name}' deleted successfully.")
        else:
            print(f"Error: Address book '{selected_name}' not found.")

    def showAllAddressBooks(self):
        """Displays all Address Books"""
        if not self.address_books:
            print("No address books found.")
        else:
            print("\nExisting Address Books:")
            for book_name in self.address_books:
                print(f"- {book_name}")

class AddressBookSearch(AddressBookMain):
    """Subclass of AddressBookMain that handles searching by City or State"""

    def searchPersonByCityOrState(self, location, search_type):
        """ Search for persons by city or state across all Address Books """
        found_contacts = {}  # Dictionary {city/state: [contact objects]}
        
        for book_name, address_book in self.address_books.items():
            for contact in address_book.contacts:
                key = contact.city.lower() if search_type == "city" else contact.state.lower()

                if key not in found_contacts:
                    found_contacts[key] = []
                found_contacts[key].append((book_name, contact))  # Store the full contact object

        # Display the results
        if location.lower() in found_contacts:
            print(f"\nPeople found in {location}:")
            for book_name, contact in found_contacts[location.lower()]:
                print(f"\nAddress Book: {book_name}")
                print(contact)  # Contact object will call its __str__() method
        else:
            print(f"No contacts found in '{location}'.")
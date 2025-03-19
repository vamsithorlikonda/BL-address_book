from address_book import AddressBook

class AddressBookMain:
    def __init__(self):
        self.address_books = {}  # Dictionary to store multiple address books

    def createAddressBook(self):
        address_book_name = input("Enter a unique name for the new address book: ")

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
            del self.address_books[selected_name]  # Remove the address book from the dictionary
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
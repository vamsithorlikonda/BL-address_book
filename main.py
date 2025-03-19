from address_book_main import AddressBookMain

if __name__ == "__main__":
    address_book_main = AddressBookMain()

    while True:
        print("\nMain Menu:")
        print("1. Create New Address Book")
        print("2. Select Address Book")
        print("3. Show All Address Books")
        print("4. Delete Address Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            address_book_main.createAddressBook()

        elif choice == "2":
            selected_book = address_book_main.selectAddressBook()
            if selected_book:
                address_book_main.manageAddressBook(selected_book)

        elif choice == "3":
            address_book_main.showAllAddressBooks()

        elif choice == "4":
            address_book_main.deleteAddressBook()

        elif choice == "5":
            print("Exiting Address Book System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

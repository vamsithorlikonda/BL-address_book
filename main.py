from address_book import AddressBook
from contact import Contact
from validate import get_valid_input

address_book_name = input("Enter the address book name: ")
address_book = AddressBook(address_book_name)

while True:
    try:
        n = int(input("Enter the number of contacts for the address book: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
i=1
while n:
    print(f"Enter the values for the contact {i}:")

    first_name = get_valid_input("Enter the first name: ", "name")  # Name validation
    last_name = get_valid_input("Enter the last name: ", "name")  # Name validation
    address = get_valid_input("Enter the address: ", "address")  # Address validation
    city = get_valid_input("Enter the city: ", "city_state")  # City validation
    state = get_valid_input("Enter the state: ", "city_state")  # State validation
    zip_code = get_valid_input("Enter the zip code: ", "zip")  # Zip validation
    phone_number = get_valid_input("Enter the phone number: ", "phone")  # Phone validation
    email_id = get_valid_input("Enter the email ID: ", "email")  # Email validation

    contact = Contact(
        first_name, last_name, address, city, state, zip_code, phone_number, email_id
    )
    address_book.addContact(contact)
    n -= 1  # Decrement n
    i+=1

print(address_book.getContacts())

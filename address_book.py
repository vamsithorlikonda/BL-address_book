class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contacts = []  # Using a list instead of a dictionary

    def addContact(self, contact_obj):
        self.contacts.append(contact_obj)

    def getContacts(self):
        print(f"\nWELCOME TO {self.address_book_name} ADDRESS BOOK")
        if not self.contacts:
            print("No contacts found.")
        for contact in self.contacts:
            print(contact)

    def findContact(self, name):
        for contact in self.contacts:
            if contact.first_name.lower() == name.lower() or contact.last_name.lower() == name.lower():
                return contact
        return None  # If no contact is found

    def deleteContact(self, name):
        contact_to_delete = self.findContact(name)
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact with name '{name}' not found.")
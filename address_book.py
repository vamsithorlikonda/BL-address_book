class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contacts = []

    def addContact(self, contact_obj):
        """ Adds a contact if it doesn't already exist """
        for contact in self.contacts:
            if (contact.first_name.lower() == contact_obj.first_name.lower() and 
               contact.last_name.lower() == contact_obj.last_name.lower()):
                print(f"Error: Contact '{contact_obj.first_name} {contact_obj.last_name}' already exists!")
                return
        self.contacts.append(contact_obj)
        print(f"Contact {contact_obj.first_name} {contact_obj.last_name} added successfully!")

    def getContacts(self):
        """ Displays all contacts in the Address Book """
        print(f"\nWELCOME TO {self.address_book_name} ADDRESS BOOK")
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def findContact(self, name):
        """ Finds a contact by first or last name """
        for contact in self.contacts:
            if contact.first_name.lower() == name.lower() or contact.last_name.lower() == name.lower():
                return contact
        return None

    def editContact(self, name, updated_contact):
        """ Edits an existing contact """
        for index, contact in enumerate(self.contacts):
            if contact.first_name.lower() == name.lower() or contact.last_name.lower() == name.lower():
                self.contacts[index] = updated_contact
                print(f"Contact '{name}' updated successfully!")
                return
        print(f"Contact with name '{name}' not found.")

    def deleteContact(self, name):
        """ Deletes a contact by first or last name """
        contact_to_delete = self.findContact(name)
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact with name '{name}' not found.")

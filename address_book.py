import os
import json
from contact import Contact  # Importing the Contact class

class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contacts = []
        self.file_name = f"{self.address_book_name}.json"  # JSON file for storing contacts
        self.read_from_json()  # Load contacts from JSON file if it exists

    def addContact(self, contact_obj):
        """ Adds a contact and writes it to the JSON file """
        for contact in self.contacts:
            if (contact.first_name.lower() == contact_obj.first_name.lower() and 
               contact.last_name.lower() == contact_obj.last_name.lower()):
                print(f"Error: Contact '{contact_obj.first_name} {contact_obj.last_name}' already exists!")
                return

        self.contacts.append(contact_obj)
        self.write_to_json()
        print(f"Contact {contact_obj.first_name} {contact_obj.last_name} added successfully!")

    def write_to_json(self):
        """ Writes all contacts to a JSON file """
        with open(self.file_name, mode="w") as file:
            json.dump([vars(contact) for contact in self.contacts], file, indent=4)

    def read_from_json(self):
        """ Reads contacts from a JSON file and loads them into the Address Book """
        if os.path.exists(self.file_name):
            with open(self.file_name, mode="r") as file:
                contacts_list = json.load(file)
                for data in contacts_list:
                    contact = Contact(**data)  # Create Contact object from dictionary
                    self.contacts.append(contact)

    def sortContacts(self, sort_by="name"):
        """ Sorts contacts based on the given criteria: name, city, state, or zip """
        if not self.contacts:
            print("No contacts available to sort.")
            return
        if sort_by == "name":
            self.contacts = sorted(self.contacts, key=lambda contact: (contact.first_name.lower(), contact.last_name.lower()))
        elif sort_by == "city":
            self.contacts = sorted(self.contacts, key=lambda contact: contact.city.lower())
        elif sort_by == "state":
            self.contacts = sorted(self.contacts, key=lambda contact: contact.state.lower())
        elif sort_by == "zip":
            self.contacts = sorted(self.contacts, key=lambda contact: contact.zip_code)

        self.write_to_json()  # Save sorted contacts to JSON file

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
        """ Edits an existing contact and updates the JSON file """
        for index, contact in enumerate(self.contacts):
            if contact.first_name.lower() == name.lower() or contact.last_name.lower() == name.lower():
                self.contacts[index] = updated_contact
                self.write_to_json()
                print(f"Contact '{name}' updated successfully!")
                return
        print(f"Contact with name '{name}' not found.")

    def deleteContact(self, name):
        """ Deletes a contact by first or last name and updates the JSON file """
        contact_to_delete = self.findContact(name)
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            self.write_to_json()
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact with name '{name}' not found.")

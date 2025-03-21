import os
import csv
from contact import Contact

class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contacts = []
        self.file_name = f"{self.address_book_name}.csv"
        self.read_from_csv()

    def addContact(self, contact_obj):
        """ Adds a contact and writes it to the CSV file """
        for contact in self.contacts:
            if (contact.first_name.lower() == contact_obj.first_name.lower() and 
               contact.last_name.lower() == contact_obj.last_name.lower()):
                print(f"Contact '{contact_obj.first_name} {contact_obj.last_name}' already exists!")
                return

        self.contacts.append(contact_obj)
        self.write_to_csv()
        print(f"Contact {contact_obj.first_name} {contact_obj.last_name} added successfully!")

    def write_to_csv(self):
        """ Writes all contacts to a CSV file """
        with open(self.file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Address", "City", "State", "Zip Code", "Phone Number", "Email ID"])  # Header
            for contact in self.contacts:
                writer.writerow([contact.first_name, contact.last_name, contact.address, contact.city,
                                 contact.state, contact.zip_code, contact.phone_number, contact.email_id])

    def read_from_csv(self):
        """ Reads contacts from a CSV file and loads them into the Address Book """
        if os.path.exists(self.file_name):
            with open(self.file_name, mode="r") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if len(row) == 8:
                        first_name, last_name, address, city, state, zip_code, phone_number, email_id = row
                        contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email_id)
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

        self.write_to_csv()  # Save sorted contacts to CSV file

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
        """ Edits an existing contact and updates the CSV file """
        for index, contact in enumerate(self.contacts):
            if contact.first_name.lower() == name.lower() or contact.last_name.lower() == name.lower():
                self.contacts[index] = updated_contact
                self.write_to_csv()
                print(f"Contact '{name}' updated successfully!")
                return
        print(f"Contact with name '{name}' not found.")

    def deleteContact(self, name):
        """ Deletes a contact by first or last name and updates the CSV file """
        contact_to_delete = self.findContact(name)
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            self.write_to_csv()
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact with name '{name}' not found.")

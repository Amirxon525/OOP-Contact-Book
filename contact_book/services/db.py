import json
from contact_book.models.contact import Contact


class DB:

    def __init__(self, filename='data/contacts.json'):
        self.filename = filename
        self.contacts: list[Contact] = []

    def load_contacts(self):
        with open(self.filename) as jsonfile:
            data_list = json.load(jsonfile)

        self.contacts: list[Contact] = []
        for data in data_list:
            self.contacts.append(Contact.from_dict(data))

    def save_contacts(self):
        data = []
        for contact in self.contacts:
            data.append(contact.to_dict())

        with open(self.filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    def add_contact(self, name, phone, email):
        self.load_contacts()
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()

    def get_contacts(self):
        self.load_contacts()
        return self.contacts
    
    def get_contact(self, contact_id: str) -> dict | None:
        self.load_contacts()
        for contact in self.contacts:
            if contact_id == contact.contact_id:
                return contact

    def update_contact(self, contact: Contact, data: dict):
        for item in self.contacts:
            if contact.contact_id == item.contact_id:
                item.name = data.get("name")
                item.phone = data.get("phone")
                item.email = data.get("email")

        self.save_contacts()

    def remove_contact(self, contact_id: str) -> bool:
        contact = self.get_contact(contact_id)

        if contact:
            self.contacts.remove(contact)
            self.save_contacts()
            return True
        else:
            return False

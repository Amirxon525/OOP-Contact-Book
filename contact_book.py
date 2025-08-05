import json
from rich.console import Console
from rich.table import Table
from contact import Contact


class ContactBook:

    def __init__(self):
        self.console = Console()
        self.contacts: list[Contact] = []

    def load_contacts(self):
        with open('contacts.json') as jsonfile:
            data_list = json.load(jsonfile)

        for data in data_list:
            self.contacts.append(Contact.from_dict(data))

    def save_contacts(self):
        data = []
        for contact in self.contacts:
            data.append(contact.to_dict())

        with open('contacts.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    def print_menu(self):
        self.console.print('[bold italic yellow on red blink]\n======== Menu ========')
        self.console.print(
            '1. Add New Contact\n'
            '2. Show All Contacts\n'
            '3. Search Contact\n'
            '4. Update Contact\n'
            '5. Delete Contact\n'
            '6. Exit\n'
        )

    def add_contact(self):
        self.console.print("[bold green]Enter A New Contact Information")
        name = input("Name: ").strip().title()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()

        self.load_contacts()
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()

    def print_contacts(self):
        table = Table(title="[bold blue]Contacts Table")

        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Phone", justify="right", style="green")
        table.add_column("Email", style="blue")

        self.load_contacts()
        for contact in self.contacts:
            table.add_row(
                contact.contact_id,
                contact.name,
                contact.phone,
                contact.email
            )

        self.console.print(table)

    def remove_contact(self):
        self.print_contacts()

        contact_id = input("Contact ID: ")
        if self.db.remove_contact(contact_id):
            print("contact ochirildi")
        else:
            print("bunday contact mavjud emas")


    def update_contact(self):
        self.print_contacts()

        contact_id = input("Contact ID: ")
        contact = self.db.get_contact(contact_id)
        if contact:
            name = input("Name: ").strip().title()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()

            data = {
                'name': name,
                'phone': phone,
                'email': email
            }
            self.db.update_contact(contact, data)
            print("Contact Update qilindi.")
        else:
            print("Bunday ID dagi contact mavjud emas.")

    def search_contact(self):
        search = input("Search: ").strip().lower()
        
        table = Table(title="[bold blue]Found Contacts Table")

        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        table.add_column("Phone", justify="right", style="green")
        table.add_column("Email", style="blue")


    def run(self):
        print("salom, Contact Book Projectga Xush Kelibsiz!")
        while True:
            self.print_menu()

            choice = input("> ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.print_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.remove_contact()
            elif choice == '6':
                self.quit()
            else:
                print("xato choice")


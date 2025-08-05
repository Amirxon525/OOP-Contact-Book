# import json
# from contact import Contact


# contact = Contact(name='Vali', phone="991231212", email="vali@gmail.com")
# print(contact.contact_id)


# with open('contacts.json') as jsonfile:
#     data_list = json.load(jsonfile)

# contacts: list[Contact] = []
# for data in data_list:
#     contacts.append(Contact.from_dict(data))

# for contact in contacts:
#     print(contact.to_dict())



from rich.console import Console


c = Console()

c.print("[bold italic yellow on red blink]This text is impossible to read")
c.print("[bold red]alert![/bold red] Something happened")
c.print("[bold red]Bold and red[/] not bold or red")
c.print("[bold]Bold[italic] bold and italic [/bold]italic[/italic]")

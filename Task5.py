class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_contact.name
                contact.phone = new_contact.phone
                contact.email = new_contact.email
                contact.address = new_contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("Search Results:")
                for i, result in enumerate(results, start=1):
                    print(f"{i}. Name: {result.name}, Phone: {result.phone}")
            else:
                print("No contacts found.")

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            new_contact = Contact(new_name, phone, email, address)
            contact_book.update_contact(name, new_contact)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
import json

class ContactsManager():
    def __init__(self,filename=r"basic_details.js"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        with open(self.filename, 'r') as file:
            return json.load(file)
        
    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent = 4)
        
    def view_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone number: {contact['phone']}, email: {contact['email']}")
        else:
            print("No contacts availble")

    def add_contacts(self, name, phone, email):
        new_contact = {
            "name" : name,
            "phone" : phone,
            "email" : email
        }
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f"Added {name} to contacts")

    def search_contacts(self,name):
        found = [contact for contact in self.contacts if contact['name'].lower() == name.lower()]
        if found:
            for contact in found:
                print(f"Found {contact['name']} details: phone number {contact['phone']} email {contact['email']}")
        else:
            print(f"No contacts found in this {name}")

    def delete_contacts(self,name):
        self.contacts = [contact for contact in self.contacts if contact['name'] != name]
        self.save_contacts()
        print(f"Deleted contact: {name}")

def main():
    manager = ContactsManager()
    while True:
        print("Contacts Manager:\n")
        print("1. Add contacts\n")
        print("2. View contacts\n")
        print("3. Delete contact\n")
        print("4. Search contact\n")
        print("5. Exit\n")
        choice = int(input("Choose an option (1/2/3/4/5): "))
        if choice == 1:
            name = input("Enter your name: ")
            phone = input("Enter your phone: ")
            email = input("Enter your email: ")
            manager.add_contacts(name,phone,email)
        elif choice == 2:
            manager.view_contacts()
        elif choice == 3:
            delete_contact = input("Enter contact name to delete: ")
            manager.delete_contacts(delete_contact)
        elif choice == 4:
            search_inp = input("Enter the name to search in the contacts: ")
            manager.search_contacts(search_inp)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Enter valid choice")
            exit
   
if __name__ == "__main__":
    main()

contact={}

def menu():
    print("<----- Contact Book Menu ----->")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
def add_contact():
    print("--- Add New Contact ---")
    name=input("Enter Name:")
    phone = input("Enter phone Number:")
    email = input("Enter Email:")
    contact[name]={'phone':phone,'email':email}
    print(f'Contact {name} added successfully.')
    
def view_contact():
    print("--- Contact List ---")
    if not contact:
        print("No contacts available.")
    else:
        for name, details in contact.items():
            print(f"Name: {name}, phone: {details['phone']}, Email: {details['email']}")
            
def search_contact():
    print("--- Search Contact ---")
    name=input("Enter Name to search:")
    if name in contact:
        details=contact[name]
        print(f"Name: {name}, phone: {details['phone']}, Email: {details['email']}")
    else:
        print("Contact not found.")
def edit_contact():
    print("--- Edit Contact ---")
    name=input("Enter Name to edit:")
    if name in contact:
        phone = input("Enter new phone Number:")
        email = input("Enter new Email:")
        contact[name]={'phone':phone,'email':email}
        print(f'Contact {name} updated successfully.')
    else:
        print("Contact not found.")
        
def delete_contact():
    print("--- Delete Contact ---")
    name=input("Enter Name to delete:")
    if name in contact:
        del contact[name]
        print(f'Contact {name} deleted successfully.')
    else:
        print("Contact not found.")

menu()    
while True:
    choice = input("Enter your choice (1-6): ")
    match choice:
        case '1':
            add_contact()
        case '2':
            view_contact()
        case '3':
            search_contact()
        case '4':
            edit_contact()
        case '5':
            delete_contact()
        case '6':
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")
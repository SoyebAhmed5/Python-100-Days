FILE_NAME = "myNotes.txt"

def show_menu():
    print("""<--- Note Taking Application --->
1. Add Note
2. View Notes
3. Delete Notes
4. Exit""")
    
def add_note():
    print("--- Add New Note ---")
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")
    
def view_note():
    try:
        with open(FILE_NAME,"r") as file:
            note = file.read()
            if not note:
                print("No Notes is found")
            else:
                print("--- Your Notes ---")
                print(note)
    except FileNotFoundError:
        print("No Notes is found")
        
def delete_note():
    confirm= input("Are you sure you want to delete all notes? (yes/no): ")
    if confirm.lower() == 'yes':
        with open(FILE_NAME, "w") as file:
            pass
        print("All notes deleted successfully.")
    else:
        print("Delete operation cancelled.")      
        
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")
    match choice:
        case '1':
            add_note()
        case '2':
            view_note()
        case '3':
            delete_note()
        case '4':
            print("Exiting the application. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")      
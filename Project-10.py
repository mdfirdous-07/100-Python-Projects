#  Note-Taking App

#  step1:- Define the file name
FILE_NAME="myNotes.txt"

# step2:- Display menu options 
def show_menu():
    print("\n ---- Notes Taking App Menu---\n")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")
    
# Step3:- Add a new note
def add_note():
    note= input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note added sucessfully")
    
# step4:- View all notes
def view_note():
    try :
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content:
                print("\n -- Your Notes---\n")
                print(content)
            else:
                print("\n No notes found ")
    except FileNotFoundError:
        print("No notes found")
        
# step5:- Delete all notes
def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (yes/no): ").strip()
    if confirm == "yes":
        with open(FILE_NAME, "w") as file:
            file.truncate(0)   # file empty kar dega
        print("All notes deleted successfully.")
    else:
        print("Deletion cancelled")
        
#  step 6:- Main program loop

while True:
    show_menu()
    choice=input("Enter your choice (1-4): ").strip()
    
    if choice=="1":
        add_note()
    elif choice=="2":
        view_note()
    elif choice=="3":
        delete_notes()
    elif choice=="4":
        print("Exiting Note-Taking App. Goodbye! ")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4") 
    
    

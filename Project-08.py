 # Contact Book
 
 # step1:- Intialize an empty contact book
contacts = {}

#step2:- Display the Menu
def show_menu():
    print("\n--- Contact Book Menu ---\n ") 
    print("1. Add Contacts")
    print("2. View Contacts")
    print("3. Search contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit ")
    
# step3:- Add a contact
def add_contact():
    name=input("Enter contact name: ")
    phone=input("Enter contact number:")
    email=input("Enter contact email: ")
    contacts[name] = {"phone":phone, "email":email}
    print(f"contact {name} has been added to your contact book successfully")

#step4:- View all contacts
def view_contact():
    if contacts:
        print("\n--- Contact list ---\n ")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("Your contact book is empty.")
#step5:- Search a contact
def search_contact():
    name=input("Enter the name of the contact you want to search: ")
    if name in contacts:
        print(f"\n---- Contact Details for {name}  -----\n")
        print(f"phone: {contacts[name]['phone']}")
        print(f"email:{contacts[name]['email']}")
    else:
        print(f"Contact {name} not found in your contact book")
        
#step6:- Edit a contact
def edit_contact():
    name=input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        phone=input("Enter new phone number: ")
        email=input("Enter the new email: ")
        contacts[name]={"phone":phone, "email":email}
        print(f"Contact {name} has been updated successfully")
    else:
        print(f"Contact {name} not found in your contact book.")   

# step7:- Delete a contact
def delete_contact():
    name=input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted successfully")
    else:
        print(f"Contact {name} not found in your contact book.")   

#step8:  Main program loop
while True:
    show_menu()
    choice= input("Enter your choice (1-6): ").strip()
    
    if choice=="1":
        add_contact()
    elif choice=="2":
        view_contact()
    elif choice=="3":
        search_contact()
    elif choice=="4":
        edit_contact()
    elif choice=="5":
        delete_contact()
    elif choice=="6":
        print("thankyou for using the Contact Book. Goodbye! ")
        break
    else:
        print("Invalid choice. please select a valid option (1-6).")  
        
        

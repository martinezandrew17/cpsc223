# Import Contacts Module

import contacts

def display_menu():
    print("\n*** TUFFY TITAN CONTACT MAIN MENU")
    print("1. Print List")
    print("2. Add Contact")
    print("3. Modify Contact")
    print("4. Delete Contact")
    print("5. Exit the Program")

def main():
    # List
    contact_list = []

    while True: 
        display_menu()
        try: 
            choice = int(input("\nEnter menu choice: "))
            if choice == 1:
                contacts.print_list(contact_list)
            elif choice == 2:
                contact_list = contacts.add_contacts(contact_list)
            elif choice == 3:
                contact_list = contacts.modify_contact(contact_list)
            elif choice == 4: 
                contact_list = contacts.delete_contacts(contact_list)
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Running
            
if __name__ == "__main__":
    main()

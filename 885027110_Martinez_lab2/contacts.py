# Andrew Martinez
# February 05, 2024
# The purpuse of this file is to store the contact list 
# functions and use it in the main driver file. 

def print_list(contacts):
    if not contacts: 
        print("\nThe contact list is empty.")
        return
    print("==================CONTACT LIST==================")
    print(f'{"Index":<8}{"First Name":<22}{"Last Name":<22}') # Spacing Purposes
    print ("====== ==================== ====================")
    for index, contact in enumerate(contacts):
        print(f'{index:<8}{contact[0]:<22}{contact[1]:<22}')

def add_contacts(contacts):
    first_name = input("Enter first name: ")
    last_name = input("Enter Last Name: ")
    contacts.append([first_name, last_name])
    print(f"Contact, {first_name} {last_name} added successfully.")
    return contacts

def modify_contact(contacts):
    try: 
        index = int(input("Enter the Index of the Contact to Modify: "))
        if 0 <= index < len(contacts):
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            contacts[index] = [first_name, last_name]
            print(f'Contact and index {index} updated successfully.')
        else:
            print("Invalid index number.")
    except ValueError:
        print("Invalid input. Please input a valid index.")
    return contacts

def delete_contacts(contacts):
    try: 
        index = int(input("Enter the Index of the Contact to Delete: "))
        if 0 <= index < len(contacts):
            deleted_contacts = contacts.pop(index)
            print(f"Contact'{deleted_contacts[0]}, {deleted_contacts[1]} deleted successfully.")  
        else:
            print("Invalid index number.")      
    except ValueError:
        print("Invalid input. Please input a valid index.")
    return contacts


import json

def content_of_file():
    try:
        with open("example.txt","r") as file:
            return json.load(file)
    except:
        return {}


def save_to_file(directory):
    with open("example.txt","w") as file:
        json.dump(directory, file, indent = 4)
        
directory = content_of_file()


print("\n Telephone Directory Menu ")
print(' ',"*"*22,'')
print("1. Add contact")
print("2. Update contact ")
print("3. Delete contact")
print("4. Search contact")
print("5. Display all contact")
print("6. Clear all contacts")
print("7. Exit")
while True:
    print('\n',"_"*20,'\n')
    choice = input("Enter the choice:")
   
    if choice == '1':
        name = input("Enter name to add ").strip().upper()
        if name in directory:
            print("\nName already exist!")
        else:
            phone = input("Enter the phone number:").strip()
            directory[name] = phone
            save_to_file(directory)
            print(f"contact of {name} is added succesfully!")
    
    elif choice == '2':
         name = input("Enter name to update ").strip().upper()
         if name in directory:
            phone = input("Enter the phone number:").strip()
            directory[name] = phone
            save_to_file(directory)
            print(f"Contact {name} updated successfully.")
         else:
            print("Contact not found!")
           
    elif choice == '3':
        name = input("Enter name to delete ").strip().upper()
        if name in directory:
            del directory[name]
            save_to_file(directory)
            print(f"Contact {name} deleted succesfully.")
        else:
            print("Contact not found")
            
    elif choice == '4':
        name = input("Enter name for searching ").strip().upper()
        if name in directory:
            print(f"{name}:{directory[name]}")
        else:
            print(name,"not found")
            
    elif choice == '5':
        if directory:
            print("\n----- All Contacts ------\n")
            for name,phone in directory.items():
                print(f"{name}: {phone}")
        else:
            print("Directory is empty.")
            
    elif choice == '6':
        with open("example.txt","w") as file:
            pass
        directory.clear()
        print("All data cleared successfully")


    elif choice == '7':
        print("Exiting program....GoodBye!")
        break

    else:
        print("Invalid choice! please enter a number between 1 and 6")
    
             
        
            
        
        
         
             
                
        
            
        
        
    

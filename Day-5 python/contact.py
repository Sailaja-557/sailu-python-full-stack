#function
def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    with open("./bb.txt", "a") as file:
            data= file.write(f"name {name} : mobile {mobile}\n")
            return data
    file.close()

def view_contacts(contacts):
    print("\n")
    for i in contacts:
        print(f"{i} : {contacts[i]}")
    with open("./bb.txt", "r") as file:
        data = file.readlines()
        return data 
    file.close()
        
def delete_contact(contacts):
    name_to_delete = input("Enter contact name to delete :")
    del contacts[name_to_delete]
    print("deleted contact " , name_to_delete)
    with open("./bb.txt", "a") as file:
            data = file.write(f"\ndelete name : {name_to_delete}")
            return data
    file.close()

def find_contact(contacts):
    name_to_find = input("Enter name to Find :")
    print(f"{name_to_find} : {contacts[name_to_find]}")
    with open("./bb.txt", "a") as file:
            data = file.write(f"\n find name is : {name_to_find}")
            return data
    file.close()

def edit_contact(contacts):
    name_to_edit = input("Enter contact name to edit :")
    number = int(input("Enter new number: "))
    contacts[name_to_edit] = number
    print("Edited contact : " , name_to_edit)
    with open("./bb.txt", "a") as file:
            data = file.write(f"\nedit nmae is : {name_to_edit}")
            return data
    file.close()
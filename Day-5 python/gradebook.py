def add_student(gradebooks):
    name =  input("Enter student name:")
    marks = input("Enter student marks with spaces:")
    mark_list = list(map(int,marks.split(" ")))
    gradebooks[name]=mark_list

def view_student(gradebooks):
    print("\n")
    for i in gradebooks:
        # for name,marks in gradebooks.item():
        #     avg=sum(marks)/len(marks)
        print(f"{i} : {gradebooks[i]}")

def search_student(gradebooks):
    name_to_search = input("Enter name to Find :")
    print(f"{name_to_search} : {gradebooks[name_to_search]}")

def update_student(gradebooks):
    name = input("Enter student name to update marks: ")
    if name in gradebooks:
        marks = input("Enter new marks separated by spaces: ")
        mark_list = list(map(int, marks.split()))
        gradebooks[name] = mark_list
        print(f"{name}'s marks updated.")
    else:
        print("Student not found.")

def remove_student(gradebooks):
    name = input("Enter student name to remove: ")
    if name in gradebooks:
        del gradebooks[name]
        print(f"{name} removed from gradebook.")
    else:
        print("Student not found.")
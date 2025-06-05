import gradebook as gh
gradebooks={}
print("\tStudent Gradebook Management System")

while True:
    try:
        print("\nChoices available:")
        print("1. add_student")
        print("2. view_student")
        print("3. search_student")
        print("4. update_student")
        print("5. remove_student")
        print("6.exit")

        choice = int(input("Enter choice : "))
        if choice==1:
            gh.add_student(gradebooks)
        elif choice==2:
            gh.view_student(gradebooks)
        elif choice==3:
            gh.search_student(gradebooks)
        elif choice==4:
            gh.update_student(gradebooks)
        elif choice==5:
            gh.remove_student(gradebooks)
        elif choice==6:
            print("completed")
            break
        else: 
            print("Invaild choice")
    except Exception as e:
        print(f"error is =  {e}")
    finally:
        print("grade book is done")
    
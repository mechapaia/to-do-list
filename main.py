from tdlfunc import *

# main program loop
try:
    while True:
        print("\n---------To-Do-List---------")
        print("\n0. Create File\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice=input("Enter option: ")
        if choice == '0':
            p=input("Are you sure? (This action will create a new file and erase all existing data from any previous file) (y/n): ")
            if p.lower()=="y":
                createFile()
                
        elif choice == '1':
            viewTasks()
        elif choice == '2':
            addTask()
        elif choice == '3':
            removeTask()
        elif choice == '4':
            print("Thank you for using this program!")
            break
        else:
            print("\nInvalid option.")

except:
    print("Error: Please reopen the program.")
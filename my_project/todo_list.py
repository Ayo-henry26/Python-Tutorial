todo_list = []

def add_task():
    task = input("Input a new task: ")
    todo_list.append({"Task": task, "Status": "Pending"})
    print("New Task Successfully Added\n")


def view_task():
    print("*** To Do List ***")
    if len(todo_list) == 0:
        print("No pending task\n")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task['Task']} - {task['Status']}")


def remove_task():
    if len(todo_list) == 0:
        print("To Do List is Empty\n")
    else:
        try:
            search_index = int(input("Enter the task number you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                remove_task = todo_list.pop(search_index)
                print(f"Removed Task: {remove_task['Task']}")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Please enter a valid task number")


def mark_done():
    if len(todo_list) == 0:
        print("To Do List is Empty\n")
    else:
        try:
            search_index = int(input("Enter the task number you want mark as completed: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = "Completed"
                print(f"The task to {todo_list[search_index]['Task']} has been completed")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Please enter a valid task number")


def menu():
    while True:
        print("*** Main Menu ***")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove task")
        print("4. Mark task as read")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application.....")
            exit()
        else:
            print("Invalid choice, Try Again")

menu()
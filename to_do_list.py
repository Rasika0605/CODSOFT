# Simple To-Do List Application

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks):
            status = "✔" if task["done"] else "✘"
            print(f"{i+1}. [{status}] {task['task']}")

def add_task():
    task_name = input("Enter new task: ")
    tasks.append({"task": task_name, "done": False})
    print("Task added successfully!")

def mark_complete():
    show_tasks()
    try:
        task_no = int(input("Enter task number to mark complete: "))
        tasks[task_no-1]["done"] = True
        print("Task marked as completed!")
    except:
        print("Invalid task number!")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no-1)
        print("Task deleted successfully!")
    except:
        print("Invalid task number!")

while True:
    print("\n---- TO-DO LIST MENU ----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
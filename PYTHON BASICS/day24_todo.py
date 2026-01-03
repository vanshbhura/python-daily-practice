# Day 24: To-Do List (CLI)
# Topics:
# lists, functions, loops, user interaction

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added.")

def delete_task():
    show_tasks()
    if tasks:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number.")

while True:
    print("\n--- TO DO MENU ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting To-Do App.")
        break
    else:
        print("Invalid choice. Try again.")

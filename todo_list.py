def display_menu():
 print("\nTo-Do List Menu")
 print("1. Add Task")
 print("2. Delete Task")
 print("3. View Tasks")
 print("4. Exit")
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
def delete_task(tasks):
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")
def view_tasks(tasks):
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please choose again.")
if __name__ == "__main__":
    main()
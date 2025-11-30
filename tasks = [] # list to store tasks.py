tasks = []  # list to store tasks

while True:
    print("\n--- To Do List Menu ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Enter a task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the number of the task to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed}' deleted!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose between 1 to 4.")
def main():
    todo_list = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.append({"task": task, "done": False})
            print("Task added successfully!")

        elif choice == "2":
            if todo_list:
                print("\nYour To-Do List:")
                for index, item in enumerate(todo_list, start=1):
                    status = "Done" if item["done"] else "Not Done"
                    print(f"{index}. {item['task']} - [{status}]")
            else:
                print("Your to-do list is empty!")

        elif choice == "3":
            if todo_list:
                print("\nYour To-Do List:")
                for index, item in enumerate(todo_list, start=1):
                    print(f"{index}. {item['task']}")
                task_number = int(input("Enter the task number to mark as done: "))
                if 1 <= task_number <= len(todo_list):
                    todo_list[task_number - 1]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number!")
            else:
                print("Your to-do list is empty!")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

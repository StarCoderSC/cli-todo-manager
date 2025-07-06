import os

TASK_FILE = "tasks.txt"

# Load task from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

# Save tak to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n TO-DO Manager")
    print("1. View Task")
    print("2. Add Task")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Quit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            if not tasks:
                print("\nNo tasks yet!")
            else:
                print("\n Current Task(s)...")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter new task.")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added ✅")
        
        elif choice == "3":
            if not tasks:
                print("no tasks yet!")
                continue
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            idx = int(input("Enter task number to mark done: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx] = tasks[idx] + "✅"
                save_tasks(tasks)
                print("Task mark done")
            
            else:
                print("Invalid task number!")

        elif choice == "4":
            if not tasks:
                print("No task to delete!")
                continue
            
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            idx = int(input("Enter task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                save_tasks(tasks)
                print(f"Deleted: {removed}")
            
            else:
                print("Invalid task number!")
        
        elif choice == "5":
            print("\n Goodbye! \n")
            break

        else:
            print("Invalid choice!")

if __name__=="__main__":
    main()


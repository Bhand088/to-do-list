
TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!\n")
    else:
        print("⚠️ Empty task not added.\n")

def complete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to mark as done: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                save_tasks(tasks)
                print(f"✅ Completed & removed: '{removed}'\n")
            else:
                print("❌ Invalid number.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()

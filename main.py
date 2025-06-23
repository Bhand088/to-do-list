# simple todo list

tasks_file = "tasks.txt"

def read_tasks():
    try:
        with open(tasks_file, "r") as f:
            lines = f.readlines()
            tasks = [line.strip() for line in lines]
    except:
        tasks = []
    return tasks

def write_tasks(tasks):
    with open(tasks_file, "w") as f:
        for t in tasks:
            f.write(t + "\n")

# main loop
print("Todo List")
tasks = read_tasks()

while True:
    print("\n1. View")
    print("2. Add")
    print("3. Done")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        if not tasks:
            print("No tasks.")
        else:
            for i in range(len(tasks)):
                print(i+1, "-", tasks[i])
    elif choice == "2":
        new_task = input("Task: ").strip()
        if new_task:
            tasks.append(new_task)
            write_tasks(tasks)
            print("Added.")
        else:
            print("Empty task not added.")
    elif choice == "3":
        for i in range(len(tasks)):
            print(i+1, "-", tasks[i])
        try:
            n = int(input("Task number to remove: "))
            if 1 <= n <= len(tasks):
                removed = tasks.pop(n-1)
                write_tasks(tasks)
                print("Removed:", removed)
            else:
                print("Invalid number.")
        except:
            print("Enter a valid number.")
    elif choice == "4":
        print("Bye.")
        break
    else:
        print("Wrong option. ")

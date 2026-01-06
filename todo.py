import os

TASK_FILE = os.path.join("data", "tasks.txt")

def add_task(task):
    with open(TASK_FILE, "a") as f:
        f.write(task + "\n")
    print(f"Task added: {task}")

def list_tasks():
    if not os.path.exists(TASK_FILE):
        print("No tasks found.")
        return
    with open(TASK_FILE, "r") as f:
        tasks = f.readlines()
    if not tasks:
        print("No tasks found.")
        return
    print("Your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")

def mark_done(task_number):
    if not os.path.exists(TASK_FILE):
        print("No tasks found.")
        return
    with open(TASK_FILE, "r") as f:
        tasks = f.readlines()
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return
    task = tasks.pop(task_number - 1)
    with open(TASK_FILE, "w") as f:
        f.writelines(tasks)
    print(f"Marked as done and removed: {task.strip()}")

def main():
    while True:
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                num = int(input("Enter task number to mark as done: "))
                mark_done(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

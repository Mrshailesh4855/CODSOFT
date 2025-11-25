tasks=[]

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status ="Done" if task["completed"] else "Pending"
            print(f"{index}. {task['title']} -{status}")
        print()

def add_task():
    title=input("Enter task name: ").strip()
    if title=="":
        print("Task name cannot be empty.\n")
        return
    task={"title": title, "completed": False}
    tasks.append(task)
    print("Task added.\n")

def update_task():
    show_tasks()
    if not tasks:
        return
    try:
        num=int(input("Enter task number to update: "))
        new_title=input("Enter new task name: ").strip()
        if new_title=="":
            print("Task name cannot be empty.\n")
            return
        tasks[num - 1]["title"]=new_title
        print("Task updated.\n")
    except:
        print("Invalid input.\n")

def mark_completed():
    show_tasks()
    if not tasks:
        return
    try:
        num=int(input("Enter task number to mark completed: "))
        tasks[num - 1]["completed"]=True
        print("Task marked as completed.\n")
    except:
        print("Invalid input.\n")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        num=int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted.\n")
    except:
        print("Invalid input.\n")

def main():
    while True:
        print("----- TO DO LIST -----")
        print("1.View tasks")
        print("2.Add task")
        print("3.Update task")
        print("4.Mark task completed")
        print("5.Delete task")
        print("6.Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            show_tasks()
        elif choice=="2":
            add_task()
        elif choice=="3":
            update_task()
        elif choice=="4":
            mark_completed()
        elif choice=="5":
            delete_task()
        elif choice=="6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.\n")

if __name__=="__main__":
    main()

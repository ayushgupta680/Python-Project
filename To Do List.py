tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("\n Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}.{task}")
            
def add_task():
    task = input("Enter task:")
    tasks.append(task)
    print("task added")
    
def delete_task():
    show_tasks()
    try:
        tasks_num = int(input("Enter the delete tasks:"))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Delete: {removed}")
        else:
            print("Invalid task number:")
    except:
        print("Enter the valid number:")
        
while True:
    print("\n To Do List Menu")
    print("1. Show task")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter choice:")
    
    if choice == "1":
        show_tasks
    elif choice == "2":
        add_task
    elif choice == "3":
        delete_task
    elif choice == "4":
        print("Good Bye")
        break
    else:
        print("Exit")
        
    
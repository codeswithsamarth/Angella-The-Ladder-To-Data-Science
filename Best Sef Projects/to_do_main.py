import os
import sys

file = "tasks.txt"

if not os.path.exists(file):
    with open(file,"w") as f:
        pass
    print("📁 File Created Successfully")

def add_task():
    time = input("Enter The Time To Do List Ex 10:30\n")
    task = input("Enter The Task:\n")
    record = f"{time}-{task}"
    with open(file,'a') as f:
        f.write(record+'\n')

def view_task():
    with open(file,"r") as f:
        tasks = f.readlines()
    if not tasks:
        print("No Task Found")
        sys.exit()
    else:
        for t in tasks:
            print("-",t.strip())

def delete_task():
    view_task()
    task = input("Enter The Task With Time To Delete Task:\n")
    with open(file,"r") as f:
        tasks = f.readlines()
    with open(file,"w") as f:
        for t in tasks:
            if t.strip().lower() != task.lower():
                f.write(t)
    print("Task Deleted Successfully If its Exists")

while True:
    print("1.Add Task")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Exit")

    choice = (input("Enter The choice\n"))
    if choice == "1":
        add_task()
        sys.exit()
    elif choice == "2":
        view_task()
        sys.exit()
    elif choice == "3":
        delete_task()
        sys.exit()
    else:
        print("Thanks For Visiting")
        break
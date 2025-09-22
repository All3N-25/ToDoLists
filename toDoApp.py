# toDoApp.py

tasks = []

def add_task(task):
    """
    This function adds a new task.
    """
    tasks.append(task)
    print("Task added!")

def show_tasks( ):
    """ Function printing tasks """
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        for i, task in enumerate(tasks):
            print(i + 1, ".", task)

def removetask(tasknumber):
    tasks.pop(tasknumber) 
    print("task removed!!")

def main():
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("enter choice : ")
        if ch=="1":
            t = input("enter task : ")
            addtask(t)
        elif ch=="2":
            show_tasks()
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            removetask(n)   
        elif ch=="4":
            break
        else:
            print("wrong choice!!")
main()

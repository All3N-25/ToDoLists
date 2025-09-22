# toDoApp.py

tasks=[]

def addtask(task) :
  tasks.append(task)
  print("task added!")

def showTasks( ):
    if len(tasks)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

def remove_task(task_number):
    """
    Removes a task from the tasks list based on the provided task number.
    Args:
        task_number (int): The index number of the task to remove (1-based indexing)
    Returns:
        None. Prints success or error message.
    Raises:
        None. Invalid task numbers are handled with error message.
    Example:
        >>> removeTask(1)  # Removes first task
        task removed!!
        >>> removeTask(99) # Invalid task number
        Invalid task number
    """
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("task removed!!")
    else:
        print("Invalid task number")

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
            showTasks()
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            removeTask(n)   
        elif ch=="4":
            break;
        else:
            print("wrong choice!!")
main()

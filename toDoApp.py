# toDoApp.py

"""
A simple ToDoList app that allows the user to:
1. Create a list.
2. View tasks.
3. And remove tasks by their number.
"""

tasks = []

def add_task(task):
    """This function adds a new task. """
    tasks.append(task)
    print("Task added!")

def show_tasks():
    """Function printing tasks """
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        for i, task in enumerate(tasks):
            print(i + 1, ".", task)

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
    """Run the main task menu loop. """
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = int(input("Enter choice: "))

        match ch:
            case 1:
                t = input("Enter task: ")
                add_task(t)
            case 2:
                show_tasks()
            case 3:
                n = int(input("Enter task no to remove: "))
                remove_task(n)
            case 4:
                break
            case _:
                print("Wrong choice!!")
        print("--------------------")

if __name__ == "__main__":
    main()

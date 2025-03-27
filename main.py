# tasks/main.py
# docstrings by chatgpt for my use, otherwise unimportant
from model.task import Task
from model.taskstate import TaskState  # Import TaskState from task_state.py
from util.date import Date
from datetime import datetime

def main():
    """
    **init** is a special method in Python known as the constructor.
    It is automatically called when a new instance of the class is created.
    """
    # creating a custom current date object to use as a reference date
    today = Date(datetime.now().strftime("%Y-%m-%d"))
    
    # creating an initial list of tasks using task.py class
    # task constructor allows us to give tasks unique details
    tasks = [
        Task(1, "purchase and consume banana", Date("2024-03-28"), "monkey", TaskState.OPEN),
        Task(2, "relink the fire", Date("2024-03-27"), "the chosen undead", TaskState.WAITING),
        Task(3, "give the covenant back their bomb", Date("2024-04-03"), "master chief", TaskState.OPEN),
        Task(4, "glass reach", Date("2024-03-25"), "Thel Vadamee,", TaskState.DONE)  # Update with appropriate state if needed
    ]
    
    # print out tasks
    print("Task List:")
    for task in tasks:
        print(task)

# __main__ is a special built-in variable
# ensures main() only runs when script is directly executed
if __name__ == "__main__":
    main()
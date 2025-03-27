# tasks/model/task.py
# docstrings by chatgpt for my use, otherwise unimportant
class Task:
    def __init__(self, task_id, description, due, assignee, state):
        """
         __init__ is a special method in Python known as the constructor.
         It is automatically called when a new instance of the class is created.
         """
        self.task_id = task_id # Initialize the task's unique identifier.
        # validate that the description is not empty.
        if not description:
            raise ValueError("Description cannot be empty")
        self.description = description #
        self.due = due
        self.assignee = assignee
        self.state = state

    def get_relative_due(self, reference):
        """
         This method calculates the relative due status of the task based on a reference date.
         It assumes that the 'due' date object has a method called 'days_between' that returns
         the difference in days between the due date and the provided reference date.
         Parameters:
         - reference: A date object to compare with the task's due date.
         Returns:
         A string indicating the relative status of the task (e.g., "Overdue", "Today").
         """
        # Calls the 'days_between' method of the 'due' date object to calculate the number of days
        # between the task's due date and the provided reference date. The 'due' attribute is assumed
        # to be a date object that has a 'days_between' method, which calculates and returns the difference
        # in days between two dates.
        days = self.due.days_between(reference)
        # check task state and days difference to return the relative due status, todo: make
        # relativeduedelagate and all required functionality
        if self.state == "Done":
            return "Irrelevant"
        elif days < 0:
            return "Overdue"
        elif days < 1:
            return "Today"
        elif days == 1:
            return "Tomorrow"
        elif days <= 7:
            return "ThisWeek"
        elif days <= 14:
            return "NextWeek"
        elif days <= 30:
            return "ThisMonth"
        elif days <= 60:
            return "NextMonth"
        else:
            return "Later"

    def __str__(self):
        """
         __str__ is a special method used to provide a human-readable string representation
         of the object. When you call str() on an object or use print(), Python internally
         uses this method.
         Returns:
         A string with raw task values.
         """
        return f"{self.task_id}, {self.description}, {self.assignee}, {self.due}, {self.state}"
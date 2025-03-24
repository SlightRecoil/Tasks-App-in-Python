# tasks/model/task.py

class Task:
    def __init__(self, task_id, description, due, assignee, state):
        """
        __init__ is a special method in Python known as the constructor.
        It is automatically called when a new instance of the class is created.
        
        Parameters:
          - task_id: Unique identifier for the task.
          - description: A short text describing the task.
          - due: The due date for the task (could be a date object).
          - assignee: The person assigned to this task.
          - state: The current state of the task (e.g., "Pending", "Done").
        """
        self.task_id = task_id  # Initialize the task's unique identifier.

        # Validate that the description is not empty.
        if not description:
            raise ValueError("Description cannot be empty")
        self.description = description  # Set the task description.

        self.due = due          # Set the due date for the task.
        self.assignee = assignee  # Set the person responsible for the task.
        self.state = state        # Set the current state of the task.

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
        # Calculate the number of days between the due date and the reference date.
        days = self.due.days_between(reference)
        
        # Check task state and days difference to return the relative due status.
        if self.state == "Done":
            return "Irrelevant"  # If the task is completed, its due date doesn't matter.
        elif days < 0:
            return "Overdue"     # Negative days means the due date has already passed.
        elif days < 1:
            return "Today"       # Less than 1 day means it's due today.
        elif days == 1:
            return "Tomorrow"    # Exactly one day left means it's due tomorrow.
        elif days <= 7:
            return "ThisWeek"    # Due within a week.
        elif days <= 14:
            return "NextWeek"    # Due in the next week.
        elif days <= 30:
            return "ThisMonth"   # Due within this month.
        elif days <= 60:
            return "NextMonth"   # Due in the next month.
        else:
            return "Later"       # Due further in the future.

    def __str__(self):
        """
        __str__ is a special method used to provide a human-readable string representation 
        of the object. When you call str() on an object or use print(), Python internally 
        uses this method.

        Returns:
          A string that describes the task in a readable format.
        """
        return f"Task {self.task_id}: {self.description} assigned to {self.assignee}, due on {self.due}"

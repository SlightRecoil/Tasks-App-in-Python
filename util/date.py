# tasks/model/date.py
"""
Custom Date Class for Task Management

Provides a simple date representation with comparison and formatting capabilities.
"""

from datetime import datetime, timedelta

class Date:
    """
    A custom date class for task management.

    Attributes:
        year (int): The year of the date
        month (int): The month of the date
        day (int): The day of the date
    """

    def __init__(self, date_string):
        """
        Initialize a Date object from a string.

        Args:
            date_string (str): Date in YYYY-MM-DD format

        Raises:
            ValueError: If date string is not in correct format
        """
        try:
            # Parse the date string
            parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
            
            # Store components separately
            self.year = parsed_date.year
            self.month = parsed_date.month
            self.day = parsed_date.day
            
            # Store the full datetime for internal calculations
            self._date = parsed_date
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

    def days_between(self, other_date):
        """
        Calculate the number of days between this date and another date.

        Args:
            other_date (Date): Another Date object to compare

        Returns:
            int: Number of days between dates (can be negative)
        """
        return (self._date - other_date._date).days

    def __str__(self):
        """
        String representation of the date.

        Returns:
            str: Date in YYYY-MM-DD format
        """
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    def __repr__(self):
        """
        Detailed string representation of the date.

        Returns:
            str: Detailed representation of the date
        """
        return f"Date('{self.__str__()}')"
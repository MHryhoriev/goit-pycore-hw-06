"""
This module defines the `AddressBook` class which manages multiple `Record` objects.
"""

from collections import UserDict
from .record import Record

class AddressBook(UserDict):
    def __init__(self):
        """
        Initialize an empty address book.
        """
        super().__init__()

    def add_record(self, record: Record):
        """
        Add a new record to the address book.
        :param record: The record to add.
        :raises ValueError: If the record already exists.
        """
        if record.name.value not in self.data:
            self.data[record.name.value] = record
            print(f"Contact '{record.name.value}' added successfully.")
        else:
            raise ValueError(f"Record with name '{record.name.value}' already exists.")
        
    def find(self, name: str):
        """
        Find a record by name.
        :param name: The name of the record to find.
        :return: The record if found.
        :raises ValueError: If the record is not found.
        """
        if name in self.data:
            return self.data[name]
        else:
            raise ValueError(f"Record with name '{name}' is missing.")
        
    def delete(self, name: str):
        """
        Delete a record by name.
        :param name: The name of the record to delete.
        :raises ValueError: If the record is not found.
        """
        if name in self.data:
            del self.data[name]
            print(f"Contact '{name}' has been successfully deleted.")
        else:
            raise ValueError(f"Record with name '{name}' not found.")

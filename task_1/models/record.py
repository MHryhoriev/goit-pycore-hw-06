"""
This module defines the `Record` class which manages contact details.
"""

from .field import Name, Phone

class Record:
    def __init__(self, name: str):
        """
        Initialize the record with a name and an empty list of phones.
        :param name: The name of the contact.
        """
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        """
        Add a phone number to the record.
        :param phone: The phone number to add.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """
        Remove a phone number from the record.
        :param phone: The phone number to remove.
        """
        self.phones = list(filter(lambda item: item.value != phone, self.phones))

    def edit_phone(self, old_phone: str, new_phone: str):
        """
        Edit an existing phone number in the record.
        :param old_phone: The phone number to replace.
        :param new_phone: The new phone number to add.
        """
        phone_to_edit = next((phone for phone in self.phones if phone.value == old_phone), None)
        if phone_to_edit:
            phone_to_edit.value = new_phone

    def find_phone(self, phone: str):
        """
        Find a phone number in the record.
        :param phone: The phone number to find.
        :return: The phone number if found, else None.
        """
        return next((item for item in self.phones if item.value == phone), None)

    def __str__(self):
        """
        Return a string representation of the record.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

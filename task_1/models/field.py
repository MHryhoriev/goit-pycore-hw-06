"""
This module defines the `Field` class and its subclasses `Name` and `Phone`.
"""

import re

class Field:
    def __init__(self, value):
        """
        Initialize the field with a value.
        :param value: The value to store in the field.
        """
        self.value = value

    def __str__(self):
        """
        Return the string representation of the field's value.
        """
        return str(self.value)


class Name(Field):
    """
    Class representing a contact's name.
    Inherits from `Field`.
    """
    pass


class Phone(Field):
    def __init__(self, value: str):
        """
        Initialize a Phone instance with validation.
        :param value: The phone number to initialize.
        """
        self.value = self.validate_phone(value)

    def validate_phone(self, value: str) -> str:
        """
        Validate the phone number format.
        :param value: The phone number to validate.
        :return: The validated phone number.
        :raises ValueError: If the phone number is invalid.
        """
        phone_pattern = re.compile(r'^\d{10}$')
        
        if not phone_pattern.match(value):
            raise ValueError(f"Invalid phone number: {value}. Phone number must contain exactly 10 digits.")

        return value

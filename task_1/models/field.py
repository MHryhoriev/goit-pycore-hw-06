"""
This module defines the `Field` class and its subclasses `Name` and `Phone`.
"""

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
    """
    Class representing a contact's phone number.
    Inherits from `Field`.
    """
    pass

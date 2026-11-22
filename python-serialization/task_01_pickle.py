#!/usr/bin/env python3
"""Module that serializes custom objects using pickle."""
import pickle


class CustomObject:
    """Custom class with name, age and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initialize the object attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the instance to a file, return None on error."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load an instance from a file, return None on error."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None

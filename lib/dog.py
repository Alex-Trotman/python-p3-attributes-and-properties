#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=""):
        # Directly use the name property to trigger validation.
        self.name = name

    def get_name(self):
        # Getter simply returns the value of _name.
        return self._name

    def set_name(self, value):
        # Setter includes validation for the name.
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            # Print the specified message if validation fails.
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)

    def __init__(self, breed=""):







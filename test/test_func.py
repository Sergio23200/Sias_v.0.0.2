import pytest


class person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def your_age(self, age: int):
        self.age = age

    def your_name(self, name: str):
        self.name = name

    def return_age(self):
        return (self.age)

    def return_name(self):
        return (self.name)

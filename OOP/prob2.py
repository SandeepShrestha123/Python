'''
Write a class “Calculator” capable of finding square, cube and square root of a number.
'''

import math


class Calculator:

    def __init__(self):
        self.x = None

    def get_data(self):
        self.x = int(
            input("enter a number to find it's sq, cube and sq root: "))

    def calculation(self):
        print(
            f"The square of the given number {self.x} is: {self.x**2}", end="")
        print(
            f"\nThe cube of the given number {self.x} is: {self.x**3}", end="")
        print(
            f"\nThe sq root of the given number {self.x} is {math.sqrt(self.x)}")

    @staticmethod
    def greet():
        print("Hello, Welcome User")


num = Calculator()
num.greet()
num.get_data()
num.calculation()

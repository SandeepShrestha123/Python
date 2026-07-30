'''
Write a class ‘Complex’ to represent complex numbers, along with overloaded operators
‘+’ and ‘*’ which adds and multiplies them
'''


class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"


c = Complex(5, 4)
c1 = Complex(5, 5)
print(c+c1)

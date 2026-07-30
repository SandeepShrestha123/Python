'''this is the example of understand the @property
'''


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def display(self):
        print(
            f"The length and the breadth of the rectangle is {self.length} {self.breadth}")

    @property
    def area(self):
        print(f"the area of the rectangle is {self.length * self.breadth}")


r = Rectangle(10, 20)
r.display()
r.area

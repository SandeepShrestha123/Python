'''This is the another example of using the property'''


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def Area(self):
        print(f"The area of the circle is {2.14 * self.radius * self.radius}")

    @property
    def Diameter(self):
        print(f"The diameter of the circle is {2 * self.radius}")


c = Circle(4)
c.Area
c.Diameter

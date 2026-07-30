'''
Create a class (2-D vector) and use it to create another class representing a 3-D vector.
'''


class twodVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2d vector is {self.i}i+{self.j}.j\n")


class threedVector(twodVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The 3d vector is {self.i}i+{self.j}j {self.k}k\n")


a = twodVector(1, 2)
a.show()
b = threedVector(1, 2, 3)
b.show()

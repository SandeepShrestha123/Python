'''this is the example of using split along with using the getter and setter'''


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def show(self):
        print(f"The name of the Employee is {self.fname} {self.lname}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


n = Employee("sandeep", "shrestha")
print(f"The name is {n.name}")
n.name = "Srestaa Shrestha"
n.show()

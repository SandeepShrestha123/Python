'''This is the example of understandinf the constructor'''


class Employee:

    # this is the dunder method and automatically runs everytime when new object are created
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        print("Object values initialized")

    def getInfo(self):
        print(
            f"The name of the employee is {self.name} having id {self.id} and salary {self.salary}.\n")

    @staticmethod
    def greet():
        print("Welcome to the office.")


sandeep = Employee("Sandeep", "01", "2000000")
Employee.getInfo(sandeep)
sandeep.greet()  # sandeep.getInfo()

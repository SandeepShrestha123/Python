'''
Simple example of Inheritance
'''


class Person:
    def __init__(self):
        print("The constructor of Person class is called")

    def nature(self):
        print("This person is very kind in nature.")


class Student(Person):
    def storeInfo(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address

    def getInfo(self):
        print(
            f"The name of the student is {self.name} having id {self.id} who lives in {self.address}")


o = Student()
o.storeInfo("Sandeep", 101, "Paknajol")
o.getInfo()
o.nature()

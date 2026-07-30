'''
This is the example of multiple inheritance
'''


class Student:

    subject = "Python"

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self. age = age

    def study(self):
        print(
            f"The name of the studnet is {self.name} having id {self.id} and is of age {self.age} and his/her major is in {self.subject}")


class Sport:
    sport_name = "Football"

    def displaySport(self):
        print(f"This studnet is engaged in this {self.sport_name} sport.")


class Athelete(Student, Sport):
    tournament = "Furfuri nagar tournament"

    def viewDetails(self):
        print(
            f"{self.name} is participating in this {self.tournament} which is the sport of {self.sport_name} which will be held at Dashrath Stadium")


a = Athelete("Sandeep", 101, 21)
a.study()
a.displaySport()
a.viewDetails()

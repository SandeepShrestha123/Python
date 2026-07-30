'''this is the example of using the self in python'''


class Student:
    name = "Sandeep"
    age = 21
    studying_at = "NCCS college"

    def getInfo(self):
        print(f"The age is {self.age} and studying at {self.studying_at}")


sandeep = Student()
sandeep.getInfo()  # without using the self this statement will act like Student.getInfo(sandeep) wheere sandeep will be taken as an arguement

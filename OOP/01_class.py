"""This is the example of understanding the syntax of the class"""


class Student:
    # name = "Sandeep"
    age = 21
    studying_at = "NCCS college"


sandeep = Student()
sandeep.name = "Sandeep"
print("Reading from the class:")
print(sandeep.name, sandeep.age, sandeep.studying_at)

# in this example, the attribute name is the Object/Instance attribute wwhere as the age and studying_at are the clas attribute

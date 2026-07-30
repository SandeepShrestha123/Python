class Student:
    name = "Sandeep"
    age = 21
    studying_at = "NCCS college"


sandeep = Student()
sandeep.studying_at = "Triniy College"
print("Reading from the class:")
print(sandeep.name, sandeep.age, sandeep.studying_at)

# here in this example the value of the attr atudying_at will take the instance attr as instance has higher preference than the class attribute

"""My first Python program"""

print(" Hello world ")
print("*" * 10)
course = "Sandeep shrestha"
print(course[0:3])
print(course[0:])
print(course[:3])
print(len(course), "\n")

# this is the example of escape sequence where \ is a escape character and " is a escape sequence
name = "Python \"Programming\n"
print(name)

# this is the example of concatenation of the string (f-strintg {formatted string})
first = "sandeep"
last = "Shrsetha"
fullName = f"{first} {last}"
print(fullName)


# This is the example of methods like strip and title find
"""find method is used to return the index value if the given character 
is found in the expression where in method returns true
or false when searching the characters from the string"""

name = "  \nsrestaa shrestha\n"
print(name.title())
print(name.strip())
print(name.find("Sres"))
print("sres" in name)
print("Paknajol" not in name)

# for exponent use double ^^

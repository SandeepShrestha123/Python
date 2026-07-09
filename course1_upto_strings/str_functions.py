"""this is the example of string functions"""

str1 = "Sandeep Shrestha"
print(str1)
print(str1.endswith("tha"))
print(str1.startswith("tha"))

# this capitalize function is used to capitalize the first index character
new_str1 = str1.capitalize()
print(new_str1)

new_str = str1.replace("Sandeep", "Sretaa")
print(new_str)

trim_str = "    Sandeep Shrestha"
print(trim_str)
print("This is the example of trimming of string space")
print(trim_str.lstrip())


# string cannot be change to change the string into another we need to declare the new string

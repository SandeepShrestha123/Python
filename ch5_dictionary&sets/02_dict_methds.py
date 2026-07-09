"""this is the example of methods of the dictionary"""

marks = {
    "sandeep": 95,
    "srestaa": 100,
    "Shashwot": 90
}

# print(marks.items())  # displays the entire dict key-value pairs
# print(marks.keys())  # displays the entire dict key names
# # displays the entire values which are stored in the dictionary
# print(marks.values())

# marks.update({"sandeep": 99})
# print(marks)


# print(marks.get("Sandeep"))  # this returns the value as none
# this gives the output as error as there is not any key present in the dictionary
# print(marks["Sandeep"])


# the difference between the pop and the popitem is that pop removes the key-value pairs by providing the key name whereas the popitems remove the last key-value pair from the dictionary
item = marks.pop("Shashwot")
print(marks)
print(item)

item1 = marks.popitem()
print(marks)
print(item1)

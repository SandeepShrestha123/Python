number = [90, 98, 77, 88]

# index = 0
# for items in number:
#     print(f"The number at index {index} is {i}")
#     index += 1

# the same above loop can be done simply using the enumerate function
for index, items in enumerate(number):
    print(f"The number at index {index} is {items}")

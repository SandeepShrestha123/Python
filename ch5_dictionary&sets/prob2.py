"""Problem to show the unique numbers"""

numbers = set()
for n in range(8):
    x = int(input("Enter any numbers: "))
    numbers.add(x)
print("your Entered numbers are:\t")
print(numbers)

# if we add numbers in an empty set such that the numbers are 20, 20.0 and '20' the length will be equal to 2 as python treats 20 and 20.0 as same number doesnot checks for data type

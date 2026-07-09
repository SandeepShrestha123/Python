"""Write a program which finds out whether a given name is present in a list or not."""

name = []
for i in range(4):
    n = input("enter the name of the anything: ")
    name.append(n)

n = input("enter any name: ")
if n in name:
    print("the name is present in the list. ")
else:
    print("the name is not in the list ")

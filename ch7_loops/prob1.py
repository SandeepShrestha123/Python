"""Write a program to print multiplication table of a given number using for loop"""

n = int(input("enter the number of which you want to find the multiplication of: "))
print(f"the matrix multiplication of your given number {n} is:\n")
for i in range(1, 11):
    result = n * i
    print(f"{n} X {i} = {result}\n")

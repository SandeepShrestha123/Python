"""Attempt problem 1 using while loop."""

n = int(input("enter the number of which you want to find the multiplication of: "))
print(f"the matrix multiplication of your given number {n} is:\n")
i = 1
while i <= n:
    result = n*i
    print(f"{n} x {i} = {result}")
    i += 1

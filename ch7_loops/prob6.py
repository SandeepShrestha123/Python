"""Write a program to calculate the factorial of a given number using for loop."""

n = int(input("Enter the number you want to find the factorial of: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"the factorial of the givenm number {n} is: {fact}")

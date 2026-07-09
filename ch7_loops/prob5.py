"""Write a program to find the sum of first n natural numbers using while loop.
"""

n = int(input("enter the range of the natural numbers"))
summation = 0
i = 1
while i <= n:
    summation += i
    i += 1
print(f"The sum of first {n} natural number is {summation}")

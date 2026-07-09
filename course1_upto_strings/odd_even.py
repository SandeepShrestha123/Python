"""This is the program of odd even in python"""

n = int(input("Enter the range of the numbers"))
count = 0
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        count += 1
print(f"We have total of {count} even numbers.")

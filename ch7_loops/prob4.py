"""Write a program to find whether a given number is prime or not."""

n = int(input("enter the number to check whether it is prime or not: "))
for i in range(2, n):
    if n % i == 0:
        print(f"the number you have entered {n} is not a prime number")
        break

else:
    print(f"the number you have entered {n} is a prime number")

"""Write a program to find whether a given username contains less than 10 characters or not."""

username = input("enter you username: ")
if len(username) <= 10:
    print("The username characters must be greater than 10")
else:
    print("Valid Username")

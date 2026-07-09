"""A spam comment is defined as a text containing following keywords: Make a lot of
money, buy now, subscribe this, click this. Write a program to detect these spams."""

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("enter you string: ")
if message in p1 or message in p2 or message in p3 or message in p4:
    print("The string u have entered is a spam string")
else:
    print("The string u have entered is not a spam string")

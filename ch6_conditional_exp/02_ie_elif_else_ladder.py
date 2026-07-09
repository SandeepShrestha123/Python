"""If-elif-else ladder"""

age = int(input("enter the age of the person: "))

if age > 18:
    print("You can cast the vote.")

elif age < 0:
    print("The input age is in negative")

elif age == 0:
    print("The age you have entered is 0")

else:
    print("You cannot cast the vote")


print("the end of program.....")

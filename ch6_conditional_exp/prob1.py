"""find the greatest from the 4 numbers"""

num = []
greatest = 0
for i in range(4):
    x = int(input(f"Enter {i+1} number: "))
    num.append(x)


for n in num:
    if n > greatest:
        greatest = n

print(f"the greatest number is: {greatest} ")

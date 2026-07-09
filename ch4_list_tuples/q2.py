"""Accept the marks of students of 6 subjects and diplay the marks in sorted order"""

marks = []
for i in range(6):
    f1 = input("Enter the marks of students:\t")
    marks.append(f1)
print(marks)
marks.sort()
print(marks)

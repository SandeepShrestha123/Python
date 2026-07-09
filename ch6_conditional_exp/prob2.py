"""percentage based if question"""

# marks = []
# summation = 0

# for i in range(3):
#     m = int(input(f"Enter the marks of the student in subject {i+1}: "))
#     marks.append(m)

# for i, mark in enumerate(marks):
#     summation += marks[i]

# total_percentage = (100*summation)/300

# if total_percentage > 40 and marks[0] > 33 and marks[1] > 33 and marks[2] > 33:
#     print(
#         f"you are passed in the exam with the percentage of: {total_percentage}")

# else:
#     print(
#         f"you are not passed in the exam as you percentage is: {total_percentage}")


# same question using tuples

temp = []
for i in range(3):
    m = int(input(f"Enter the marks of subject{i+1}: "))
    temp.append(m)

marks = tuple(temp)
summation = sum(marks)
total_percentage = (100*summation)/300
if total_percentage > 40 and marks[0] > 33 and marks[1] > 33 and marks[2] > 33:
    print(
        f"you have passed the exam with the percentage of: {total_percentage}")
else:
    print(
        f" sorry, you failed the exam as yur total percentage is only: {total_percentage}")

'''
Write a program to mine a log file and find out whether it contains ‘python’
'''

with open("log.txt", "r", encoding="UTF-8") as f:
    lines = f.readlines()

line_no = 1
for line in lines:
    if "python" in line.lower():
        print(f"the word Python is present in the line no {line_no}")
        break
    line_no += 1

else:
    print("The word Python is not presnet in the file.")

'''
Write a program to make a copy of a text file “this.txt”.
'''


with open("replace.txt", "r", encoding="UTF-8") as f:
    contents = f.read()

with open("replace_copy.txt", "w", encoding="UTF-8") as f:
    f.write(contents)

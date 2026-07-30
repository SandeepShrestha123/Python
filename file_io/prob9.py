'''
Write a program to find out whether a file is identical and matches the content of another
file.

'''

with open("replace.txt", "r", encoding="UTF-8") as f:
    contents = f.read()

with open("replace_copy.txt", "r", encoding="UTF-8") as f:
    contents1 = f.read()

if contents == contents1:
    print("Both the files have the same contents")

else:
    print("Seperate contents in both the files")

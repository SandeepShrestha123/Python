'''
A file contains a word “Donkey” multiple times. You need to write a program which
replaces this word with ##### by updating the same file.
'''

with open("prob4.txt", "r", encoding="UTF-8") as f:
    data = f.read()

if "donkey" in data.lower():
    data = data.replace("donkey", "#####")
    with open("prob4.txt", "w", encoding="UTF-8") as f:
        f.write(data)

print("Text replaced successfully")

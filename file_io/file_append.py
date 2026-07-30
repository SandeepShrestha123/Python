"""This is the example of file appending"""

st = "This is the example of apending in an existing file.\n"

f = open("file_io/writing.txt", "a", encoding="UTF-8")
f.write(st)

print("\nsuccessfully appended!\n")

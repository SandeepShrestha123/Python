"""This is the example of file reading """

st = "This is the example of writing in a new file."

f = open("writing.txt", "w", encoding="UTF-8")
f.write(st)

print("\nsuccessfully written!\n")

print("Now reading from the file:")
f = open("writing.txt", "r", encoding="UTF-8")
data = f.read()
print(data)
f.close()

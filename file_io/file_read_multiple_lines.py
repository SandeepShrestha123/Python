"""this is the example of reading multiple lines from the file"""

f = open("file_io/multiplelines.txt")
# data = f.readlines()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()

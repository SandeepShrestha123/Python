'''
this is the example of using with statement wihtout needing to use open and end explicitly
'''


with open("file_io/writing.txt", "r", encoding="UTF-8") as f:
    print(f.read())

print("\nSuccessfully read from the file")

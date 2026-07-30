'''Write a program to mine a log file and find out whether it contains python'''

with open("log.txt", "r", encoding="UTF-8") as f:
    content = f.read().lower()


if "python".lower() in content:
    print("Python word is present in the file.")

else:
    print("Python word is not present in the file.")

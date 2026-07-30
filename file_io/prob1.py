""""this is the problem to read from the file called poems.txt and fiding the word twinkle from that file"""

with open("file_io/poems.txt", "r", encoding="UTF-8") as f:
    text = f.read()

    if text.lower().find("twinkle") != -1:
        print("the word twinkle is present in the file.\n")

    else:
        print("the word twinkle is not present in the file.\n")

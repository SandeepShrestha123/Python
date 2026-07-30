words = ["donkey", "animal", "you"]

with open("replace.txt", "r", encoding="UTF-8") as f:
    data = f.read().lower()

for word in words:
    data = data.replace(word, "#" * len(word))

with open("replace.txt", "w", encoding="UTF-8") as f:
    f.write(data)

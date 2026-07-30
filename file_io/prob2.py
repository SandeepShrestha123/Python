""" The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file Hi-score.txt which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score.
"""

import random


def game():
    score = random.randint(1, 100)
    return score


score = game()
print(f"You scored {score}")

with open("file_io/highscore.txt", "r", encoding="UTF-8") as f:
    data = f.read()

if data == "":
    with open("file_io/highscore.txt", "w", encoding="UTF-8") as f:
        f.write(str(score))
else:
    if score > int(data):
        with open("file_io/highscore.txt", "w", encoding="UTF-8") as f:
            f.write(str(score))

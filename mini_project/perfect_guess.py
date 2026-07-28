import random

n = random.randint(1, 100)
a = -1
guesses = 1
while a != n:
    a = int(input("Guess the number: "))
    if a < n:
        print("Higher number please!")
        guesses += 1
    elif a > n:
        print("Lower Number please!")
        guesses += 1

print(f"You have guess the correct number {n} in {guesses} attempt")

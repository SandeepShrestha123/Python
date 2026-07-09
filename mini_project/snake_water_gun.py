"""snake-water-gun- game"""

import random

myDict = {
    "snake": 1,
    "water": -1,
    "gun": 0
}
revDict = {
    1: "snake",
    -1: "water",
    0: "gun"
}

print("\n1.Enter 1 to Play the game\n2.Enter 2 for Exiting from the game\n")

while True:
    ch = int(input("\nDo u want to play? "))
    computer = random.choice(["snake", "gun", "water"])
    match ch:
        case 1:
            choice = input("\nEnter you choice: ").lower()
            if choice not in ["snake", "water", "gun"]:
                print("Invalid choice! Please enter snake, water, or gun.")
                continue
            else:
                urChoice = myDict[choice]
                print(
                    f"Your choice: {revDict[urChoice]}\nComputer choice: {computer}")

                if choice == computer:
                    print("Both choice are same. No one wins!\n")

                elif (choice == "snake" and computer == "water") or (choice == "water" and computer == "gun") or (choice == "gun" and computer == "snake"):
                    print("You Win")

                else:
                    print("Computer Wins")

        case 2:
            print("\nExited from the game......")
            break

        case _:
            print("invalid Menu choice!!!")

print("Game ends.....")

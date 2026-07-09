"""to find the value of user input data from the dictionary"""

words = {
    "subha-pravat": "Good-morning",
    "kukur": "dog",
    "biralo": "cat"
}

print(words, type(words))

meaning = input("\nEnter the word which you want to find the meaning: ")
print(f"The meaning of the word {meaning} is {words[meaning]}")

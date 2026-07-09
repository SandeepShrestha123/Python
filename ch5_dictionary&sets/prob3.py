"""to enter the key-value pairs from the user"""

language = {}
for n in range(4):
    key = input("Enter the name of your friend: ")
    values = input("Enter your friend fav programming langauge ")
    language.update({key: values})
    # language[key] = values
print("\nKey-value pairs are: \n")
print(language)

# if we have two keys of the same name then the values will be assign to the latest one, if two values are same from the input then it can happen as the main focus is only on the key not on the values

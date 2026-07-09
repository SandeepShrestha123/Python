"""While loop program"""

# here the lower will convert any kind of text format to lowercase
command = ""
while command != "quit" and command != "QUIT":  # or use while loop as while command.lower != "quit"
    command = input("Enter any text")
    print("ECHO: ", command)

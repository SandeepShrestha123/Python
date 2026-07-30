'''This is the example of exception handling with finally'''

# the finally block use can be especially seen in the function calls
# It is different with the exception with else as the else part runs only when the try blocks run successfully
# finally blocks run no matter what


def check_num():
    try:
        a = int(input("Enter a number: "))
        print(f"The number you entered is {a}")
    except:
        print("Enter a number not invalid characters!!!")
    finally:
        print("Program run successfully")


check_num()

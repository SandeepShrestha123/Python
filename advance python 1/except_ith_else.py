def check_num():
    try:
        a = int(input("Enter a number: "))
        print(f"The number you entered is {a}")
    except:
        print("Enter a number not invalid characters!!!")
    else:
        print("Program run successfully")


check_num()

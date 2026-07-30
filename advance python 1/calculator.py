# Python considers calculator.py as the main program. so if we perform print(__name__) then prints the value as main as it is directly running from the main program

def add(a, b):
    return a+b


def sub(a, b):
    return a-b


# print(__name__)

if __name__ == "__main__":
    print(add(10, 20))
    print(sub(10, 20))


'''Here if we don't include " if __name__ == "__main__" " the file where we import this file method (add or sub) will run this file code from top to bottom that means the imported file will generate the result of 
    print(add(10, 20))
    print(sub(10, 20))
although it is not the part of their file 
'''

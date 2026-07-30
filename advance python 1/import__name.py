# here the file runs the another file by importing so it prints the ___name__ as the imported file name without the extension .py which is module if the file name was calculator.py then ___name__ will print calculator as the value

from calculator import add
print(add(2, 1))

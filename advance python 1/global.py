a = 90  # first assign the value as 90 in a


def show():
    # global a  # if we declare a as global then the value assigned after this to a will be globally declared even outside this funtion
    a = 4  # here a is a local variable which value will only be initialzed only in this method
    print(a)


show()
print(a)

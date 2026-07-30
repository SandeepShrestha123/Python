'''
This is the example of understading the class methods
'''


class Parent:

    a = 10

    @classmethod  # becaude of class method the class attribute won't be affected by the instance attribute
    def Value(cls):
        print(f"The value of this class is {cls.a}")


o = Parent()


# o.a = 45  # here the instance attribute is changing the value of the class attribute as it has the preference over the class attribute
# o.Value()  # prints the value 45 instead of 10


o.a = 45
o.Value()  # even thougfh we set the instance attribute the value of a will not be change becuase of the class method

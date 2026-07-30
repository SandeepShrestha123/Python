'''this is the example of understand the static method'''


class Student:

    @staticmethod
    def greet():
        print("Welcome to the college.")


Student.greet()

# here in this program, using the static method will not pass as an arguement

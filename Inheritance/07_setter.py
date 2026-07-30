'''
This is the example of using the setter in 
'''


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def display(self):
        print(f"The celsuis is {self.celsius}°C")

    @property
    def fahrenheit(self):
        f = (self.celsius * 9/5) + 32
        return f

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
        # print(f"Your Fahrenheit in celsius is : {self.celsius}")


t = Temperature(90)
t.display()
print(f"The conversion of given  celsius to fahrenheit is {t.fahrenheit}°F.")
t.fahrenheit = 30
t.display()

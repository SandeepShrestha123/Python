'''
Create a class “Programmer” for storing information of few programmers working at
Microsoft.
'''


class Programmer:
    # def __init__(self, name, id, address):
    #     self.name = name
    #     self.id = id
    #     self.address = address
    #     print("the Values for the programmers are initialized.")

    def __init__(self):
        self.id = None
        self.roll = None
        self.name = None

    def storeInfo(self):
        self.name = input("Enter programmmer name: ")
        self.id = input("Enter programmer id: ")
        self.address = input("Enter programmer address: ")

    def getInfo(self):
        print(
            f"\nThe prorgammer name is {self.name} having id {self.id} and lives in {self.address}")


p = Programmer()
p.storeInfo()
p.getInfo()

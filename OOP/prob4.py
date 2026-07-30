'''
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get
fare information of train running under Indian Railways
'''


from random import randint


class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(
            f"Your booking for the Train no: {self.trainNo} from {fro} to {to} has been done.")

    def getStatus(self):
        print("your train is available and ready to run. ")

    def getFareInfo(self, fro, to):
        print(
            f"The price for the Train no: {self.trainNo} from {fro} to {to} is Rs.{randint(1, 5000)}")


t = Train(200)
t.book("Kathmandu", "Pokhara")
t.getFareInfo("Kathmandu", "Pokhara")
t.getStatus()

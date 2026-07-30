'''
Suppose a user has Rs. 5000 in their account.
Ask the user to enter the withdrawal amount.
Raise an exception if the amount is greater than the available balance.
'''


class InsufficientBalance(Exception):
    pass


def check_balance(num):
    if num >= 5000:
        raise InsufficientBalance("Insufficient Balance")
    else:
        print(f"Amount {num} withdrawed successfully")


balance = int(input("Enter the ammount you want to withdraw: "))
check_balance(balance)

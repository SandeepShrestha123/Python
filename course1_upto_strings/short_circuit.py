"""short circuit evaluation"""

withdraw_greater_50k = True
credit_granted = True
student = True
if withdraw_greater_50k and credit_granted and not student:
    print("eligible")
else:
    print("not eligible")

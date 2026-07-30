'''This is the example of understading the type definitions'''

n: int = 5  # defining n as an integer
print(n)

a: str = "SAndeep"
print(a)


def sum(a: int, b: int) -> int:  # we are defining the types of the parameters as int and gives the result as an intger
    return a+b


print(f"The sum of the two integers is {sum(90, 10)}")

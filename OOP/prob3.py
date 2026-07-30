'''
Create a class with a class attribute a; create an object from it and set ‘a’ directly using
‘object.a = 0’. Does this change the class attribute?
'''


class Demo:
    a = 10          # Class attribute


obj = Demo()

print("Before changing:")
print("Class attribute:", Demo.a)
print("Object attribute:", obj.a)

obj.a = 0          # Creates an instance attribute
# does not modify the class attribute.
# Instead, Python creates a new instance attribute named a.

print("\nAfter changing:")
print("Class attribute:", Demo.a)
print("Object attribute:", obj.a)

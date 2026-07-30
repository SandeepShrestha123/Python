'''
this is the example of understanding walrus operator in python
'''

# normally we would write this code as
# n = len([1, 2, 3, 4, 5])
# if n > 3
#   .......
    
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long with {n} elements expeected (<=3)")


"""
Names defined inside a def can only be seen by the code within that def.
You cannot even refer to such names from outside the function.
"""


# Global scope
x = 99
print('x =', x)

x += 1

print('x =', x)


def test():
    global x
    x += 1
    # print('z =', z)

test()

print('x =', x)

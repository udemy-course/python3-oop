
"""
continue and break
"""


a = 1

while a < 10000:
    if a % 2 == 0:
        a = a + 1
        continue
    print(a)
    a = a + 1



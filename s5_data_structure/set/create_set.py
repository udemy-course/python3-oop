
"""
Python also includes a data type for sets.

A set is an unordered collection with no duplicate elements.
Basic uses include membership testing and eliminating duplicate entries.

Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
"""

# create an empty set
a = set()
print('empty set =', a)

b = [1, 2, 2, 3, 4, 4]
print('set of list: ', set(b))

a = set('abracadabra')
b = set('alacazam')

print('set a =', a)
print('set b =', b)


print('set a - b =', a - b)
print('set a & b =', a & b)
print('set a | b = ', a | b)

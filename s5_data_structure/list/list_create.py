
# A list contains items separated by commas and enclosed within square brackets.

a = [1, 2, 3]

print('list a =', a)


# List indexes like strings starting at 0 in the beginning of the list and working their way from -1 at the end.

print('a[0] =', a[0])

print('a[-1] =', a[-1])

# Python Lists are mutable objects that can change their values.

a[0] = 2

print('list a =', a)


# list elements don't have to be of the same type.

b = ['a', 'c', 1, 2, 3, [4, 5, 6]]

print('list b =', b)


# Lists operations include slicing ([ ] and [:]) ,
# concatenation (+), repetition (*), and membership (in).

c = [1, 2, 3, 4, 5]
print('c =', c)
print('c[1:3] =', c[1: 3])

d = [6, 7, 8]

print('d =', d)

print('c + d =', c + d)

print('1 in d?', 1 in d)

print('2*d =', 2*d)

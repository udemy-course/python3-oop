"""
It steps through the items of lists, tuples, strings, the keys of dictionaries and other iterables.
The Python for loop starts with the keyword "for" followed by an arbitrary variable name,
which will hold the values of the following sequence object, which is stepped through.

The general syntax looks like this:

for <variable> in <sequence>:
	<statements>


"""

a = [1, 2, 3]
b = (4, 5, 6)
c = 'abc'
d = {1: 'a', 2: 'b'}

for i in d:
    print('i =', i)

print('done')


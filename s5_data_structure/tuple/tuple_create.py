
# Python Tuples are Immutable objects that cannot be changed once they have been created.
# A tuple contains items separated by commas and enclosed in parentheses instead of square brackets.

t = (1, 2, 3)
print(t)
print(t[0])

# You can update an existing tuple by (re)assigning a variable to another tuple.
# Tuples are faster than lists and protect your data against accidental changes to these data.

"""
➜  ~ python3.5 -m timeit -s "x=(1,2,3,4,5,6,7,8)" "y=x[3]"
10000000 loops, best of 3: 0.0591 usec per loop
➜  ~
➜  ~ python3.5 -m timeit -s "x=[1,2,3,4,5,6,7,8]" "y=x[3]"
10000000 loops, best of 3: 0.0624 usec per loop
➜  ~
"""

# The rules for tuple indices are the same as for lists and they have the same operations, functions as well.
# To write a tuple containing a single value, you have to include a comma,
# even though there is only one value. e.g. t = (3, )

print('t[1:3] =',  t[1: 3])

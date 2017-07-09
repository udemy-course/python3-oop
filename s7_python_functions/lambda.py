
"""
The lambda’s general form is the keyword lambda,
followed by one or more arguments (exactly like the arguments list you enclose in parentheses in a def header),
followed by an expression after a colon:

lambda argument1, argument2,... argumentN :expression using arguments
"""

def sum(x, y ,z):
    return x + y + z

print(sum(1, 2, 3))


f = lambda x, y, z: x + y + z
print(f(1, 2, 3))


"""
➜  ~ python3.5
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 08:49:46)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = [1, 2, 3, 4]
>>> b = []
>>>
>>>
>>> for i in a:
...     b.append(i + 3)
...
>>> b
[4, 5, 6, 7]
>>>
>>>
>>>
>>>
>>> a = [1, 11, 14, 56]
>>>
>>> b = [33, 2, 27, 35]
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> def inc(x):
...     return x + 3
...
>>>
>>> map(inc, a)
<map object at 0x1022e25c0>
>>>
>>>
>>> list(map(inc, a))
[4, 14, 17, 59]
>>>
>>>
>>>
>>>
>>> list(map(inc, b))
[36, 5, 30, 38]
>>>
>>>
>>>
>>>
>>> a
[1, 11, 14, 56]
>>> b
[33, 2, 27, 35]
>>>
>>>
>>>
>>>
>>>
>>> map((lambda x: x+3), a)
<map object at 0x1022e2668>
>>>
>>>
>>> list(map((lambda x: x+3), a))
[4, 14, 17, 59]
>>>
>>>
>>>
>>> list(map((lambda x: x+3), b))
[36, 5, 30, 38]
>>>
"""
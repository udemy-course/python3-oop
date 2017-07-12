
# Read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
    data = f.read()

# Write binary data to a file
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')


"""
>>> a = 'hello world'
>>> b = b'hello world'
>>> a
'hello world'
>>> b
b'hello world'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'bytes'>
>>> print(len(a))
11
>>> print(len(b))
11
>>> for i in a:
...     print(i)
...
h
e
l
l
o

w
o
r
l
d
>>> for i in b:
...     print(i)
...
104
101
108
108
111
32
119
111
114
108
100
>>>
"""

# http://tool.oschina.net/commons?type=4
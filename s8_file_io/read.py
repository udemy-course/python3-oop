
f = open('test.txt')

f.read()
f.close()

"""
➜  s8_file_io git:(master) ✗ python3.5
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 08:49:46)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>> f = open('/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io/test.txt')
>>> f
<_io.TextIOWrapper name='/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io/test.txt' mode='r' encoding='UTF-8'>
>>>
>>>
>>>
>>>
>>>
>>> s = f.read()
>>> s
'this is first line\nthis is the second line\nthis is the third line\n'
>>> s1 = f.read()
>>> s1
''
>>>
>>>
>>>
>>> f.close()
>>>
>>> f = open('/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io/test.txt')
>>>
>>>
>>>
>>> f.readline()
'this is first line\n'
>>> f.readline()
'this is the second line\n'
>>>
>>> f.readline()
'this is the third line\n'
>>>
>>>
>>> f.readline()
''
>>> f.close()
>>> f = open('/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io/test.txt')
>>>
>>>
>>>
>>> l = f.readlines()
>>>
>>>
>>> l
['this is first line\n', 'this is the second line\n', 'this is the third line\n']
>>> f.close()
>>>
>>>
>>> f = open('/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io/test.txt')
>>>
>>>
>>> for line in f:
...     print(line)
...
this is first line

this is the second line

this is the third line

>>> f.close()
>>>
>>> f = open('/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io/test.txt')
>>>
>>> f.readline()
'this is first line\n'
>>> f.readline()
'this is the second line\n'
>>> f.readline()
'this is the third line\n'
>>> f.readline()
''
>>> f.seek(0)
0
>>> f.readline()
'this is first line\n'
>>> f.readline()
'this is the second line\n'
>>> f.readline()
'this is the third line\n'
>>>
>>>
>>> f.seek(0)
0
>>> f.readline()
'this is first line\n'
>>> f.seek(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: negative seek position -1
>>> f.seek(-1
KeyboardInterrupt
>>> ^D
➜  s8_file_io git:(master) ✗ clear

➜  s8_file_io git:(master) ✗ python3.5
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 08:49:46)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> f = open('/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io/test.txt')
>>> f.readline()
'this is first line\n'
>>> f.readline()
'this is the second line\n'
>>> f.readline()
'this is the third line\n'
>>> f.readline()
''
>>> f.seek(0)
0
>>> f.readline()
'this is first line\n'
>>> f.readline()
'this is the second line\n'
>>> f.readline()
'this is the third line\n'
>>> f.readline()
''
>>> f.tell()
66
>>>
>>> f.seek(0)
0
>>> f.tell()
0
>>> f.readline()
'this is first line\n'
>>> f.tell()
19
>>>
"""
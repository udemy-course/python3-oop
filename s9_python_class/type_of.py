"""
➜  ~ python3.5
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 08:49:46)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 12
>>>
>>> type(a)
<class 'int'>
>>>
>>>
>>> b = '12'
>>> type(b)
<class 'str'>
>>>
>>> type([1,2])
<class 'list'>
>>>
>>>
>>>
>>>
>>> max()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: max expected 1 arguments, got 0
>>> max([1,2,3])
3
>>> max
<built-in function max>
>>> type(max)
<class 'builtin_function_or_method'>
>>>
>>>
>>>
>>>
>>>
>>> class Demo:
...     pass
...
>>>
>>>
>>> demo = Demo()
>>> demo
<__main__.Demo object at 0x1023e26a0>
>>> type(demo)
<class '__main__.Demo'>
>>>
>>>
>>>
>>>
>>> isinstance(a, int)
True
>>>
>>>
>>> isinstance(a, str)
False
>>> isinstance(b, str)
True
>>> b
'12'
>>>
>>> isinstance(demo, Demo)
True
>>>
>>>
"""
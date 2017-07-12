
"""
>>> import os
>>> path = '/Users/beazley/Data/data.csv'

>>> # Get the last component of the path
>>> os.path.basename(path)
'data.csv'

>>> # Get the directory name
>>> os.path.dirname(path)
'/Users/beazley/Data'

>>> # Join path components together
>>> os.path.join('tmp', 'data', os.path.basename(path))
'tmp/data/data.csv'

>>> # Expand the user's home directory
>>> path = '~/Data/data.csv'
>>> os.path.expanduser(path)
'/Users/beazley/Data/data.csv'

>>> # Split the file extension
>>> os.path.splitext(path)
('~/Data/data', '.csv')
>>>
"""

"""
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 08:49:46)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io'
>>> os.listdir()
['os_module.py', 'read.py', 'test.txt', 'write.py']
>>> os.chdir("/Users/penxiao/PycharmProjects/github/udemy/python3-oop")
>>> os.getcwd()
'/Users/penxiao/PycharmProjects/github/udemy/python3-oop'
>>> os.listdir()
['.git', '.gitignore', '.idea', 'LICENSE', 'README.md', 's2_python_for_windows', 's3_python_for_mac', 's4_python_for_linux', 's5_data_structure', 's6_control_structure', 's7_python_functions', 's8_file_io']
>>> os.chdir("/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io")
>>> os.listdir()
['os_module.py', 'read.py', 'test.txt', 'write.py']
>>> os.mkdir('test')
>>>
>>>
>>> os.listdir()
['os_module.py', 'read.py', 'test', 'test.txt', 'write.py']
>>> os.getcwd()
'/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io'
>>>
>>> a = os.getcwd()
>>> a
'/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io'

>>>
>>> os.dirname()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'dirname'
>>> os.listdir()
['os_module.py', 'read.py', 'test', 'test.txt', 'write.py']
>>>
>>> os.getcwd()
'/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io'
>>> os.list()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'list'
>>>
>>>
>>> os.getcwd()
'/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io'
>>> os.listdir()
['os_module.py', 'read.py', 'test', 'test.txt', 'write.py']
>>> a = os.getcwd()
>>> os.path.dirname(a)
'/Users/penxiao/PycharmProjects/github/udemy/python3-oop'
>>> os.path.isfile(a)
False
>>> os.path.isdir(a)
True
>>> new_path = os.path.join(a, 'new_folder')
>>> new_path
'/Users/penxiao/PycharmProjects/github/udemy/python3-oop/s8_file_io/new_folder'
>>> os.path.exists(new_path)
False
>>> os.listdir()
['os_module.py', 'read.py', 'test', 'test.txt', 'write.py']
>>>
"""
# datetime


# datetime对象的构建

"""
>>> from datetime import datetime
>>> cur = datetime(year=2016, month=9, day=2, hour=10, minute=30,second=13, microsecond=2)
>>> cur
datetime.datetime(2016, 9, 2, 10, 30, 13, 2)
>>> cur.date()
datetime.date(2016, 9, 2)
>>> cur.time()
datetime.time(10, 30, 13, 2)
>>>
"""

# 获取当前时间的datetime对象

"""
>>> datetime.today()
datetime.datetime(2017, 8, 8, 8, 50, 49, 552758)
>>> datetime.now()
datetime.datetime(2017, 8, 8, 8, 50, 54, 17340)
>>>
"""

# 通过时间戳来获取一个datetime对象

"""
>>> import time
>>> datetime.fromtimestamp(time.time())
datetime.datetime(2017, 8, 8, 8, 52, 7, 158772)
>>>
"""


# 通过date和time对象来组合成一个datetime对象

"""
>>> from datetime import date
>>> from datetime import time
>>> from datetime import datetime
>>>
>>> d = date(year=2017, month=8, day=10)
>>> t = time(hour=19, minute=20)
>>> d
datetime.date(2017, 8, 10)
>>> t
datetime.time(19, 20)
>>> datetime.combine(d,t)
datetime.datetime(2017, 8, 10, 19, 20)
>>>
"""

# replace()方法允许我们对datetime的任意字段进行替换，并返回一个新的datetime对象
# 这个新的对象在其他字段上与原有对象保持一致

"""
>>> t1 = datetime.now()
>>> t1.date()
datetime.date(2017, 8, 8)
>>> t1.time()
datetime.time(11, 12, 14, 584808)
>>> t2 = t1.replace(month=t1.month+1)
>>> t2
datetime.datetime(2017, 9, 8, 11, 12, 14, 584808)
>>> t2 = t1.replace(month=t1.month+1, day=t1.day+3)
>>> t2
datetime.datetime(2017, 9, 11, 11, 12, 14, 584808)
>>>
"""

# time delta

"""
>>> t1 = datetime.now()
>>> t2 = datetime.now()
>>> t2-t1
datetime.timedelta(0, 4, 671693)
>>> t = t2 - t1
>>> t
datetime.timedelta(0, 4, 671693)
>>> t.days
0
>>> t.seconds
4
>>> t.total_seconds
<built-in method total_seconds of datetime.timedelta object at 0x10203bf80>
>>> t.total_seconds()
4.671693
>>>

>>> from datetime import timedelta
>>> delta = timedelta(days=7, seconds=10)
>>> delta
datetime.timedelta(7, 10)
>>>
>>> now = datetime.now()
>>> now
datetime.datetime(2017, 8, 8, 11, 34, 34, 918385)
>>>
>>> now + delta
datetime.datetime(2017, 8, 15, 11, 34, 44, 918385)
>>>

"""

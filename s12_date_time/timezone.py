"""
time zone
"""


"""
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 08:49:46)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import arrow
>>>
>>>
>>> utc = arrow.utcnow()
>>> utc
<Arrow [2017-08-08T15:43:50.258796+00:00]>
>>> utc
<Arrow [2017-08-08T15:43:50.258796+00:00]>
>>> dir(utc)
['_ATTRS', '_ATTRS_PLURAL', '_MONTHS_PER_QUARTER', '__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__weakref__', '_cmperror', '_datetime', '_get_datetime', '_get_frames', '_get_iteration_params', '_get_timestamp_from_input', '_get_tzinfo', 'astimezone', 'ceil', 'clone', 'ctime', 'date', 'datetime', 'dst', 'float_timestamp', 'floor', 'for_json', 'format', 'fromdate', 'fromdatetime', 'fromtimestamp', 'humanize', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'min', 'naive', 'now', 'range', 'replace', 'resolution', 'shift', 'span', 'span_range', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'to', 'toordinal', 'tzinfo', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday']
>>>
>>> utc.date()
datetime.date(2017, 8, 8)
>>> utc.time()
datetime.time(15, 43, 50, 258796)
>>>
>>>
>>>
>>>
>>> utc8 = utc.to('Asia/Shanghai')
>>>
>>>
>>> utc8
<Arrow [2017-08-08T23:43:50.258796+08:00]>
>>>
>>> utc8.time()
datetime.time(23, 43, 50, 258796)
>>> utc8.date()
datetime.date(2017, 8, 8)
>>> utc
<Arrow [2017-08-08T15:43:50.258796+00:00]>
>>> utc.timestamp
1502207030
>>>
>>> import time
>>> t = time.time()
>>>
>>> t
1502207311.38509
>>>
>>>
>>> t2 = utc.fromtimestamp(t)
>>> t2
<Arrow [2017-08-08T23:48:31.385090+08:00]>
>>>
"""
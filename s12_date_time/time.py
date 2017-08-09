# time module

import time


print('start...')

time.sleep(5)
print('end.....')

"""
>>> import time
>>> time.gmtime(0)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
>>>
>>> help(time)
>>> time.gmtime()
time.struct_time(tm_year=2017, tm_mon=8, tm_mday=7, tm_hour=15, tm_min=11, tm_sec=49, tm_wday=0, tm_yday=219, tm_isdst=0)
>>>
>>>
>>>
>>>
>>>
>>> time.time()
1502118799.14633
>>>
>>>
>>> a = time.time()
>>> a
1502118924.542266
>>> a
1502118924.542266
>>> a
1502118924.542266
>>>
>>>
>>>
>>>
>>> a
1502118924.542266
>>>
>>>
>>> time.gmtime(a)
time.struct_time(tm_year=2017, tm_mon=8, tm_mday=7, tm_hour=15, tm_min=15, tm_sec=24, tm_wday=0, tm_yday=219, tm_isdst=0)
>>>
>>>
>>>
>>> time.localtime()
time.struct_time(tm_year=2017, tm_mon=8, tm_mday=7, tm_hour=23, tm_min=16, tm_sec=13, tm_wday=0, tm_yday=219, tm_isdst=0)
>>> b = time.localtime()
>>> time.strftime("%a, %d %b %Y %H:%M:%S +0000",b)
'Mon, 07 Aug 2017 23:18:38 +0000'
>>>
>>>
>>> time.sleep(5)
>>>
"""
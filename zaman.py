import network
import time
import utime
import machine
from ntptime import settime

settime()
rtc=machine.RTC()

# for time convert to second
tampon1=utime.time() 
    
# for gmt. For me gmt+3. 
# 1 hour = 3600 seconds
# 3 hours = 10800 seconds
tampon2=tampon1+10800

# for second to convert time
(year, month, mday, hour, minute, second, weekday, yearday)=utime.localtime(tampon2)

# first 0 = week of year
# second 0 = milisecond
rtc.datetime((year, month, mday, 0, hour, minute, second, 0))

#ŞU ŞEKİLDE ÇAĞIRABİLİRSİN
"""
>>> import zaman
>>> simdi = zaman.rtc.datetime()
>>> print(simdi)
(2018, 8, 12, 6, 20, 20, 41, 887396)
"""
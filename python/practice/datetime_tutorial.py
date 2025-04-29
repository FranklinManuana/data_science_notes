import datetime

# get the current date and time
now = datetime.datetime.now()

print(now)
#----------------------------------------------

# Example 4: get current date------------------------------------
current_date = datetime.date.today()

print(current_date)

#get list of all datetime module attributes
print(dir(datetime))

d = datetime.date(2022, 12, 25)
print(d)
# --------------------------------------------------
from datetime import date

#today() to get current date
todays_date = date.today()

print("Today's date=", todays_date)

#Example 5: Get timestamp---------------------------------------

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

# Example 6: get today's date in year,month, and day------

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#Example 7: Time object to represent time

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time(hour, minute and second)
b = time(11, 34, 56)
print(b)

# time(hour, minute, and second)
c = time(hour = 11, minute = 34, second =56)
print(c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print(d)


# Example 8: Print hour, minute, second and microsecond-------------

from datetime import time
a = time(11, 34, 56)

print("Hour =", a.hour)
print("Minute =", a.minute)
print("Second =", a.second)
print("Microsecond =", a.microsecond)

# Example 9: Python datetime object -----------------------------

from datetime import datetime

#datetime(year, month, day)
a = datetime(2022, 12, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)


# Example 10: Print year, month, hour, minute and timestamp

from datetime import datetime

a = datetime(2022, 12, 28, 23, 55, 59, 342380)

print("Year =", a.year)
print("Month =", a.month)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Timestamp =", a.timestamp())

# Exampl 12: Difference between two time delta objects -------------

from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)

t3 = t1 - t2

print("t3 =", t3)


# Example 14 : Time duration in seconds ----------------------------

from datetime import timedelta
t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("Total seconds =", t.total_seconds())


# Handling Timezones in Python-----------------------------------------

from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m%d%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m%d%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m%d%Y, %H:%M:%S"))
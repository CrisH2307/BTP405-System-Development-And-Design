def isLeapYear1(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(isLeapYear1(2000))


### or

import calendar
def isLeapYear2(year):
    return calendar.isleap(year)

print(isLeapYear2(2000))
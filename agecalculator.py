import datetime
from dateutil import relativedelta
import datetime as dt
year = int(input('Enter Year of Birth'))
month = int(input('Enter month of Birth'))
day = int(input('Enter Day of Birth'))
date1 = datetime.date(year, month, day)
year = int(input('Enter Year of Calculation'))
month = int(input('Enter month of Calculation'))
day = int(input('Enter Day of Calculation'))
date2 = datetime.date(year, month, day)
difference = relativedelta.relativedelta(date2, date1)
years = difference.years
months = difference.months
days = difference.days
hours = difference.hours
minutes = difference.minutes
print(" %s year %s months %s days " %(years, months, days))
diffDays = (years*365)+(months*30)+days
print("Which is %s days" %(diffDays))
print("Which is %s months & %s days" %(((years*12)+months),days))
print("which is %s weeks & %s days" %((int(diffDays/7)),(diffDays%7)))
diffHours = (diffDays*24)+dt.datetime.now().hour
print("Which is %s hours" %diffHours)
print("Which is %s minutes" %(diffHours*60))
print("Which is %s seconds" %(diffHours*60*60))
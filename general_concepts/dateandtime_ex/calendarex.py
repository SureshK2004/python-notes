import calendar
import datetime as dt
currentdate=dt.date.today()
year=currentdate.year

month=currentdate.month
print(calendar.month(year,month-1))
print(calendar.month(year,month+1))
print(calendar.month(year,month))
print(calendar.calendar(0))
obj=calendar.Calendar(firstweekday=0)
for day in obj.iterweekdays():
    print(day)

for day in obj.itermonthdates(2024,9):
    print(day)

print(obj.monthdayscalendar(2024,9))
print(obj.monthdatescalendar(2024,9))

import datetime
import datetime as dt
currenttime=(dt.datetime.now())
print(currenttime)
currentday=(dt.date.today())
print(currentday)
print(f"current year={currenttime.year}")
print(f"current day={currenttime.day}")
print(f"current month={currenttime.month}")
print(f"current microsecond={currenttime.microsecond}")
print(f"current hour={currenttime.hour}")
#creating a specific date and time
mydatetime=dt.datetime(2024,6,24,5,24,44,884092)
print(mydatetime)
mydate=dt.date(2023,6,24)
print(mydate)
mytime=(dt.time(10,33,32,675432))
print(mytime)
orderdate=dt.datetime(2024,6,24,5,24,39,765432)
print(orderdate)
rev_date=dt.datetime(2023,6,27,5,24,30,908765)
print(rev_date)
difference=rev_date-orderdate
print(difference.days)
no_of_days=90
future=currenttime+datetime.timedelta(days=no_of_days)
print(future)
print(currenttime.weekday())#it startt with 0 to n number of time
print(currenttime.isoweekday())#it start with 1 to n number of time
if currenttime.weekday()==0:
    print('monday')
elif currenttime.weekday()==1:
    print('tuesday')
elif currenttime.weekday()==2:
    print('wednesday')
elif currenttime.weekday() == 3:
    print('thursday')
elif currenttime.weekday()==4:
    print('friday')
elif currenttime.weekday()==5:
    print('saturday')
else:

    print('sunday')
print(currenttime.isoformat())
print(currenttime)
update_hour=currenttime.replace(month=11)
print(update_hour)
print(mydate)
print(mytime)
combine=dt.datetime.combine(mydate,mytime)#it is used to combine the day and time
print(combine)
v=1633072800
v1=dt.datetime.fromtimestamp(v)
print(v1)
print(currenttime.strftime('%Y-%m-%d'))
print(currenttime.strftime('%Y/%m/%d'))
print(currenttime.strftime('%B'))# B it will print the exact month in alphabets
print(currenttime.strftime('%B %d,%Y'))
print(currenttime.strftime('%Y/%m/%d %H:%M'))
print(currenttime.strftime('%Y/%m/%d %H:%M:%S'))
print(currenttime.strftime('%B %Y/%m/%d %H:%M:%S %p'))# SMALL P REFERS TO AM OR PM

#Datetime Exercises
from datetime import datetime
from datetime import date
now= datetime.now()
print(now)
format_date= now.strftime('%m/%d/%Y,%H:%M:%S')
print(format_date)
date_str='5 December,2019'
date_obj= datetime.strptime(date_str,'%d %B,%Y')
print(date_obj)
today= date(year=2025,month=1,day=31)
new_year= date(year=2026, month=1,day=1)
time_left_newyear= new_year-today
print(time_left_newyear)
date1=date(year=1970,month=1,day=1)
time_diff=today - date1
print(time_diff)
def new_year_message(today):
    today= datetime.today()
    if today.month==1 and today.day==1:
        return 'Happy New Year!!!'
    else:
        return 'Just another day in the trenches'
print(new_year_message(today))
# File Handling

from datetime import datetime, date, time, timedelta


d = date(2012, 10, 25)
print(d, type(d))
t = time(12, 15, )
print(t, type(t))
# dt = d = t
dt = datetime.combine(d, t)
print(dt, type(dt))
print(datetime.now().replace(microsecond=0))
dtt = datetime.now()
dtt = dtt.replace(hour=12, minute=12, second=30, year=2025, month=1, day=1)
print(dtt)
# dat = input('Введите дату (дд.мм.ггг):')
# date_ = datetime.strptime(dat, '%d.%m.%Y')
# print(date_)
dt = datetime.now()
# d = dt.timetuple()
# for i in d:
print(dt.weekday())
print(dt.isoweekday())
cc = dt.isocalendar()
print(cc)
print(dt.strftime('%A %d %Y %B'))
# days = ('Пн','Вт')
# print(days[dt.weekday()])
td = date_ - dt
print(td.days)
print(td.seconds)
#     print(i)
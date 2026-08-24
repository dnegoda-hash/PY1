from datetime import datetime, date, time, timedelta


# d = date(2012, 10, 25)
# print(d, type(d))
# t = time(12, 15, )
# print(t, type(t))
# # dt = d + t
# dt = datetime.combine(d, t)
# print(dt, type(dt))
# print(datetime.now().replace(microsecond=0))
# dtt = datetime.now()
# dtt = dtt.replace(hour=12, minute=12, second=30, year=2025, month=1, day=1)
# print(dtt)
# # dat = input('введите дату (дд.мм.гггг):')
# # date_ = datetime.strptime(dat, '%d.%m.%Y')
# # print(date_)
# dt = datetime.now()
# # d = dt.timetuple()
# # for i in d:
# #     print(i)
# print(dt.weekday())
# print(dt.isoweekday())
# cc = dt.isocalendar()
# print(cc)
# print(dt.strftime('%A %d %Y %B  %H:%M:%S'))
# print(dt.strftime('%A %d %Y %B  %X'))
# days = ('Пн','Вт','Ср','Чт','Пт','Сб','Вс')
# print(days[dt.weekday()])
# dat = input('введите дату (дд.мм.гггг):')
# date_ = datetime.strptime(dat, '%d.%m.%Y')
# td = date_ - dt
# print(td)
# print(td.days)
birthday = input("Дата рождения (дд.мм.гггг): ")
birthday = datetime.strptime(birthday, "%d.%M.%Y").date()
date_today = date.today()
print(birthday,date_today)
year_=date_today.year
birthday = birthday.replace(year=year_)
if birthday < date_today:
    birthday_ = birthday.replace(year=year_ + 1)
    age_days = ((date_today + timedelta(days=365)) - dirth_day).days
elif birthday == date_today:
    print('!!!')
    exit(0)

days_ = (birthday-date_today).days
age_days = (date_today - birth_day).days
age = age_days / 365
print(f'Количество дней до ДР - "{days_}" Вам исполнится {age:2d} лет')
print('Количество дней до ДР - \'{}\', Вам исполнится {} лет'.format(days_, age))
print('Количество дней до ДР - %d'% (days_))


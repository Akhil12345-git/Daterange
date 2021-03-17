from datetime import date
year = date.today().year
month = date.today().month

dt = date(year, month, 1)
first_w = dt.isoweekday()
saturday1 = 28-first_w
saturday2 = 28-first_w
saturday3 = 28-first_w
saturday4 = 28-first_w
dt = date(year, month, saturday1)
dt = date(year, month, saturday2)
dt = date(year, month, saturday3)
dt4 = date(year, month, saturday4)

if dt == dt4:
    pass
elif dt and dt % 5 == 0:
    print(dt.day, dt.month, dt.year)
else:
    print(dt4.day, dt4.month, dt4.year)



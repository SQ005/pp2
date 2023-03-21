# #1///
import datetime
def five_days():
    d = datetime.date.today()
    l = datetime.timedelta(days = 5)
    print(d - l)
    print(l)
five_days()
#2///
# import datetime
# def days():
#     d = datetime.date.today()
#     l = datetime.timedelta(days = 1)
#     print(d - l)
#     print(d)
#     print(d + l)
# days()
#3///
import datetime
def micro():
    d = datetime.datetime.today()
    print(d)
    d = datetime.datetime.today().replace(microsecond = 0)
    print(d)
micro()
#4///
import datetime
def sec():
    a = datetime.datetime(2013,12,30,23,59,59)
    b = datetime.datetime(2013,12,31,23,59,59)
    print((b-a).total_seconds())
sec()
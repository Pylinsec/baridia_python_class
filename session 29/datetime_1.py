import datetime

# kar ba zeman feli ya local 
# print(datetime.datetime.now()) # tarikh emrooz chap mikone 
# print(datetime.datetime.now().day) # rooze chandom 
# print(datetime.datetime.now().month) # month
# print(datetime.datetime.now().year) # month
# print(datetime.datetime.now().year) # year
# print(datetime.datetime.now().minute) # minute alan
# print(datetime.datetime.now().hour) # hour be saat local 
# print(datetime.datetime.now().second) # second be saat local 
# print(datetime.datetime.now().microsecond) # micro second be saat local 
print(datetime.datetime.now().weekday) # rooz dar hafteh 


# kar ba zeman khas 
# birthday = datetime(year,month,day,hour,minute,second,microsecond)
birthday = datetime.datetime(2008,6,10,20,25,21,256325)
print(birthday.hour)

# strftime--> string format time
print(birthday.strftime('%B'))
print(birthday.strftime('%a'))
print(birthday.strftime('%A'))
print(birthday.strftime('%w'))
print(birthday.strftime('%W'))
print(birthday.strftime('%y'))
print(birthday.strftime('%x'))
print(birthday.strftime('%X'))


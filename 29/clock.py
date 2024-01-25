import datetime , time

while True:
    now = datetime.datetime.now()
    # print(now)
    time.sleep(1)
    print(f"{now.strftime('%H')}:{now.strftime('%M')}:{now.strftime('%S')}\r",end='')
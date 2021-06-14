import os
import datetime

today = datetime.date.today()
str = str(today.year) + str(today.month) + str(today.day)
if not os.path.exists(str):
    os.mkdir(str)
else:
    print('ディレクトリはすでに存在します')

s = input('日付入力してください。')
s1 = s.split('/')
d = datetime.date(int(s1[0]),int(s1[1]),int(s1[2]))
day = {0:'日',1:'月',2:'火',3:'水',4:'木',5:'金',6:'土'}
wday = d.weekday()
print(day[wday] + '曜日')

d2w = d + datetime.timedelta(days = 14)
print('入力された日付の2週間後の日付:')
print(d2w)
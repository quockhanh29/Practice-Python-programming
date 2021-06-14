import urllib.request
import os
import datetime
import shutil

today = datetime.date.today()
str = str(today.year) + str(today.month) + str(today.day)
if not os.path.exists(str):
    os.mkdir(str)
else:
    print('ディレクトリはすでに存在します')


url ='https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'
with urllib.request.urlopen(url) as conn:
    data = conn.read()
    text = data.decode('utf-8')

    with open('sample13_3_2.html', 'w') as f:
        f.write(text)

shutil.move('sample13_3_2.html', str)

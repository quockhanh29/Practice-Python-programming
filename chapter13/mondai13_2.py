import os
import datetime
import requests
import time
from bs4 import BeautifulSoup

def start (url, dir):
    time.sleep(1)
    response = requests.get(url)
    requests.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        start(href, dir)
    fname = url.split('/')[-1]
    filepath = os.path.join(dir, fname)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(response.text)

today = datetime.date.today()
dir = str(today.year) + str(today.month) + str(today.day)+ '_test'
if not os.path.exists(dir):
    os.mkdir(dir)

url ='https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'
start(url,dir)

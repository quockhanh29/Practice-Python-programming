import requests
from bs4 import BeautifulSoup

url ='https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'

response = requests.get(url)
requests.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

for a_tag in soup.find_all('a'):
    text = a_tag.string
    href = a_tag.get('href')
    print('{}:{}'.format(text, href))

import urllib.request

url = 'https://wii.winschool.jp/public/students/73256.html'

with urllib.request.urlopen(url) as conn:
    data = conn.read()
    text = data.decode('utf-8')
    print(text)

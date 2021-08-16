import requests
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/index.do'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    # location = soup.select('dl > dt')
    # print(location)
else : 
    print(response.status_code)

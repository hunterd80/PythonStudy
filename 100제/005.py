import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropoltian_Subway"

resp = requests.get(url)
html_src =resp.text

soup = BeautifulSoup(html_src, 'html.parser')

first_img = soup.find(name='img')
print(first_img)
print("\n")

target_img = soup.find(name='img', attrs={'src':'//upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/30px-Wiktionary-logo-v2.svg.png'})
print(target_img)

# 파일명 : 30px-Wiktionary-logo-v2.svg.png

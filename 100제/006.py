import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropoltian_Subway"
resp = requests.get(url)
html_src =resp.text
soup = BeautifulSoup(html_src, 'html.parser')

links = soup.find_all("a")



#d
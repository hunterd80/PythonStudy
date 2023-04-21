import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropoltian_Subway/"
filename = "robots.txt"
robot = requests.get("https://en.wikipedia.org/" + filename)
# print(robot.text)
# print(url)

# print("===========================")
# print(resp.text)
# print("\n")


resp = requests.get(url)
html_src =resp.text

soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("=============================================\n")

print(soup.head)
print("=========================================\n")

print(soup.body)
print("==========================================================\n")

print("title 태그요소:", soup.title)
print("title 태그이름:", soup.title.name)
print("title 태그 문자열:", soup.title.string)
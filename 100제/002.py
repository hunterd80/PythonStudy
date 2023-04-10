import requests

url = "http://www.python.org"
resp = requests.get(url)

html = resp.text
print(html)
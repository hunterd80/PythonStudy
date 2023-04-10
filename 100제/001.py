import requests

url = "http://www.python.org/"
resp = requests.get(url)
print(resp)

url2 = "http://www.python.org/1"
resp2 = requests.get(url2)
print(resp2)

url3 = "http://swit.io/"
resp3 = requests.get(url3)
print(resp3)

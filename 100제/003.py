import requests

urls = ["http://www.naver.com/", "http://www.python.org/", "http://swit.io/"]

filename = "robots.txt"

for url in urls:
    file_path = url + filename
    print(file_path)
    resp = requests.get(file_path)
    print(resp.text)
    print("\n")
    
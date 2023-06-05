import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropoltian_Subway"
resp = requests.get(url)
html_src =resp.text

soup = BeautifulSoup(html_src, 'html.parser')

target_img = soup.find(name='img', attrs={'src':'//upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/30px-Wiktionary-logo-v2.svg.png'})
# target_img = soup.find(name='img', attrs={'alt':'Seoul-metro-2009-20180916-103548.jpg'})
print('HTML 요소',target_img)
print('\n')

target_img_src = target_img.get('src')
print('이미지 파일 경로', target_img_src)
print('\n')

target_img_resp = requests.get('http:' + target_img_src)
out_file_path = "./100제/output/download_image.jpg"

with open(out_file_path, "wb") as out_file:
    out_file.write(target_img_resp.content)
    print('이미지 파일로 저장하였습니다.')

# 파일명 : 30px-Wiktionary-logo-v2.svg.png

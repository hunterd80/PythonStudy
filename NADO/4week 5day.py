# language = input("어떤 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어 입니다.".format(language))

print(dir())
import random
print(dir())
import pickle
print(dir())
import random
print(dir(random))

lst = [1,2,3]
print(dir(lst))

name = "JIm"
print(dir(name))

import glob
# print(glob.glob("c://Users/USER/Desktop/PythonWorkspace/nado/*.*"))
print(glob.glob("./NADO/*.*"))

import os
# print(os.getcwd())
folder = "sample_dir"
if os.path.exists(folder):
    print("이미 존재하는 폴더 입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제 했습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성했습니다.")    

print(os.listdir("./NADO/"))

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난 지 100일은", today + td)

import byme
byme.sign()


print("ab" + "ab")
print("ab" , "ab")

print("나는 %d살입니다." %20)
print("나는 %s을 좋아합니다."%"파이썬")
print("apple은 %c로 시작해요." %"A")
print("나는 %s살입니다."%20)

print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨강"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨강", age=20))

age =20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("백문이 불여일견\n 백견이 불여일타")
print("저는 \"나도코딩\"입니다.")

print("C:\\User\\Nadocoding\\Desktop\\PythonWorkspace")
print(r"C:\User\Nadocoding\Desktop\PythonWorkspace")

print("Red Apple \rPine")

url = "http://naver.com"
dotcount = url.find(".")
domain = url[7:dotcount]

a = domain[:3]
b = str(len(domain))
c = str(domain.count("e"))

print( url +"의 비밀번호는"+a+b+c+"!입니다.")

url = "http://daum.net"
dotcount = url.find(".")
domain = url[7:dotcount]

a = domain[:3]
b = str(len(domain))
c = str(domain.count("e"))

print( url +"의 비밀번호는"+a+b+c+"!입니다.")

url = "http://google.com"
dotcount = url.find(".")
domain = url[7:dotcount]

a = domain[:3]
b = str(len(domain))
c = str(domain.count("e"))

print( url +"의 비밀번호는"+a+b+c+"!입니다.")

url = "http://youtube.com"
dotcount = url.find(".")
domain = url[7:dotcount]

a = domain[:3]
b = str(len(domain))
c = str(domain.count("e"))

print( url +"의 비밀번호는"+a+b+c+"!입니다.")



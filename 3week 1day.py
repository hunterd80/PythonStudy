def profile(name, age, main_lang):
    print(name, age, main_lang)
    # print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}".format(name, age, main_lang))
    
# profile("찰리")
# profile("찰리", 22)
# profile("찰리", 24, "자바")
# profile("루시")

profile(name="찰리", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="루시")

profile("찰리", 20, "파이썬")

def profile1(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end ="")
    print(lang1, lang2, lang3, lang4, lang5)

profile1("찰리", 20, "파이썬", "자바", "c", "c++", "c#")
profile1("루시", 25, "코틀린", "스위프트", "", "", "")
    

def profile2(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end ="")
    print(language, type(language))

profile2("찰리", 20, "파이썬", "자바", "c", "c++", "c#")
profile2("루시", 25, "코틀린", "스위프트", "", "", "")
print("--------------------")


def profile3(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end ="")
    
    # #print(language, type(language))
    for lang in language:
        print(lang, end=" ")
    print()

profile3("찰리", 20, "파이썬", "자바", "c", "c++", "c#", "자바스크립트")
profile3("루시", 25, "코틀린", "스위프트")

print()

glasses = 10

def rent(people):
    global glasses 
    glasses = glasses - people
    print("[함수내부] 남은 3d 안경 개수 : {0}".format(glasses))

print("전체 3d 안경 개수 : {0}".format(glasses))
rent(2)
print("남은 3d 안경 개수 : {0}".format(glasses))

print()
glasses = 10

def rent_return(glasses, people):
    glasses = glasses - people
    print("[함수내부] 남은 3d 안경 개수 : {0}".format(glasses))
    return glasses
print("전체 3d 안경 개수 : {0}".format(glasses))
glasses = rent_return(glasses, 2)
print("남은 3d 안경 개수 : {0}".format(glasses))


def std_weight(height, gender):
    if gender == "남자":
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height*100, round(height * height * 22,2)))
              
    elif gender == "여자":
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height*100, round(height * height * 21,2)))
        
kk=float(input("키는 몇 미터"))
sex = str(input("성별 남자?여자?"))
# print(kk)
# print(sex)

std_weight(kk, sex)

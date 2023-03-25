# answer = input("아무 값이나 입력")
# print("입력한 값은" + answer + "입니다.")
# print(type(answer))
# print(type(int(answer)))
# answer =10
# print(type(answer))


print("파이썬" , "자바")
print("파이썬" + "자바")
print("파이썬" , "자바" , sep=",")

print("파이썬" , "자바", "자바스크립트" , sep=" vs ")

print("파이썬" , "자바" , sep=",", end="? ")
print("무엇이 더 재미")

import sys
print("파이썬" , "자바", file=sys.stdout)
print("파이썬" , "자바", file=sys.stderr)

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3))
    
print("{0}".format(500))
print("{0: >10}".format(500))

print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print()
print("{0:_<10}".format(500))

print("{0:,}".format(100000000000))
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

print("{0:^<+30,}".format(100000000000))

print("{0:.2f}".format(5/3))

print("{0:_>+5}".format(100))
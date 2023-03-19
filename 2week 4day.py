for waiting_no in [1,2,3,4,5]:
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(1,6,2):
    print("대기번호 : {0}".format(waiting_no))
    
orders = ["이이언맨", "토르", "스파이더맨"]
for customer in orders:
    print("{0}님, 커피가 준비됐습니다. 픽업대로 와주세요.".format(customer))
    
customer = "토르"
index = 5

while index >= 1:
    print("{} 님, 커피가 준비됬습니다.".format(customer))
    index -= 1
    print("{} 번 남았어요.".format(index))
    if index == 0:
        print("커피는 페기 처분합니다.")

# customer = "아이언맨"
# index = 1

# while True:
#     print("{0}님, 커피가 준비됬습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = None

# while person != customer:
#     print("{0}님, 커피가 준비됐습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
    
absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요.".format(student))
        break
    print("{0}번 학생, 책을 읽어 보세요.".format(student))
        
student = [1,2,3,4,5]
print(student)

student = [ i + 100 for i in student]
print(student)

student = ["Iron man", "Thor", "Spider Man"]
print(student)

student = [ len(i) for i in student]
print(student)

import random
count = 0
for sonnim  in range(1,51):
    time = random.randrange(1,51)
    if 5 <= time <= 15:
        print("[0] {0} 번째 손님(소요시간 : {1}분)".format(sonnim, time))
        count += 1
    else:
        print("[] {0} 번째 손님(소요시간 : {1}분)".format(sonnim, time))
print("총 탑슨객 : {}명".format(count))
    
                 
    
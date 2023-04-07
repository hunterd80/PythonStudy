# class bigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self) :
#         return "[오류 코드 001]" + self.msg
# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         # raise ValueError
#         raise bigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
# except bigNumberError as err:
#     print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")
    
chicken = 10
waiting = 1

class SoldOutError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
        

while True:
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문 하시겠습니까?"))
    
        if order > chicken:
            # print("재료가 부족합니다.")
            raise SoldOutError("재료 소진돼 더이상 주문을 받지 않습니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문했습니다.".format(waiting,order))
            waiting += 1
            chicken -= order
    except ValueError:
        print("값을 잘못 입력 했슈")
    except SoldOutError as err:
        print(err)
        break


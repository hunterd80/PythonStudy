def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()

def deposit(balance, money):
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance+money))
    return balance+money


def withdrew_night(balance, money):
    commission = 100
    print("업무 시간외에 {}원을 출금했습니다.".format(money))
    return commission, balance -money - commission

def withdrew(balance, money):
    if balance >= money:
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance-money))
        return balance -money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance



balance = 0
balance = deposit(balance, 1000)

commission, balance = withdrew_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# 출금
# balance = withdrew(balance, 2000)
# balance = withdrew(balance, 500)
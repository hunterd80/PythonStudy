try:
    print("나누기 전용 계산기 입니다.")
    # num1 = int(input("첫 번째 순자를 입력하세요 : "))
    # num2 = int(input("두 번째 순자를 입력하세요 : "))
    # print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
    nums =[]
    nums.append(int(input("첫 번째 숫자를 입력하세요 ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
   print("오류 발생! 잘못된 값을 입력했습니다.") 
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알수 없는 오류가 발생했습니다.")
    print(err)
    
    
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 순자를 입력하세요 : "))
    num2 = int(input("두 번째 순자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise ValueError
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
        

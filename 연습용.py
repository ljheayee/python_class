##temp = int(input("현재 온도를 입력하세요:"))
##
##if temp >= 25:
##    print("반바지를 쳐입으세요.")
##else:
##    print("긴바지를 쳐입으세요.")

##import random
##x = random.randint(1,100)
##
##y = random.randint(1,100)
##print(x)
##print(y)
##z = x-y
##ans = int(input(str(x)+"-"+str(y)+"="))
##
##if z == ans:
##    print("맞았습니다")
##else:
##    print("틀렸습니다")

##num1 = int(input("정수를 입력하세요:"))
##
##if num1%2 == 0 and num1%3 == 0:
##    print("2와 3으로 나누어 집니다")
##
##elif num1%2 == 0 and num1%3 != 0:
##    print("2로만 나누어 집니다")
##elif num1%2 != 0 and num1%3 == 0:
##    print("3으로만 나누어 집니다")
##
##else:
##    print("안나눠짐")

##import random
##x = random.randint(0,99)


##num = int(input("복권 번호를 입력하세요(0~99 사이):"))
##print("당첨번호는", str(x)+"입니다")
##
##sol1 = x//10
##sol2 = x%10
##
##dig1 = num//10
##dig2 = num%10
##
##if sol1 == dig1 and sol2 == dig2:
##    print("백만원 기모리")
##elif sol1 == dig1 or sol2 == dig2:
##    print("50만원 반모리")
##else:
##    print("아쉬워~라")


##for i in range(5):
##    for j in range(10):
##        print("*",end="")
##    print("")
##
##for z in range(1,15):
##    for y in range(1,z+1,):
##        print("*",end="")
##    for z in range(15-z,1):
##        print("*",end="")
##    print("")

sign = True

while sign:
    light = input("신호등 색깔을 입력하세요")
    if light =="blue":
        sign = False
print("전진")

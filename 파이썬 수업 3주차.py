##sec = int(input("측정 시간 입력:"))
##distance = 340*sec
##print("자신의 위치에서 번개가 친 장소까지의 거리", distance, "m")

##str1 = input("문자열을 입력하시오:")
##num1 = int(input("숫자를 입력하시오:"))
##print(str1*num1)

##import turtle
##t= turtle.Turtle()
##t.shape("turtle")
##lth = int(input("한 변의 길이를 입력하시오:"))
##clr = input(" 컬러 입력:")
##t.color(clr)
##t.begin_fill()
##t.left(90)
##t.fd(lth)
##t.right(120)
##t.fd(lth*2)
##t.left(120)
##t.fd(lth)
##t.lt(120)
##t.fd(lth*2)
##t.end_fill()


##a = int(input("첫 번째 숫자를 입력하시오:"))
##b = int(input("두 번째 숫자를 입력하시오:"))
##c = int(input("세 번째 숫자를 입력하시오:"))
##x, y, z = input(" 수 3개 입력: ").split(" ")
##x, y, z = int(x), int(y), int(z)
##
##                
##avg = (x+y+z)/3
##print("평균:", (x+y+z)/3)
##
##print("평균 =", round(avg, 2))
##print(format(round(avg,2)))
##print("평균 = %.2f"%(avg))
##print("평균 = %.0f"%(avg))

##출력형태 추가 정리
##,
##Format
##% 사용
##->%f를 사용, %와f 사이에 .과 숫자를 넣어 사용
##-> ex) print(“%.2f”%(3.7452)) -> 3.75
##
##+사용
##-> 소수점 제한시: round() 함수 사용 
##-> round() 함수는 ,와 format 와 + 에서 사용
##
##-> 실수값에서 소수점 없이 출력하고자 할 떄
##
##%0f
##Int() 함수 사용
##Round(실수값, 0)으로 출력됨을 주의


##
##p = int(input("나눔 수:"))
##q = int(input("나누는 수:"))
##print("몫:",p//q)
##print("나머지",p%q)


##x, y =-1, 3
##print(x- 4*y)
##print(-(3/x)+(9/y))
##print(x**2+6*x*y)
##print((x+y)/2*x*y)

##ftemp = int(input("화씨 온도를 입력하세요:"))
##ctemp = (ftemp -32)*5/9
##print(" 섭씨온도:",int(ftemp)) 
##
##ftemp = int(input("섭씨 온도를 입력하세요:"))
##ctemp =(9/5*ftemp)+32
##print("화씨온도:",int(ctemp))


##x1 = int(input("x1: "))
##y1 = int(input("y1: "))
##x2 = int(input("x2: "))
##y2 = int(input("y1: "))
##x1, y1 =(input("첫 번째 좌표를 입력하세요:").split(" "))
##x2, y2 =(input(" 번째 좌표를 입력하세요:")).split(" ")
##x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
##
##print("두 점 사이의 거리=%.3f "%((x2-x1)**2+(y2-y1)**2)**0.5)
##
##
##import turtle
##t = turtle.Turtle()
##t.shape("turtle")
##
##t.goto(0, 0)
##t.down()
##t.lt(45)
##t.fd(141.4)
##t.up()
##t.goto(0,0)
##t.down()
##t.setheading(0)
##t.fd(100)
##t.setheading(90)
##t.fd(100)


##import time
##fseconds = time.time() #1970년 1월 1일 부터 현재까지의 초(실수)
##total_sec =int(fseconds) #전체 초 저장
##total_min = total_sec//60 # 전체 분 저
##minute = total_min%60
##total_hour = total_min//60
##hour = total_hour%24+9
##print("현재 한국 시간:"+str(hour)+"시"+str(minute)+"분")
##


money = int(input("투입한 돈"))
price = int(input("물건 가격"))

change = money - price
print("거스름돈:",change)
coin500s = change//500
change = change%500


coin100s = change//100
print("500원 동전의 개수:",coin500s)
print("100원 동전의 개수:",coin100s)

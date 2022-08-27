##import random, turtle
##
##r= random.randint(100,250)
##t= turtle.Turtle()
##t.shape("turtle")
##
##while True:
##    cirn = int(turtle.textinput("","3,4,5,6 중 하나를 입력:"))
##    if 3<= cirn <=6:
##        for count in range(cirn):
##            t.circle(r)
##            t.left(360/cirn)
##        break
##
##for i in range(2):
##    print("c-d",end="")
##    if i<1:
##        print("-", end="")


        
##import random, turtle
##t= turtle.Turtle()
##t.shape("turtle")
##
##length = random.randint(10,300)
##
##x1 = random.randint(-300,300)
##y1 = random.randint(-300,300)
##
##r = random.random()
##g = random.random()
##b = random.random()
##
##
##
##for i in range(50):
##    length = random.randint(10,300)
##
##    x1 = random.randint(-300,300)
##    y1 = random.randint(-300,300)
##
##    r = random.random()
##    g = random.random()
##    b = random.random()
##
##    t.up()
##    t.color(r,g,b)
##    t.goto(x1,y1)
##    t.down
##    t.begin_fill()
##    
##    for j in range (4):
##        t.fd(length)
##        t.lt(90)
##    t.end_fill()
##    

##num1 = int(input("자연수 입력쓰:"))
##
##for i in range(1,num1+1):
##    if num1%i == 0:
##        print(str(i)+" ",end="")
##
##x <= num1
##
##while True:
##    num%x == 0
##    print(x,end="")
##    
##    break

##
##n = int(input("정수 1:"))
##m = int(input("정수 2:"))
##
##if n<m:
##    n, m = m, n
##
##while m>0:
##    r = n%m
##    n, m = m, r
##
##if n != 1:
##    print("두 수의 최대공약수:",n)
##else:
##    print("두 수는 서로소이다.")

##import random
##score = 100
##
##
##
##while True:
##    x = random.randint(1,3)
##    room = int(input("방번호 입력 기모링:"))
##    if x != room:
##        score -= 10
##        print("점수 감점", score)
##
##    if x == room or score == 0:
##        print("게임 오바 점수:", score)
##        break

##
##import random
##
##x = random.randint(1,100)
##tries = 0
##while True:
##    ans = int(input("정답을 입력하세요"))
##
##    if not 1<= ans <=100:
##        print("정답 범위가 아닙니다.")
##    elif ans < x:
##        tries += 1
##        print("정답보다 낮음","시도횟수:",tries)
##    elif ans > x:
##        tries += 1
##        print("정답보다 높음","시도횟수:",tries)
##    else:
##        print("정답","시도횟수:",tries)
##        break
##    if tries == 10:
##        print(" 탈락")
##        break

##for i in range(1,101):
##    if i%2 == 0:
##        print(i,end="")
##

##n = int(input("구구단 숫자 입력:"))
##
##for i in range (1,10):
##    print("%s * %s = %s"%(n, i, n*i))
##



##year = 0
##balance = 1000
##while True:
##    year += 1
##    interest = balance*0.07
##    balance += interest
##
##    if balance >= 2000:
##        print(year, "년이 걸립니다")
##        break
##


import random

x= random.randint(1,10)
y= random.randint(1,10)


while True:
    ans = int(input(str(x)+"*"+str(y)+"="))
    if ans != x*y:
        print("땡")
    elif ans == x*y:
        print("네이스")
        break

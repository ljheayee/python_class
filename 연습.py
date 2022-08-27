##import random
##x = random.randint(1,10)
##y = random.randint(30,50)
##print("x",x)
##print("y",y)
##
##su = int(input("수를 입력하세요"))
##
##sum1 = 0
##for i in range(x,y+1):
##    sum1 += i
##print("%s~%s까지의 총합은 %s"%(x, y, sum1))
##
##
##for i in range(x,y+1):
##    if i%su == 0:
##        print(i)
##       
##

##str1 = input("문자열을 입력하세요")
##str1_1 = len(str1)
##i = 1
##while i <= str1_1:
##    print(str1[:i])
#

##for i in range(1,6):
##    for j in range(1, i+1):
##        print("*", end="")
##    print()

##import turtle
##t= turtle.Turtle()
##t.shape("turtle")
##
##s= turtle.textinput("","몇 각형 그릴까?:")
##n =int(s)
##
##for i in range (n):
##    t.lt(360/n)
##    t.fd(50)


##import turtle, random
##t= turtle.Turtle()
##t.shape("turtle")
##
##for i in range(10):
##    n = random.randint(1,100)
##    ang = random.randint(-180,180)
##    t.fd(n)
##    t.lt(ang)

import random
score = 0

while True:
    room = random.randint(1,3)
    n = int(input("방 번호 입력"))

    if room == n:
        score += 100
        print("점수",str(score))
        break
    
    elif room != n:
        score -= 10
        a = score
        print("틀림",str(a))

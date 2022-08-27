##num = int(input("정수 입력:"))
##if num >= 0:
##    if num ==0:
##        print("0입니다")
##    else:
##        print("양수입니다")
##else:
##    print("음수입니다")
##    
##    true 0이외의 값/ false 0

##a, b, c = input("세 변의 숫자를 입력하세요:").split(" ")
##a, b, c = int(a), int(b), int(c)
##if c**2 == a**2+b**2:
##    print("직각삼각형 입니다")
##else:
##    print("직각삼각형이 아닙니다")

##import turtle
##t= turtle.Turtle()
##t.shape("turtle")
##
##t.up()
##t.goto(100,100)
##t.write("입력된 정수는 양의 정수입니다.")
##t.goto(100, 0)
##t.write("입력된 정수는 0입니다.")
##t.goto(100,-100)
##t.write("입력된 정수는 양의 정수입니다.")
##t.goto(0,0)
##t.down()
##
##s = turtle.textinput("","숫자를 입력하세요:")
##n = int(s)
##if n>0:
##    t.goto(100,100)
##elif n==0:
##    t.goto(100,0)
##if n<0:
##    t.goto(100,-100)


##jumin = int(input("주민번호 앞자리를 입력하세요:"))
##
##if jumin == 1 or jumin == 3:
##    print("남성입니다")
##
##elif jumin == 2 or jumin == 4:
##    print("여성입니다")
##else:
##    print("잘못입력하셨습니다")
##
##

##import random
##
##gender =random.randrange(4)
##gender = gender+1
##
##print(str(gender))
##
##if gender == 1 or gender == 3:
##    print("남성입니다")
##else:
##    print("여성입니다")
##


#import turtle, random
##import turtle
##screen = turtle.Screen()
##image1 = "img/front.gif"
##image2 = "img/back.gif"
##screen.addshape(image1)
##screen.addshape(image2)
##t1=turtle.Turtle()
##t1.shape(image1)
##
##
##import random
##coin = random.randint(0,1)
##
##if coin ==0:
##    t1.shape(image1)
##    t1.stamp()
##else:
##    t1.shape(image2)
##    t1.stamp()


##j1 = input("1번 전지가 있습니까?(y/n)")
##j2 = input("2번 전지가 있습니까?(y/n)")
##
##if j1.upper() == "Y" and j2.upper() == "Y":
##    print("직렬연결: 켜집니다")
##else:
##    print("직렬연결: 꺼집니다")
##
##if j1.upper() == "N" and j2.upper() == "N":
##    print("병렬연결: 꺼집니다")
##else:
##    print("병렬연결: 켜집니다")
##    
##
##import turtle, random
##screen = turtle.Screen()
##
##
##d1 = "img/dice1.gif"
##d2 = "img/dice2.gif"
##d3 = "img/dice3.gif"
##d4 = "img/dice4.gif"
##d5 = "img/dice5.gif"
##d6 = "img/dice6.gif"
##screen.addshape(d1)
##screen.addshape(d2)
##screen.addshape(d3)
##screen.addshape(d4)
##screen.addshape(d5)
##screen.addshape(d6)
##
##t1=turtle.Turtle()
##
##
##d = random.randint(1,6)
##
##if d == 1:
##    t1.shape(d1)
##    t1.stamp()
##elif d == 2:
##    t1.shape(d2)
##    t1.stamp()
##elif d == 3:
##    t1.shape(d3)
##    t1.stamp()
##elif d == 4:
##    t1.shape(d4)
##    t1.stamp()
##elif d == 5:
##    t1.shape(d5)
##    t1.stamp()
##else:
##    t1.shape(d6)
##    t1.stamp()



##
##year = int(input("년도 입력:"))
##
##if ((year%4 ==0) and (year%100 !=0)) or year%400 ==0:
##    print("윤년입니다")
##else:
##    print("낫 윤년입니다")

##
##a, b, c = input("ax**2+bx+c=0 에서 a,b,c를 입력하세요:").split(" ")
##a, b, c = float(a), float(b), float(c)
##
##D= b**2 -4*a*c
##
##if D>0:
##    print("서로 다른 두 실근")
##
##elif D==0:
##    print("중근")
##    
##else:
##    print("서로 다른 두 허근")
##
##
##
## 
##
##x1, y1 = input("큰원의 좌표를 입력하세요:").split(", ")
##x1, y1 = int(x1), int(y1)
##r1 = int(input("반지름을 입력하세요:"))
##yy1 = (y1-r1)
##
##
##x2, y2 = input("작은원의 좌표를 입력하세요:").split(", ")
##x2, y2 = int(x2), int(y2)
##r2 = int(input("반지름을 입력하세요:"))
##yy2 = (y2-r2)
##
##import turtle
##t= turtle.Turtle()
##t.shape("turtle")
##
##
##t.up()
##t.goto(x1,yy1)
##t.down()
##t.circle(r1)
##
##
##
##t.up()
##t.goto(x2,yy2)
##t.down()
##t.circle(r2)
##
##d = ((x1-x2)**2 + (y1-y2)**2)**0.5
##
##if d ==0:
##    turtle.write("동심원")
##elif d == r1-r2:
##    turtle.write("내접")
##elif r1 -r2< d < r1+r2:
##    turtle.write("두 점에서 만남")
##elif  d > r1+r2:
##    turtle.write("만나지 않고 외부에")
##elif  d == r1+r2:

##t.clear(): 화면 지우기
##t.hideturtle: 터틀숨기기 t.ht()
##t.showturtle: 터틀 보이기 t.st()
##t.home(): 터틀 0,0으로 이동

##    turtle.write("외접")
##elif  d < r1-r2:
##    turtle.write("만나지 않고 내부에")
##
##
##if s== "직사각형":
##    s = turtle.textinput("","가로:")
##    w = int(s)
##    s = turtle.textinput("","세로:")
##    h = int(s)
##    t.fd(w)
##    t.lt(90)
##    t.fd(h)
##    t.lt(90)
##    t.fd(w)
##    t.lt(90)
##    t.fd(h)





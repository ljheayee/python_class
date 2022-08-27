##x, y, z = input("수를 입력하시오:").split(" ")
##x, y, z = int(x), int(y), int(z)
##
##print("덧셈", x, "+", y,"+", z, "=", x+y+z)
##print("%s + %s + %s = %s "%(x, y, z, x+y+z))
##print("뺄셈", x, "-", y,"-", z, "=", x-y-z)
##print("곱셈", x, "*", y,"*", z, "=", x*y*z)
##print("나눗셈", x, "/", y, "=",x/y)
##print("지수", x, "**", y, "=",x**y)
##print("나눈 나머지", x, "%", y, "=",x%y)
##print("몫", x, "//", y, "=",x//y)

##pi = 3.14
##r = int(input("반지름 입력:"))
##h = int(input("높이 입력:"))
##print("원기둥 부피:", r**2*h*pi)


##n1 = int(input("4자리 숫자 입력:"))
##x = n1%10
##y = (n1//10)%10
##z = (n1//100)%10
##w = n1//1000
##print(x+y+z+w)


##x1, y1 = input("좌표 입력").split(",")
##x2, y2 = input("좌표 입력").split(",")
##x1, y1 = int(x1), int(y1)
##x2, y2 = int(x2), int(y2)
##
##import turtle
##t = turtle.Turtle()
##t.shape("turtle")
##t.up()
##t.goto(x1, y1)
##t.down()
##t.goto(x2, y2)
##
##dis = ((x1-x2)**2 +(y2-y1)**2)**0.5
##print("길이 계산", dis)
##t.write("길이 계산:"+str(dis))
##t.write("안녕하세요?", True, "center", ("", 15, "bold"))

##poem1 = "이렇게\n정다운"
##
##print(poem1)

##print("안녕하세요라고 \"그"\"가 말했다")
##      
##s = "python"
##a = input("기호를 입력하시오:")
##b = input("문자를 입력하시오:")
##print(a[0]+b[0::1]+a[-1])
##
##
##
##print("소금물의 농도를 구하는 프로그램입니다")
##salt = int(input("소금의 양은 몇g 입니까?"))
##water = int(input("물 양은 몇g 입니까?"))
##nong = (salt/water)*100
##print("소금물의 농도는"+str(nong)+"% 입니다")

##
##print("안녕하세요")
##name = input("이름이 뭐에요?: ")
##print("만나서 반갑습니다", name+"님")
##print(name+"님, 이름의 길이는 다음과 같군요:",len(name))
##age = int(input("나이가 어떻게 되세요?: "))
##print("내년이면", str(age+1)+"세가 되시는군요")
##


##import turtle
##t = turtle.Turtle()
##t.shape("turtle")
##t.up()
##t.goto(0,200)
##s = turtle.textinput("","이름을 입력하시오:")
##t.write("안녕하세요?"+s+"씨, 터틀 인사드립니다", True, "center", ("", 15, "bold"))
##t.goto(0,0)
##t.down()
##t.fd(100)
##t.lt(90)
##t.fd(100)
##t.lt(90)
##t.fd(100)
##t.lt(90)
##t.fd(100)
##t.lt(90)
##t.up()
##t.goto(50, 50)


##s ="도서관에서 보자"
##print("평문:",s)
##print("암호:",s[-1:-9:-1])
##
##import time
##now = time.time()
##thisYear = int(1970+now//(365*24*3600))
##print("올해는"+str(thisYear)+"년입니다")

p = input("평문 입력:")#"도서관에서 보자"
print("평문: {}".format(p))
print("암호문: {}".format(p[-1:-(len(p)+1):-1]))
print(p[0]+p[-2:-(len(p)):-1]+p[-1])

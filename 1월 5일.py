##result = 0
##def calculate_area():
##    global result
##    result = 3.14*r**2
##
##r = float(input("원의 반지름:"))
##calculate_area()
##print(result)
##
##
##def greet(name,msg):
##    print("안녕",name+','+msg)
##
##greet("철수", "좋은아침")
##print(exam1)
##
##
##import random, turtle
##t = turtle.Turtle()
##t.shape("turtle")
##
##def poly_num():
##    msg = ""
##    while True:
##        num = int(turtle.textinput("",msg+"다각형 개수를 입력하세요.:"))
##        if 10<= num <= 20:
##            break
##        else:
##            msg = "10 - 20 사이의 수를 입력하세요.\n"
##        return sum
##    
##def poly_size():
##    size = random.randint(50,100)
##    return size
##
##def random_positon():
##    x = random.randint(-200,200)
##    y = random.randint(-200,200)
##    t.up()
##    t.goto(x,y)
##    t.down()
##
##def draw_polygon(size):
##    p = [3, 4, 5, 6, 9]
##    s = random.choice(p)
##    if s == 9:
##        t.circle(size)
##    else:
##        t.circle(size,stemps=s)
##
##for i in range(poly_num()):
##    s = poly_size()
##    random_position()
##    draw_polygon(s)
##
##


##def bmi(height, weight):
##    result = weight / (height*height)
##    return result
##
##def result_print(result):
##    if result <18.5:
##        print("저체중입니다.")
##    elif result < 23:
##        print("당신은 정상입니다")
##    elif result < 25:
##        print("당신은 과체중입니다")
##    elif result < 30:
##        print("당신은 경도비만입니다")
##    else:
##        print("당신은 정상입니다")
##
##h = float(input("키 입력"))
##w = float(input("몸무게 입력"))
##
##result = bmi(h,w)
##result_print(result)
##exchange_list = [['미국', '달러', 1182.5], ['중국', '위안', 169.22], ['유럽', '유로', 1268.74], ['일본', '엔', 1078.14]]
##
##def inputinfo():
##    while True:
##        c = input("국가입력")
##        i = 0
##        while i < len(exchange_list):
##            if c in exchange_list[i]:
##                break
##            i += 1
##        if i == len(exchange_list):
##            print("해당 국가가 없습니다. 다시 입력하세요.")
##        else:
##            break
##    money = int(input("환전 금액 입력"))
##    return c, money
##
##def exchange(c,m):
##    for i in range(len(exchange_list)):
##        if c in exchange_list[i]:
##            indx = i
##            break
##        result = round(m/exchange_list[indx][2], 2)
##        print("%s원은 %s %s"%(m, result, exchange_list[indx][1]))
##        
##    
##
##
###main part
##
##country, money = inputinfo()
##exchange(country, money)


n

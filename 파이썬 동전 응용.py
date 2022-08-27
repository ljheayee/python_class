import turtle, random
screen = turtle.Screen()
front = "img/front.gif"
back = "img/front.gif"
screen.addshape(front)
screen.addshape(back)
t= turtle.Turtle()

coin1 = random.randint(0,1)
t.up()
t.goto(-150,0)
if coin1 == 0:
    t.shape(front)
else:
    t.shape(back)
t.stamp()

coin2 = random.randint(0,1)

t.goto(150,0)
if coin2 == 0:
    t.shape(front)
else:
    t.shape(back)
t.stamp()

t.ht()
t.goto(0,200)
if coin1 == coin2:
    turtle.write("성공")
else:
    turtle.write("실패")

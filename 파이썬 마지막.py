##import turtle
##
##def draw_maze(x,y):
##    for i in range(2):
##        t.pu()
##        if i ==1:
##            t.goto(x+100,y+100)
##        else:
##            t.goto(x,y)
##        t.pd()
##        t.fd(300)
##        t.rt(90)
##        t.fd(300)
##        t.lt(90)
##        t.fd(300)
##
##def turn_left():
##    t.lt(10)
##    t.fd(10)
##
##def turn_right():
##    t.rt(10)
##    t.fd(10)
##
##t = turtle.Turtle()
##screen = turtle.Screen()
##t.shape("turtle")
##t.speed(0)
##
##draw_maze(-300,200)
##screen.onkey(turn_left, "Left")
##screen.onkey(turn_right, "Right")
##
##t.pu();
##t.goto(-300,250)
##t.pd();
##screen.listen()
##screen.mainloop()



d1 = dict()
d1["Name"] = "홍길동"
d1["Age"] = 7
d1["Class"] = "초급"
print(d1)
print(d1["Name"])

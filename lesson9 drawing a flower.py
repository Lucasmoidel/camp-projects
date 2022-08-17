import turtle
myT = turtle.Turtle()
myT.speed(0)
def petal(myT):
    myT.fillcolor("red")
    startdirection = myT.heading()
    myT.pendown()
    myT.begin_fill()
    myT.lt(32)
    for x in range(5):
        myT.fd(20)
        myT.rt(16)
    myT.rt(100)
    for x in range(5):
        myT.fd(20)
        myT.rt(16)
    myT.penup()
    myT.end_fill()
    myT.setheading(startdirection)
def circle(myT):
    myT.fillcolor("yellow")
    myT.penup()
    myT.setheading(0)
    myT.goto(-1.75, 20)
    myT.pendown()
    myT.begin_fill()

    for x in range (36):
        myT.forward(3.5)
        myT.right(10)
    myT.end_fill()
    myT.penup()
myT.home()
myT.rt(22.5)
for p in range(8):
    petal(myT)
    myT.lt(45)
circle(myT)
myT.hideturtle()
turtle.done()

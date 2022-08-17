import turtle

myT = turtle.Turtle()
myT.speed(0)

def petal(T):
    T.fillcolor("red")

    startdirection = T.heading()

    T.pendown()
    T.begin_fill()
    T.lt(32)

    for x in range(5):
        T.fd(20)
        T.rt(16)

    T.rt(100)
    
    for x in range(5):
        T.fd(20)
        T.rt(16)

    T.end_fill()
    T.penup()
    T.setheading(startdirection)

def stem(T):

    T.fillcolor("green")
    T.penup()
    T.goto(-3, 0)

    T.pendown()
    T.begin_fill()
    T.goto(-3, -300)
    T.goto(3, -300)
    T.goto(3, 0)
    T.end_fill()
    T.penup()

def circle(T):

    T.fillcolor("yellow")
    T.penup()
    T.setheading(0)
    T.goto(-1.75, 20)

    T.pendown()
    T.begin_fill()

    for x in range(36):
        T.forward(3.5)
        T.right(10)

    T.end_fill()
    T.penup()

stem(myT)
myT.home()
myT.rt(22.5)
for p in range(8):
    petal(myT)
    myT.rt(45)
circle(myT)
myT.hideturtle()

turtle.done()

import turtle
T = turtle.Turtle()
T.speed(0)
h = 30
w = 15
T.pencolor("red")
T.left(90)
for i in range(5):
    for i in range(4):
        T.forward (50)
        T.rt(90)
    T.forward (50)
T.rt(90)
T.fd(50)
T.rt(90)
T.fd(250)
T.lt(180)
for i in range(4):
    for i in range(4):
        T.forward (50)
        T.rt(90)
    T.forward (50)
T.rt(90)
T.fd(50)
T.rt(90)
T.fd(200)
T.lt(180)
for i in range(3):
    for i in range(4):
        T.forward (50)
        T.rt(90)
    T.forward (50)
T.rt(90)
T.fd(50)
T.rt(90)
T.fd(150)
T.lt(180)
for i in range(2):
    for i in range(4):
        T.forward (50)
        T.rt(90)
    T.forward (50)
T.rt(90)
T.fd(50)
T.rt(90)
T.fd(100)
T.lt(180)
for i in range(1):
    for i in range(4):
        T.forward (50)
        T.rt(90)
    T.forward (50)
T.lt(180)
T.fd(50)
T.rt(90)
T.fd(200)

turtle.done()

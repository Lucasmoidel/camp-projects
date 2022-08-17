import turtle
T = turtle.Turtle()
T.speed(0)
#h = 60
#w = 30
times = 0
T.left(90)
T.pencolor("red")
for i in range(4):
    T.lt(90)
    h = 60
    w = 30
    for i in range(5):
        T.forward (h)
        T.rt(90)
        T.forward (w)
        T.rt(90)
        T.forward (h)
        T.rt(90)
        T.forward (w)
        T.rt(90)
        h = h + 10
        w = w + 10
turtle.done()

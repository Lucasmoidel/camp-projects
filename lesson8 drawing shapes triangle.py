import turtle
T = turtle.Turtle()
T.speed(0)
T.fillcolor("green")
T.begin_fill()
for i in range(3):
    T.left(120)
    T.forward(100)
    T.end_fill()
turtle.done()

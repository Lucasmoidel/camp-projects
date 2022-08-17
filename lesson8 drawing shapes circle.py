import turtle
T = turtle.Turtle()
T.speed(0)
T.color("blue")
for i in range(36):
    T.forward(10)
    T.right(10)
    T.end_fill()
turtle.done()

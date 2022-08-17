import turtle

T = turtle.Turtle()
T.speed(1)

T.penup()
T.goto(-150, 100)

T.color("red")
T.begin_fill()
T.pendown()
T.forward(100)
T.right(90)
T.forward(100)
T.right(90)
T.forward(100)
T.right(90)
T.forward(100)
T.right(90)
T.penup()
T.end_fill()

T.goto(150, 0)

T.color("green")
T.begin_fill()
T.pendown()
T.left(120)
T.forward(100)
T.left(120)
T.forward(100)
T.left(120)
T.forward(100)
T.penup()
T.end_fill()

T.goto(0, -50)

T.color("blue")
T.begin_fill()
T.pendown()
for i in range(36):
    T.forward(10)
    T.right(10)
T.penup()
T.end_fill()

turtle.done()

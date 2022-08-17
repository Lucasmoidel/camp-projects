import turtle   # Import the turtle library

T = turtle.Turtle()   # Create a new turtle named T
T.speed(1)   # Set the turtle's speed to maximum

T.penup()   # Lift the pen so the turtle doesn't draw
T.goto(-150, 100)   # Move the turtle to the upper left corner

# Draw a square
T.pendown()   # Place the pen down so the turtle draws
T.forward(100)   # Move the turtle forward ( Can also use T.fd(100) )
T.right(90)      # Turn the turtle right ( Can also use T.rt(90) )
T.forward(100)
T.right(90)
T.forward(100)
T.right(90)
T.forward(100)
T.right(90)
T.penup()   # Lift the pen since we're done drawing this shape

T.goto(150, 0)   # Move the turtle to the right side

# Draw a triangle
T.pendown()   # Put the pen down to start drawing the shape
T.left(120)      # Turn the turtle left ( Can also use T.lt(120) )
T.forward(100)
T.left(120)
T.forward(100)
T.left(120)
T.forward(100)
T.penup()   # Lift the pen since we're done drawing this shape

T.goto(0, -50)   # Move the turtle to the bottom middle

# Draw a circle
T.pendown()   # Place the pen down to start drawing
for i in range(36):   # 36 times, do the following:
    T.forward(10)   # Move the turtle forward a small amount
    T.right(10)     # Turn the turtle right a small amount
T.penup()   # Lif the pen since we're done drawing

turtle.done()   # Tell Python that we're done drawing with the turtle

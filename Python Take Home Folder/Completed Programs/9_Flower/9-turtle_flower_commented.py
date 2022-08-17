import turtle   # Import the turtle library

myT = turtle.Turtle()   # Create a new turtle
myT.speed(0)   # Set the turtle's speed to maximum

# Function to draw a petal at the current position
def petal(T):
    T.fillcolor("red")
    # Save the turtle's starting rotation
    startdirection = T.heading()

    # Start drawing the petal
    T.pendown()
    T.begin_fill()
    T.lt(32)

    # Draw one edge of the petal
    for x in range(5):
        T.fd(20)
        T.rt(16)

    # Rotate the turtle
    T.rt(100)

    # Draw the other edge of the petal
    for x in range(5):
        T.fd(20)
        T.rt(16)

    # Move the turtle back to its starting location
    T.end_fill()
    T.penup()
    T.setheading(startdirection)

# Function for drawing a circle
def circle(T):
    # Position the turtle
    T.fillcolor("yellow")
    T.penup()
    T.setheading(0)
    T.goto(-1.75, 20)

    # Start drawing the circle
    T.pendown()
    T.begin_fill()

    for x in range(36):
        T.forward(3.5)
        T.right(10)

    T.end_fill()
    T.penup()

# Use the functions defined earlier to draw a flower
myT.home()   # Return the turtle to its default position
myT.rt(22.5)
for p in range(8):   # Repeat this block 8 times:
    petal(myT)     # Draw a petal
    myT.rt(45)     # Rotate the tutle 45 degrees
circle(myT)    # Draw a circle of radius 50
myT.hideturtle()   # Hide the turtle after drawing everything

turtle.done()   # Set the turtle window to close when clicked

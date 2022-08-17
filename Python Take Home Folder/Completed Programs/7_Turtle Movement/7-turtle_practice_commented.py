import turtle   # Import the turtle module

T = turtle.Turtle()   # Create a new turtle, and store it in the variable T

# Place a background image behind the turtle
screen = T.getscreen()   # Get the screen that the turtle is using
screen.bgpic("goal.gif") # Set the background image of the screen

T.shape("turtle")   # Set the turtle's shape to be a turtle

# Move the turtle below the obstacle
T.speed(1)           # Set the turtle's speed to the slowest setting

# Start moving the turtle by using the rt, lt, and fd functions
# (Have students try to figure out this section, given the appropriate syntax)
T.right(30)    # Turn the turtle right 30 degrees
T.forward(100)   # Move the turtle forward 100 pixels
T.left(30)    # Turn the turtle left 30 degrees
T.forward(100)   # Move the turtle forward again
T.left(30)    # Turn the turtle left 30 degrees
T.forward(100)   # Move the turtle forward into the goal

turtle.done()   # Stop using the turtle

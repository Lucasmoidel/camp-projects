"""

###PART ONE###

"""

import turtle   # Import the turtle module

# Give the player instructions on how to move
print("Type commands to move the green turtle between his blue turtle parents")
print("This turtle doesn't know how to float so don't move into the water")
print("Avoid the snake in the middle of the road")
print("Use the commands 'lt' and 'rt' to turn the turtle")
print("and use 'fd' to move the turtle forward.")
print("Type 'q' to quit.")

#Create a green turtle and move it to the starting point
myT = turtle.Turtle()   # Create a new turtle, and store it in the variable myT
myT.shape("turtle")   # Set the turtle's shape to be a turtle
myT.color("green")      #Set player turtle color to green
myT.penup()        # Lift the pen so that the turtle doesn't draw when we move it
myT.speed(0)           # Set the turtle's speed to the fastest setting
myT.goto(0,-100)   #Set player at starting position
myT.left(90)        #Turn turtle left to face up
myT.speed(1)           # Set the turtle's speed to the slowest setting

# Place a background image behind the turtle
screen = myT.getscreen()   # Get the screen that the turtle is using
screen.bgpic("street2.gif") # Set the background image of the screen

#Create two blue parent turtles as a goal line
dadT = turtle.Turtle()  #create turtle for dad
momT = turtle.Turtle()  #create turtle for mom
momT.shape("turtle")   # Set the turtle's shape to be a turtle
momT.color("blue")      #Set the turtle's color to blue
dadT.shape("turtle")   # Set the turtle's shape to be a turtle
dadT.color("blue")      #Set the turtle's color to blue
momT.penup()        #Lift pen so turtle doesn't draw
dadT.penup()        #Lift pen so turtle doesn't draw
momT.speed(0)        # Set the turtle's speed to the fastest setting
dadT.speed(0)        # Set the turtle's speed to the fastest setting
momT.goto(-25, 100)     #Set turtle position at the left of goal line
dadT.goto(25, 100)       #Set turtle position at the right of goal line
momT.left(90)       #Turn turtle left to face up
dadT.left(90)       #Turn turtle left to face up

"""

###PART TWO###

"""

# Set a variable "location" representing myT's position


"""

###PART THREE###

"""

# Repeat the following until the player reaches the goal
while(True): # So long as the player isn't at the goal
    command = input("Direction: ")   # Prompt the player for input
    # Do the command the player puts in
    if(command == "rt"):
                        #add code to turn myT to the right 90 degrees
    elif(command == "lt"):
                        #add code to turn myT to the left 90 degrees
    elif(command == "fd"):
                        #add code to move myT 50 pixels forward
    elif(command == "q"):
        print("Quitting")
        break        #break from while loop to end game
    else:
        # Tell the player if they put in an invalid command
        print("Not a valid command")

    """

    ###PART FOUR###

    """

print("Game Over")

turtle.bye()    # Shut the turtle graphics window

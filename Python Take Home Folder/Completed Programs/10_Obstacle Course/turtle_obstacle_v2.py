import turtle   # Import the turtle module

# Give the player instructions on how to move
print("Type commands to move the green turtle between his blue turtle parents")
print("This turtle doesn't know how to float so don't move into the water")
print("Avoid the snake in the middle of the road")
print("Use the commands 'lt' and 'rt' to turn the turtle")
print("and use 'fd' to move the turtle forward.")
print("Type 'q' to quit.")

myT = turtle.Turtle()   # Create a new turtle, and store it in the variable myT

# Place a background image behind the turtle
screen = myT.getscreen()   # Get the screen that the turtle is using
screen.bgpic("street2.gif") # Set the background image of the screen

myT.shape("turtle")   # Set the turtle's shape to be a turtle
myT.color("green")      #Set player turtle color to green

#Create parent turtles as a goal line
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

# Move the turtle below the obstacle
myT.speed(0)           # Set the turtle's speed to the fastest setting
myT.penup()        # Lift the pen so that the turtle doesn't draw when we move it
myT.goto(0,-100)   #Set player at starting position
myT.left(90)        #Turn turtle left to face up
myT.speed(1)           # Set the turtle's speed to the slowest setting
location = myT.position()   # Set a variable representing its location

# Repeat the following until the player reaches the goal
while(True): # So long as the player isn't at the goal
    command = input("Direction: ")   # Prompt the player for input
    # Do the command the player puts in
    if(command == "rt"):
        myT.right(90)
    elif(command == "lt"):
        myT.left(90)
    elif(command == "fd"):
        myT.forward(50)
    elif(command == "q"):
        print("Quitting")
        break        #break from while loop to end game
    else:
        # Tell the player if they put in an invalid command
        print("Not a valid command")
        
    location = myT.position()   # Set location to the current position
    if(int(location[0]) == 0 and int(location[1]) == 100): #check if location is between the parents (0,100)
        print("Nice job! You got to the turtle back to its family!")
        break     #break from while loop to end game
    if(int(location[0]) > 50 or int(location[0]) < -50): #check if location is in the water
        print("You fell in the water!")
        break     #break from while loop to end game
    if(int(location[0]) == 0 and int(location[1]) == 0): #check if location is on the snake (0,0)
        print("You ran into the snake!")
        break     #break from while loop to end game

print("Game Over")

turtle.bye()    # Shut the turtle graphics window

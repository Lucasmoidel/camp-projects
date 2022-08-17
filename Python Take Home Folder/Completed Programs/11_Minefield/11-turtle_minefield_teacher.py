"""
###PART ONE###
"""

import turtle   # Import the turtle module
import random   # Import the random module

Tom = turtle.Turtle()   # Create a new turtle named Tom
Tom.speed(0)            # Set Tom's movement speed to the fastest
Tom.pencolor("red")     # Set the color of the line Tom draws behind him
Tom.penup()   # Lift the pen so that Tom doesn't draw when we move him

screen = Tom.getscreen()   # Set a variable screen to the screen Tom is using
screen.setup(400, 400, -100, 100) #setup screen dimension and placement
screen.bgpic("obstacle_course.gif")    # Set the background image

obstacles = []   # Create an empty list of obstacles (will be filled later)
tries = 3   # Give the player three tries to get through the course
gridsize = 50 #the screen will be a grid, this will be the size of each grid

pos = (0, -2)    # Set the player's position
goal = (0, 2)    # Set the goal's position

# Give the player instructions on how to move
print("Type commands to move Tom through the obstacle course.")
print("Watch out for the hidden obstacles!")
print("You have " + (str)(tries) + " tries to make it through.")
print("Type 'up', 'down', 'left', or 'right' to move Tom.")
print("Type 'quit' to quit.")

"""
###PART TWO###
"""

# Place five obstacles in the grid at random positions
for i in range(5):
    temp = pos   # Set a temporary variable to the current position    
    # Don't place obstacles in the same place, or on the player's start or goal
    while(temp == pos or temp == goal or temp in obstacles): #while temp is not valid
        tempx = random.randint(-2, 2)   # Get a random x in the grid
        tempy = random.randint(-2, 2)   # Get a random y in the grid
        temp = (tempx, tempy)   # Set temp to the random position
    obstacles.append(temp)   # If it's a valid position, place an obstacle here

"""
###PART THREE###
"""

# Move the turtle to a specific grid cell
def moveto(coordinates, T):
    T.goto(coordinates[0] * gridsize, coordinates[1] * gridsize)

"""
###PART FOUR###
"""

# Show the player that they hit an obstacle
def showobstacle(coordinates):
    # Create a new turtle, and position it at the obstacle cell
    hit = turtle.Turtle()
    hit.hideturtle()#We want the turtle to draw an X, we dont want to see it
    hit.pencolor("red")
    hit.speed(0)
    hit.penup()
    #Here we need to add code to call our moveto() function to move our X to the coordinates given
    moveto(coordinates, hit)
    hit.setheading(45)
    hit.fd(25)
    hit.rt(180)
    # Draw an X on the obstacle cell
    hit.pendown()
    hit.fd(50)
    hit.rt(180)
    hit.fd(25)
    hit.lt(90)
    hit.fd(25)
    hit.rt(180)
    hit.fd(50)

moveto(pos, Tom)   # Set Tom to the starting position for the maze
Tom.setheading(90)  # Turn Tom to face upwards
Tom.pendown()   # Put the pen down to start drawing a line again

"""
###PART FIVE###
"""

# Repeat the following until the player reaches the goal
while(pos != goal): # So long as Tom isn't at the goal
    command = input("Direction: ")   # Prompt the player for input
    x = pos[0]
    y = pos[1]
    # Set x and y to the new coordinates, if they're within the grid
    if(command == "right" and x < 2):
        Tom.setheading(0)
        x += 1
    elif(command == "up" and y < 2):
        Tom.setheading(90)
        y += 1
    elif(command == "left" and x > -2):
        Tom.setheading(180)
        x -= 1
    elif(command == "down" and y > -2):
        Tom.setheading(270)
        y -= 1
    elif(command == "quit"):
        break
    else:
        # Tell the player if they put in an invalid command
        print("Not a valid command")

    # Set the position to the new coordinates, and move there
    pos = (x, y)
    moveto(pos, Tom)

    """
    ###PART SIX###
    """

    # If the new position was in the list of obstacles, tell the player
    if pos in obstacles:
        print("You hit an obstacle!")
        showobstacle(pos)
        tries -= 1   # Take away one try from the player
        if(tries == 0):
            break    # No more tries so game over
        else:
            # Reset the player's position
            Tom.penup()
            pos = (0, -2)      # Set the position to move to
            moveto(pos, Tom)  # Move to that position
            Tom.setheading(90)
            Tom.pendown()
            
# If the player is at the goal, congratulate them for winning
if(pos == goal):
    print("Nice job! You got to the goal!")
else:
    print("Game over!")
   
turtle.bye()   # Set the turtle window to close
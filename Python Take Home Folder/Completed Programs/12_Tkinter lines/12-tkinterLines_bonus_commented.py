# Import * so that writing "Tkinter.something()" isn't necessary
from tkinter import *
import random

myTk = Tk()   # Create the Tk object

# Create elements to place on the screen
canvas = Canvas(myTk, width=400, height=400) # Create a canvas
canvas.pack()   # Pack the canvas onto the screen

# Define a random color list to use for the lines
colorlist = ["red", "green", "blue"]

# Draw a random line on the canvas
def drawline():
    # Get a random endpoint
    x = random.randint(0, 400)
    y = random.randint(0, 400)

    """
    # For the bottom-right drawing in Part 6
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    
    # Extra set of random coordinates
    x2 = random.randint(200, 400)
    y2 = random.randint(200, 400)
    """
    
    # Choose a random element from the list of colors
    color = random.choice(colorlist)
    canvas.create_line(200, 200, x, y, fill=color)

    """
    # For the bottom-right drawing in Part 6
    # (Also comment the create_line() call above this)
    canvas.create_line(100, 100, x2, y2, fill=color)
    canvas.create_line(300, 300, x, y, fill=color)
    """
    

# Run the update function for myTk in a loop
while True:
    drawline()   # Draw a random line
    myTk.update()   # Update the screen

myTk.destroy()   # When the player has pressed the quit button, destroy myTk

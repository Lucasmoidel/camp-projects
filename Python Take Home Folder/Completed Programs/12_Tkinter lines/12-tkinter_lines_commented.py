# Import * so that writing "Tkinter.something()" isn't necessary
from tkinter import *
import random

myTk = Tk()   # Create the Tk object

# Create elements to place on the screen
canvas = Canvas(myTk, width=400, height=400) # Create a canvas
canvas.pack()   # Pack the canvas onto the screen

# Draw a random line on the canvas
def drawline():
    # Get a random endpoint
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.create_line(200, 200, x, y)   # Draw a line from the center

# Run the update function for myTk in a loop
while True:
    drawline()   # Draw a random line
    myTk.update()   # Update the screen

myTk.destroy()   # When the player has pressed the quit button, destroy myTk

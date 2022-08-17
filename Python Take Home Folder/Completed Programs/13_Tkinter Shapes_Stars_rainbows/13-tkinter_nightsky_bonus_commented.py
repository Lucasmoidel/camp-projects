# Import * so that writing "Tkinter.something()" isn't necessary
from tkinter import *
import random
import time

myTk = Tk()   # Create the Tk object

# Create elements to place on the screen
canvas = Canvas(myTk, width=400, height=400, bg="black") # Create a black canvas
canvas.pack()   # Pack the canvas onto the screen

# Create a list of colors that the stars can use
starcolors = ["yellow", "gray30", "gray50", "gray70", "gray90", "gray95", "white"]
# Create a list of colors that the lights on the tree can use
lightcolors = ["red", "orange", "yellow", "blue", "violet", "white"]

# Draw a circle on the canvas with the specified position, size, and color
def drawcircle(cx, cy, radius, color):
    # Find the corner points given the radius
    x1 = cx - radius
    x2 = cx + radius
    y1 = cy - radius
    y2 = cy + radius
    
    # Draw a circle centered on (cx, cy)
    canvas.create_oval(x1, y1, x2, y2, fill=color)

# Run the update function for myTk in a loop
while True:
    canvas.delete("all")   # Delete everything to speed up processing

    # Draw a triangular mountain
    canvas.create_polygon(0, 400, 100, 350, 200, 400, fill="gray30")

    # Draw some stars
    c = random.choice(starcolors)
    drawcircle(50, 50, 4, c)
    c = random.choice(starcolors)
    drawcircle(150, 100, 3, c)
    c = random.choice(starcolors)
    drawcircle(250, 25, 4, c)
    c = random.choice(starcolors)
    drawcircle(100, 200, 3, c)
    c = random.choice(starcolors)
    drawcircle(300, 150, 3, c)
    c = random.choice(starcolors)
    drawcircle(350, 100, 4, c)
    c = random.choice(starcolors)
    drawcircle(200, 200, 4, c)

    # Draw a tree
    canvas.create_polygon(350, 300, 325, 400, 375, 400, fill="darkgreen")

    # Draw lights on the tree
    c = random.choice(lightcolors)
    drawcircle(345, 350, 3, c)
    c = random.choice(lightcolors)
    drawcircle(360, 375, 3, c)
    c = random.choice(lightcolors)
    drawcircle(350, 325, 3, c)
    c = random.choice(lightcolors)
    drawcircle(340, 385, 3, c)
    
    myTk.update()   # Update the screen
    time.sleep(0.05)   # Wait a fraction of a second before looping

myTk.destroy()   # When the player has pressed the quit button, destroy myTk

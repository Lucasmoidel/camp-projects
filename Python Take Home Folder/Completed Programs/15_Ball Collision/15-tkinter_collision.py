# import * so that we don't have to type Tkinter.function() for everything
from tkinter import *
import time
import random

myTk = Tk()   # Create the Tk interface object
canvas = Canvas(myTk, width=400, height=400)   # Create a canvas object
canvas.pack()   # Pack the canvas onto the screen

# Create a circle centered at (200, 200)
c = canvas.create_oval(180, 180, 220, 220, fill="blue")
x=random.randint(0, 380)
y=random.randint(0, 380)
b = canvas.create_rectangle(x, y, x+20, y+20, fill = "yellow")

moveleft = False   # If the left arrow key being held
moveright = False   # If the right arrow key is being held
moveup = False   # If the up arrow key is being held
movedown = False   # If the down arrow key is being held

# Set movement variables to True when the arrow keys are pressed
def keypress(event):
    global moveleft, moveright, moveup, movedown   # Get the global variables for use
    if(event.keysym == "Left"):   # If the key symbol has "Left"
        moveleft = True   # The player has pressed the left key
    if(event.keysym == "Right"):   # If the key symbol has "Right"
        moveright = True   # The player has pressed the right key
    if(event.keysym == "Up"):   # If the key symbol has "Up"
        moveup = True
    if(event.keysym == "Down"):   # If the key symbol has "Down"
        movedown = True

# Set movement variables to False when the arrow keys are released
def keyrelease(event):
    global moveleft, moveright, moveup, movedown   # Get the global variables for use
    if(event.keysym == "Left"):   # If the key symbol has "Left"
        moveleft = False   # The player has released the left key
    if(event.keysym == "Right"):   # If the key symbol has "Right"
        moveright = False   # The player has released the right key
    if(event.keysym == "Up"):   # If the key symbol has "Up"
        moveup = False   # The player has released the up key
    if(event.keysym == "Down"):   # If the key symbol has "Down"
        movedown = False   # The player has released the down key

# Move the player if the arrow keys are being held
def movement():
    if moveleft:   # If holding the left key
        canvas.move(c, -3, 0)   # Move the player object left
    if moveright:   # If holding the right key
        canvas.move(c, 3, 0)   # Move the player object right
    if moveup:
        canvas.move(c, 0, -3)   # Move the player object up
    if movedown:
        canvas.move(c, 0, 3)   # Move the player object down

def checkhit():
    global b
    hb = canvas.bbox(c)
    hits = canvas.find_overlapping(hb[0], hb[1], hb[2], hb[3])
    if(b in hits):
        canvas.delete(b)
        x=random.randint(0, 380)
        y=random.randint(0, 380)
        b = canvas.create_rectangle(x, y, x+20, y+20, fill = "yellow")

# Bind the KeyPress/ KeyRelease events to their appropriate functions
canvas.bind_all("<KeyPress>", keypress)
canvas.bind_all("<KeyRelease>", keyrelease)

# Run the update loop for the game
while True:
    movement()
    checkhit()
    myTk.update()   # Call the myTk update function
    time.sleep(0.01)   # Wait before drawing the next frame

myTk.destroy()   # Destroy the myTk window when the player loses


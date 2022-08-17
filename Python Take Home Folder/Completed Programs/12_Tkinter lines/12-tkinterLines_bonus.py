from tkinter import *
import random

myTk = Tk()   
canvas = Canvas(myTk, width=400, height=400)
canvas.pack()   

colorlist = ["red", "green", "blue"]

def drawline():
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
    
    color = random.choice(colorlist)
    canvas.create_line(200, 200, x, y, fill=color)

    """
    # For the bottom-right drawing in Part 6
    # (Also comment the create_line() call above this)
    canvas.create_line(100, 100, x2, y2, fill=color)
    canvas.create_line(300, 300, x, y, fill=color)
    """
    
while True:
    drawline() 
    myTk.update()  

myTk.destroy() 

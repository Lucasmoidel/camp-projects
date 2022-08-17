from tkinter import *
import random
import time

myTk = Tk()   

canvas = Canvas(myTk, width=400, height=400, bg="black")
canvas.pack()  


starcolors = ["yellow", "gray30", "gray50", "gray70", "gray90", "gray95", "white"]

lightcolors = ["red", "orange", "yellow", "blue", "violet", "white"]

def drawcircle(cx, cy, radius, color):
    x1 = cx - radius
    x2 = cx + radius
    y1 = cy - radius
    y2 = cy + radius
    
    canvas.create_oval(x1, y1, x2, y2, fill=color)

while True:
    canvas.delete("all")   

    canvas.create_polygon(0, 400, 100, 350, 200, 400, fill="gray30")

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

    canvas.create_polygon(350, 300, 325, 400, 375, 400, fill="darkgreen")

    c = random.choice(lightcolors)
    drawcircle(345, 350, 3, c)
    c = random.choice(lightcolors)
    drawcircle(360, 375, 3, c)
    c = random.choice(lightcolors)
    drawcircle(350, 325, 3, c)
    c = random.choice(lightcolors)
    drawcircle(340, 385, 3, c)
    
    myTk.update()   
    time.sleep(0.05)   

myTk.destroy()  

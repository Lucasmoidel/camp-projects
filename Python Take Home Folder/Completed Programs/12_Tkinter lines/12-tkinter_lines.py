from tkinter import *
import random

myTk = Tk()
canvas = Canvas(myTk, width=400, height=400)
canvas.pack()  

def drawline():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.create_line(200, 200, x, y)  

while True:
    drawline()  
    myTk.update()  

myTk.destroy()   

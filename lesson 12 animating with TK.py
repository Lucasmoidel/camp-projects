from tkinter import *
import random
myTK = Tk()
canvas = Canvas(myTK, width=1366, height=768)
canvas.pack()
colorlist = ['red', 'green', 'blue']
def drawline():
    x=random.randint(0,1366)
    y=random.randint(0,768)
    color = random.choice(colorlist)
    canvas.create_line(683, 384, x, y, fill=color)
while True:
    drawline()
    myTK.update()
myTK.destroy()

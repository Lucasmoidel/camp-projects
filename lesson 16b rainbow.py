from tkinter import *
import random
import time
myTK = Tk()
canvas = Canvas(myTK, width=400, height=400, bg='skyblue')
canvas.pack()
colorlist = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
def drawoval(offset, color):
    x1= 75 - offset
    x2= 325 + offset
    y1= 230 - offset
    y2= 500
    canvas.create_oval(x1, y1, x2, y2, fill=color)
while True:
    canvas.delete('all')
    for i in range(5, 0, -1):
        c = random.choice(colorlist)
        drawoval(i * 8, c)
    drawoval(0, "skyblue")
    canvas.create_rectangle(0, 365, 500, 500, fill='green')
    myTK.update()
    time.sleep(0.05)
myTK.destroy()
    


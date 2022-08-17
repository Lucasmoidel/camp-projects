from tkinter import *
import random
import time
ran1 = random.randint(1, 400)
ran2 = random.randint(1, 400)
ran3 = random.randint(1, 400)
ran4 = random.randint(1, 400)
ran5 = random.randint(1, 400)
ran6 = random.randint(1, 400)
ran7 = random.randint(1, 400)
ran8 = random.randint(1, 400)
ran9 = random.randint(1, 400)
ran10 = random.randint(1, 400)
ran11 = random.randint(1, 400)
ran12 = random.randint(1, 400)
myTK = Tk()
canvas = Canvas(myTK, width=400, height=400, bg='black')
canvas.pack()
starcolors = ['yellow', 'grey30', 'grey50', 'grey70', 'grey90', 'grey95', 'white']
lightcolors = ['red', 'orange', 'yellow', 'blue', 'violet', 'white']
def drawcircle(cx, cy, radius, color):
    x1= cx - radius
    x2= cx + radius
    y1= cy - radius
    y2= cy + radius
    canvas.create_oval(x1, y1, x2, y2, fill=color)
while True:
    canvas.delete('all')
    canvas.create_polygon(0, 400, 100, 350, 200, 400, fill='grey30')
    c = random.choice(starcolors)
    drawcircle(ran1, ran2, 4, c)
    drawcircle(ran3, ran4, 4, c)
    drawcircle(ran5, ran6, 4, c)
    drawcircle(ran7, ran8, 4, c)
    drawcircle(ran9, ran10, 4, c)
    drawcircle(ran11, ran12, 4, c)
    canvas.create_polygon(350, 300, 325, 400, 375, 400, fill='darkgreen')
    ##############
    c = random.choice(lightcolors)
    drawcircle(350, 370, 3, c)
    c = random.choice(lightcolors)
    drawcircle(360, 360, 3, c)
    c = random.choice(lightcolors)
    drawcircle(350, 320, 3, c)
    ###################
    myTK.update()
    time.sleep(0.05)
myTK.destroy()

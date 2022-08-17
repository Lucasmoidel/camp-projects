from tkinter import *
import time
myTK = Tk()
canvas = Canvas(myTK, width=400, height=400)
canvas.pack()
moveleft = False
moveright = False
moveup = False
movedown = False
c = canvas.create_oval(180, 180, 220, 220, fill="blue")
def keypress(event):
    global moveleft,moveright, moveup, movedown
    if (event.keysym == "Left"):
        moveleft=True
    if (event.keysym == "Right"):
        moveright=True
    if (event.keysym == "Up"):
        moveup=True
    if (event.keysym == "Down"):
        movedown=True
def keyrelese(event):
    global moveleft,moveright, moveup, movedown
    if (event.keysym == "Left"):
        moveleft=False
    if (event.keysym == "Right"):
        moveright=False
    if (event.keysym == "Up"):
        moveup=False
    if (event.keysym == "Down"):
        movedown=False
def movement():
    if(moveleft):
        canvas.move(c, -3, 0)
    if(moveright):
        canvas.move(c, 3, 0)
    if(moveup):
        canvas.move(c, 0, -3)
    if(movedown):
        canvas.move(c, 0, 3)
canvas.bind_all("<KeyPress>", keypress)
canvas.bind_all("<KeyRelease>", keyrelese)
while True:
    movement()
    myTK.update()
    time.sleep(0.01)
myTK.destroy()

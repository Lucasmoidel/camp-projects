from tkinter import *
myTK = Tk()
smiling = False
canvas = Canvas(myTK, width=400, height=400)
canvas.pack()
def mouseclick(event):
    global smiling
    smiling = True
def mouserelease(event):
    global smiling
    smiling = False
def drawcharichter():
    canvas.create_oval(150, 150, 250, 250, fill="yellow", width=0)
    canvas.create_rectangle(150, 200, 250, 300, fill="yellow", outline="yellow")
    canvas.create_rectangle(150, 195, 250, 205, fill="black")
    canvas.create_oval(175, 175, 225, 225, fill="grey", width=0)
    canvas.create_oval(180, 180, 220, 220, fill="white", width=0)
    canvas.create_oval(195, 195, 205, 205, fill="black", width=0)
def drawmouth(smile):
    if smile:
        canvas.create_arc(175, 230, 225, 260, extent=-180, style=CHORD, fill="black")
    else:
        canvas.create_rectangle(175, 250, 225, 255, fill="black")
myTK.bind("<Button-1>", mouseclick)
myTK.bind("<ButtonRelease-1>", mouserelease)
while True:
    canvas.delete("all")
    drawcharichter()
    drawmouth(smiling)
    myTK.update()
myTK.destroy()
    


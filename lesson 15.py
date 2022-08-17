from tkinter import*
import random
myTk = Tk()
canvas = Canvas(myTk, width=400, height=400)
canvas.pack()
colorlist = ["red", "green", "blue", "orange", "yellow", "purple", "black", "white", "gold","gray","brown","pink","cyan"]
def drawline():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    color = random.choice(colorlist)
    canvas.create_line(200, 200, x, y, fill=color)
while True:
    drawline()
    myTk.update()
myTk.destroy()

                   
            


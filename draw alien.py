from tkinter import *
window = Tk()
window.title ("Alien")
c = Canvas(window, height=300, width=400)
c.pack()
body = c.create_oval(100,150,300,250, fill = "green")
eye = c.create_oval(170, 70, 230, 130, fill="white")
eyeball = c.create_oval(190, 90, 210, 110, fill="black")
mouth = c.create_oval(150,220, 250, 240, fill="red")
lips = c.create_line(150, 230, 250, 230)
eyeneck = c.create_line(200, 150, 200, 130)
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill="blue")
words = c.create_text(200, 280, text = "I am an alien!")
def mouth_open():
    c.itemconfig(mouth, fill= "black")
def mouth_closed():
    c.itemconfig(mouth, fill= "red")
def burp(event):
    mouth_open()
    c.itemconfig(words, text= "BURP!")
def unburp(event):
    mouth_closed()
    c.itemconfig(words, text= "excuse me!")
def blink():
    c.itemconfig(eye, fill= "green")
    c.itemconfig(eyeball, state= HIDDEN)
def unblink():
    c.itemconfig(eye, fill= "white")
    c.itemconfig(eyeball, state= NORMAL)
c.bind_all("<Button-1>", burp)
c.bind_all("<ButtonRelease-1>", unburp)
def asleep(avent):
    blink()
    c.itemconfig(words, text= "ZZZZZZ")
def awake(event):
    unblink()
    c.itemconfig(words, text= "good moorning")
c.bind_all("<KeyPress-a>", asleep)
c.bind_all("<KeyPress-z>", awake)
def eye_control(event):
    Key = event.keysym
    if Key == "Up":
        c.move(eyeball, 0, -5)
    elif Key == "Down":
        c.move(eyeball, 0, 5)
    elif Key == "Right":
        c.move(eyeball, 5, 0)
    elif Key == "Left":
        c.move(eyeball, -5, 0)
c.bind_all("<Key>", eye_control)
window.mainloop()

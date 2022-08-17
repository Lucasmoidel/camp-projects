from tkinter import *
import time
import random
myTK = Tk()
canvas = Canvas(myTK, width=400, height=400)
canvas.pack()
backround = PhotoImage(file="pokemon_map_v2.gif")
canvas.create_image(0, 0, anchor=NW, image=backround)
moveleft = False
moveright = False
moveup = False
movedown = False
c = canvas.create_oval(180, 180, 220, 220, fill="blue")
found = []
caught = []
fire = ['charmander', 'magmar', 'vulpix']
water = ['squirtle', 'goldeen', 'magicarp']
rock = ['onix', 'sandshrew', 'geodude']
grass = ['weedle', 'caterpie', 'oddish']

print("Welcome to pocemon safari")
print("use arrow ceys to explore 4 diffarent terrains")
print("thare are 3 diffarent pokemon for every terrain")
print("trie to cach all 12 before the timer runs out")
def temporrary_text(message):
    textbox = canvas.create_text(200, 200, font=("Pursia", 16), text=message)
    rect= canvas.create_rectangle(canvas.bbox(textbox),fill=white)
    canvas.tag_lower(rect,textbox)
    myTK.update()
    time.sleep(0.5)
    canvas.delete(textbox)
    canvas.delete(rect)
def spawn(terrain):
    pokemon=random.choice(terrain)
    print("you found", pokemon)
    if (pokemon not in found):
        found.append(pokemon)
    coinflip = random.randint(0, 1)
    if (coinflip == 0):
        print(pokemon, "ran away")
    else:
        print("you caught", pokemon)
        if (pokemon not in caught):
            caught.append(pokemon)
def encountered():
    encountered = False
    encountered_probability = random.randint(1, 50)
    pos = canvas.coords(c)
    if(encountered_probability == 1):
        encountered = True
    if(encountered):
        if(int(pos[2]) <=175 and int(pos[3]) <= 175):
            spawn(grass)
        if(int(pos[2]) <=175 and int(pos[1]) >= 225):
            spawn(water)
        if(int(pos[0]) >=225 and int(pos[1]) >= 225):
            spawn(rock)
        if(int(pos[0]) >=225 and int(pos[3]) <= 175):
            spawn(fire)
        
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
    pos = canvas.coords(c)
    if(moveleft and int(pos[0]) >= 3):
        canvas.move(c, -3, 0)
        encountered()
    if(moveright and int(pos[2]) <= 397):
        canvas.move(c, 3, 0)
        encountered()
    if(moveup and int(pos[1]) >= 3):
        canvas.move(c, 0, -3)
        encountered()
    if(movedown and int(pos[3]) <= 397):
        canvas.move(c, 0, 3)
        encountered()
canvas.bind_all("<KeyPress>", keypress)
canvas.bind_all("<KeyRelease>", keyrelese)
totalsec = 0.0
maxsec= 500.0
while True:
    movement()
    myTK.update()
    time.sleep(0.01)
    totalsec += 0.1
    if (totalsec >= maxsec):
        print("Time's up! game over!")
        break
    elif(len(caught) == 12):
        print("congrats! you caught them all!")
        break
print("you found " + str(len(found)) + " of the 12 pokemon")
if(len(found) > 0):
    print("found pokemon are:" + str(found))
print("you caught " + str(len(caught)) + " of the 12 pokemon")
if(len(caught) > 0):
    print("caught pokemon are:" + str(caught))

myTK.destroy()

#Solution - Pokemon game
from tkinter import *
import time
import random

myTk = Tk()  

w = 400 
h = 400 

# get screen width and height
ws = myTk.winfo_screenwidth() 
hs = myTk.winfo_screenheight() 

# calculate x and y coordinates for the Tk window
x = 3*(ws/4) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
myTk.geometry('%dx%d+%d+%d' % (w, h, x, y))

canvas = Canvas(myTk, width=400, height=400)   
canvas.pack()  

background = PhotoImage(file="pokemon_map_v2.gif")
canvas.create_image(0, 0, anchor=NW, image=background)

# Create a circle centered at (200, 200)
c = canvas.create_oval(180, 180, 220, 220, fill="blue")

totalsec = 0.0
maxsec = 15.0

moveleft = False   
moveright = False   
moveup = False   
movedown = False   

found = []  
caught = [] 

#list for each pokemon types
fire = ["charmander", "magmar", "vulpix"]
water = ["squirtle", "goldeen", "magicarp"]
rock = ["onix", "sandshrew", "geodude"]
grass = ["weedle", "caterpie", "oddish"]

#Beginning print message to game
print("Welcome to Pokemon Safari")
print("Use arrow keys to explore the 4 different terrains")
print("There are 3 different Pokemon for every terrain")
print("Try to find and catch all 12 before time runs out!")

def temporary_text(message):
    textbox = canvas.create_text(200, 200, font=("Purisa", 16), text=message)   #create text object to appear in middle of screen
    rect = canvas.create_rectangle(canvas.bbox(textbox),fill="white")           #create white rectangle
    canvas.tag_lower(rect,textbox)                                              #attach white rectangle behind text  
    myTk.update()   
    time.sleep(0.5)   
    canvas.delete(textbox)  
    canvas.delete(rect)    

def spawn(terrain):
    pokemon = random.choice(terrain)
    text = "You found " + pokemon
    temporary_text(text)
    if(pokemon not in found):
        found.append(pokemon)
    coinflip = random.randint(0, 1)
    if(coinflip == 0):
        text = pokemon + " ran away"
        temporary_text(text)
    else:
        text = "You caught " + pokemon
        temporary_text(text)
        if(pokemon not in caught):
            caught.append(pokemon)
            print(len(caught), text)

def encounter():
    encountered = False
    encounter_probability = random.randint(1, 100) 
    if(encounter_probability == 1):  
        encountered = True
    pos = canvas.coords(c)
    if(encountered):
        if(int(pos[2]) <= 175 and int(pos[3]) <= 175):
            spawn(grass)
        if(int(pos[2]) <= 175 and int(pos[1]) >= 225):
            spawn(water)
        if(int(pos[0]) >= 225 and int(pos[1]) >= 225):
            spawn(rock)
        if(int(pos[0]) >= 225 and int(pos[3]) <= 175):
           spawn(fire)

# Set movement variables to True when the arrow keys are pressed
def keypress(event):
    global moveleft, moveright, moveup, movedown   
    if(event.keysym == "Left"):   
        moveleft = True   
    if(event.keysym == "Right"):   
        moveright = True   
    if(event.keysym == "Up"):   
        moveup = True
    if(event.keysym == "Down"):   
        movedown = True

# Set movement variables to False when the arrow keys are released
def keyrelease(event):
    global moveleft, moveright, moveup, movedown   
    if(event.keysym == "Left"):   
        moveleft = False   
    if(event.keysym == "Right"):   
        moveright = False   
    if(event.keysym == "Up"):   
        moveup = False   
    if(event.keysym == "Down"):   
        movedown = False  

# Move the player if the arrow keys are being held
def movement():
    pos = canvas.coords(c)
    if (moveleft and int(pos[0]) >= 3):   
        canvas.move(c, -3, 0)   
        encounter()
    if (moveright and int(pos[2]) <= 397):  
        canvas.move(c, 3, 0)   
        encounter()
    if (moveup and int(pos[1]) >= 3):
        canvas.move(c, 0, -3)   
        encounter()
    if (movedown and int(pos[3]) <= 397):
        canvas.move(c, 0, 3)   
        encounter()

# Bind the KeyPress/ KeyRelease events to their appropriate functions
canvas.bind_all("<KeyPress>", keypress)
canvas.bind_all("<KeyRelease>", keyrelease)

# Run the update loop for the game
while True:
    movement()  
    myTk.update()   
    time.sleep(0.01)   
    totalsec += 0.01
    if(totalsec >= maxsec):
        print("Time's up! Game Over!")
        break
    elif(len(caught) == 12):
        print("Congrats! You caught them all")
        break

print("You found " + str(len(found)) + " of the 12 pokemon")
if(len(found) > 0):
    print ("Found pokemon are: " + str(found))
print("You caught " + str(len(caught)) + " of the 12 pokemon")
if(len(caught) > 0):
    print ("Caught pokemon are: " + str(caught))
        
myTk.destroy()   # Destroy the myTk window when the player loses


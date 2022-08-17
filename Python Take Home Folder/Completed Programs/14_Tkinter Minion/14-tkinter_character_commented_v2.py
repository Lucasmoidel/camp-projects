from tkinter import *   # Import the Tkinter module

tk = Tk()   # Create the Tk object
smiling = False   # Whether the character is smiling

# Create elements to place on the screen
canvas = Canvas(tk, width=400, height=400)   # Create a canvas
canvas.pack()   # Pack the canvas onto the screen

# When the mouse is clicked, set the character to smile
def mouseclick(event):
    global smiling   # Get a global variable for use
    smiling = True

# When the mouse is released, set the character to stop smiling
def mouserelease(event):
    global smiling   # Get a global variable for use
    smiling = False

# Draw the character without a mouth
def drawcharacter():
    canvas.create_oval(150, 150, 250, 250, fill="yellow", width=0)
    canvas.create_rectangle(150, 200, 250, 300, fill="yellow", outline="yellow")
    canvas.create_rectangle(150, 195, 250, 205, fill="black", outline="black")
    canvas.create_oval(175, 175, 225, 225, fill="gray", width=0)
    canvas.create_oval(180, 180, 220, 220, fill="white", width=0)
    canvas.create_oval(195, 195, 205, 205, fill="black", width=0)

# Draw the mouth, based on whether it's set to smile or not
def drawmouth(smile):
    if smile:
        canvas.create_arc(175, 230, 225, 260, extent=-180, style=CHORD, fill="black")
    else:
        canvas.create_rectangle(175, 250, 225, 255, fill="black")

# Bind mouse button press and release events
tk.bind_all("<Button-1>", mouseclick)
tk.bind_all("<ButtonRelease-1>", mouserelease)

# Run the update function for tk in a loop
while True:
    canvas.delete("all")   # Remove everything from the canvas
    drawcharacter()   # Draw the character body
    drawmouth(smiling)   # Draw the character's mouth

    tk.update()   # Update the screen

tk.destroy()   # When the player has pressed the quit button, destroy tk

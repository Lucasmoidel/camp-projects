import random

playerhealth = 100
dragonhealth = 100

print("the daragon has apered can you beat it?")
while (playerhealth>0 and dragonhealth> 0):
    print("YOUR HEALTH", playerhealth)
    print("DRAGON HEALTH", dragonhealth)
    move = input("Type 1 for light attack and 2 for heavy attack")
    number=random.randint(1, 100)
    if (number <= 75 and move == "1"):
        print("print you landed a ligh attack")
        dragonhealth -= 25
    elif (number <= 75 and move == "2"):
        print("print you landed a heavy attack")
        dragonhealth -= 50
    else:
        print("you've mised your attack and the dragon has struck you")
        playerhealth -= 50
if (playerhealth >= 0):
    print("you have defeted the dragon")
else:
    print("you have been defeeted")

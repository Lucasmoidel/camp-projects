import random

print("I chalinge you to a battle of rock paper scisors")
compchoice = random.randint(1, 3)
if(compchoice == 1):
    compchoice = "rock"
elif(compchoice == 2):
    compchoice = "paper"
else:
    compchoice = "scissors"
print('i have made my selection now it is your turn')
playerchoice = input("tell me rock, paper, or scissors: ")
print('you choose', playerchoice,"I chose", compchoice)
if(playerchoice == "rock"):
    if (compchoice == 'rock'):
        print("it is a draw")
    elif (compchoice == 'paper'):
        print("you have lost")
    else:
        print("you have won")
elif (playerchoice == "paper"):
    if (compchoice == 'rock'):
        print("you won")
    elif (compchoice == 'paper'):
        print("it is a draw")
    else:
        print("you have lost")
elif (playerchoice == "scissors"):
    if (compchoice == 'rock'):
        print("you have lost")
    elif (compchoice == 'paper'):
        print("you have won")
    else:
        print("it is a draw")
    
else:
    print("Cannot recognize", playerchoice, "please type science, programming, or animal")
import random

def play():   # Introduce the idea of defining functions
    print("You are walking in an ice storm back to camp.")
    print("You see 3 ice bridges ahead. One will crack if you step on it.")
    alive = True
    score=0
    
    while alive:
        number = random.randint(1,3)   # Get a random number for the bad bridge
        print("Choose bridge 1, 2, or 3.")
        guess = int(input())   # Get a number from the user
 
        if (guess == number):   
            print("Crack -- Crash -- Bye, byeeeeeeeeeee!")
            alive = False   # The player loses
        else:   # Otherwise
            print("Nice job! You are safe for now.  Keep going.")
            print("Next set of bridges ahead.")
            score += 1   # Introduce a new way of incrementing variables
 
    print("Game Over!  You scored " + (str)(score))

playgame = True

# Play until the user wants to stop
while playgame:
    play()   # Introduce the idea of calling functions
    again = input("Would you like to play again?  Type yes or no.")
    if(again != "yes"):   # If the user types "yes", play the game again
        playgame = False

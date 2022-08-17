import random

def play():  
    print("You are walking in an ice storm back to camp.")
    print("You see 3 ice bridges ahead. One will crack if you step on it.")
    alive = True
    score=0
    
    while alive:
        number = random.randint(1,3)   
        print("Choose bridge 1, 2, or 3.")
        guess = int(input())  
 
        if (guess == number):   
            print("Crack -- Crash -- Bye, byeeeeeeeeeee!")
            alive = False   
        else:  
            print("Nice job! You are safe for now.  Keep going.")
            print("Next set of bridges ahead.")
            score += 1  
 
    print("Game Over!  You scored " + (str)(score))

playgame = True

while playgame:
    play()  
    again = input("Would you like to play again? Type yes or no.")
    if(again != "yes"): 
        playgame = False

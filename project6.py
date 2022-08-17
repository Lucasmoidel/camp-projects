import random

def play():
    print("you are walking through an ice stormback to camp")
    print("you see 3 ice bridges ahead. they look dangarous.")
    alive = True
    score=0
    while alive:
        number= random.randint(1, 3)
        print ("chose bridge 1, 2, or 3.")
        guess = int(input())
        if (guess == number):
            print ("Crack -- crach -- Bye, byeeeeeeeeeeee")
            alive == False
        else:
            print("Nice job!you are safe for now...")
            print("There are more bridges ahead.")
            score += 1
    print("Game Over! you scored " + (str)(score) + ".")
play()

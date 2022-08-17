import random

won = False  
tries = 0

number = random.randint(1, 100)  
print("I'm thinking of a number between 1 and 100. Try to guess it!")

while not won:   
    guess = int(input())  
    tries = tries + 1  
    
    if(guess > number):
        print("You guessed too high!")
    if(guess < number):
        print("You guessed too low!")
    if(guess == number):
        won = True

print("Correct! The number was " + (str)(number))
print("You guessed the number in " + (str)(tries) + " tries!")



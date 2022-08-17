import random

won = False   # Set a variable for whether the user has won
tries = 0   # Set the starting number of tries to 0
    
number = random.randint(1, 100)   # Randomly choose a number between 1 and 100
print("I'm thinking of a number between 1 and 100. Try to guess it!")

while not won:   # So long as the user hasn't won yet, loop.
    guess = int(input())   # Get a number from the user
    tries = tries + 1   # Add 1 to the number of tries

    # Tell the user if their guess was too high or too low
    if(guess > number):
        print("You guessed too high!")
    if(guess < number):
        print("You guessed too low!")
    # If they guessed correctly, set won to True, to get out of the loop
    if(guess == number):
        won = True

# Print the winning message, and tell the user how many tries it took
print("Correct! The number was " + (str)(number))
print("You guessed the number in " + (str)(tries) + " tries!")

# Tell the user how well they did based on the number of tries it took
if(0 < tries <= 5):
    print("Incredible!")
if(5 < tries <= 8):
    print("Awesome!")
if(8 < tries <= 10):
    print("Good job!")
if(10 < tries <= 15):
    print("Nice!")
if(tries > 15):
    print("Better luck next time!")

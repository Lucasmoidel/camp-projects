import random
won = False
tries = 0
number = random.randint(1, 100)
print("im thinking of a number between 1 and 100...", number)
while not won:
    guess = int(input())
    tries = tries+1
    if (guess == number):
        won = True
    if (guess > number):
        print("you guessed too high!")
    if (guess < number):
        print("you guessed too low!")
        
print("Correct! The number was " + (str)(number))
print("You guessed the number in " + (str)(tries) + " tries.")

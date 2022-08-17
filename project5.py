import random

dicethrow = random.randint(1, 6)
print ("you rolled a", dicethrow)
win = False
lose = False
if (win):
    print ("We win!")
if (lose):
    print ("We lose!")
count = 0
while(count < 5):
    dice_roll = random.randint(1, 6)  #random dice roll
    if dice_roll == 1:
        print("we rolled a 1")
        count += 1

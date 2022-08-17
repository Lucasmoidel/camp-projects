import random
def play():
    print ("You are in an old castle. Each of the floors have 4 doors. Behind 3 doors are tresures for you, behind the other door is a dragon.")
    alive= True
    money= 0
    floor=1
    while alive:
        number = random.randint (1, 4)
        print ("you are on levle " +(str)(floor) + ". Choose dooor 1, 2, 3, or 4.")
        guess = int(input())
        if (guess ==0):
            break
        if (guess == number):
            print("uh oh, you opend the door with the dragon in it.")
            alive = False
        else:
            print ("you opend the door with the tresure. you erned some money")
            money+= random.randint(1000, 5000)
            floor +=1
            print ("you now have a total of $" + (str) (money) + "!")
            print ("would you like to contineu to levle" + (str) (floor) + " or leav the castle now? type 0 (zero) to leav the castle with all your money.")
    if alive==True:
        print ("you escaped with $" + (str) (money) + " have fun")
    else:
        print("Game over! the dragon ate you, along with all your money.")

playgame = True
while playgame:
    play()
    again = input("would you loke to play again and try your luck at getting to the shelter?")
    if (again != "yes"):
        playgame = False
play()

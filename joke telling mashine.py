scienceJokeQ = "why cant you trust an attom?"
scienceJokeA = "because they make up everything!"

programmingJokeQ = "why did the function not get along with the others?"
programmingJokeA = "it had to many arguments!"

animalJokeQ = "what do you call a bear with no ears?"
animalJokeA = "B!"

print("It is i, sir jokes-A-lot, the funnniest computer in all the land")
print("I know plenty of joces. just give me a acatagory and I'll make you laugh")
print("please type science, programming, or animal")
catagory = input()
print("you choose", catagory)
if (catagory == "science"):
    print(scienceJokeQ)
    input()
    print(scienceJokeA)
elif (catagory == "programming"):
    print(programmingJokeQ)
    input()
    print(programmingJokeA)
elif (catagory == "animal"):
    print(animalJokeQ)
    input()
    print(animalJokeA)

else:
    print("Cannot recognize", catagory, "please type science, programming, or animal")

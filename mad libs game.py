nouns = []
adjitaves = []
verbs = []
print("welcome to the madlibs game")
print("we will ask for a noun a adgitave or a verb to fill in aur story")
for i in range(3):
    nouns.append(input("please provide a noun: "))
for i in range(2):
    adjitaves.append(input("please provide a adjitave: "))
for i in range(1):
    verbs.append(input("please provide a verb: "))
story ="thare once was a " + nouns[0] + ' who was called geff.\n'
story +="he was in love with a girl named sandy who is a " + nouns[1] + '.\n'
story +="one day geff ran into a " + adjitaves[0] + " " + nouns[2] + '.\n'
story +="jeff was suprised and desided the only thing he could do is " + verbs[0] + '.\n'
story +="sandy saw jeff and told him 'wow you are so " + adjitaves[1] + "!'.\n"
story += "they lived hapily ever after..."
print()
print("all done here is our story")
print()
print(story)

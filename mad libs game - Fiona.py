nouns = []
adjectives = []
verbs = []
print("Welcome to the madlibs game!")
print("We will ask for some nouns, adjectives, and a verb to fill in our story.")
for i in range(3):
    nouns.append(input("Let's start with some nouns: "))
for i in range(2):
    adjectives.append(input("Next, some adjectives: "))
for i in range(1):
    verbs.append(input("Finally, a verb: "))
story ="There was a " + nouns[0] + ' who went by the name of Geoffrey.\n'
story +="Every day, he went on a walk down " + nouns[1] + ' street. \n'
story +="He enjoyed his walks, but on this particularly " + adjectives[0] + '\n'
story +="day, something seemed awry. So he " + verbs[0] + ' all the way back to his house.\n'
story +="But as soon as he opened the door, he was confronted with a wild " + nouns[2] + "!\n"
story +="In that moment, he woke up. 'What a " + adjectives[1] + " dream.' \n"
print()
print("The End! :]")
print()
print(story)

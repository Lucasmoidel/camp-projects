import random

answers = ['Realy. thats interesting', 'yes what else', 'absolutely', 'Tell me more']
subjects = [
    ['name', 'My name is yodav2. Wats yours?'],
    ['wether', 'I hope it rains!'],
    ['basebal', 'baseball is fun! Do you like footall'],
    ["ice cream", 'Ice cream is cold'],
    ["summer", 'summer is the best season'],
]
print("hi i'm yodav2, I want to be your computer friend.")
print("Lets chat! Tell me something interesting about yourself.")
print("if you're ever tired of talking , type quit or exit.")
while True:
    text = input()
    if (text == 'quit'):
        break
    if (text == 'exit'):
        break
    responded = False
    for s in subjects:
        if(text.find(s[0]) != -1):
            response = s[1]
            print(response)
            responded = True
            break

    if (not responded):
        response = random.choice(answers)
        print(response)
print ("Its been great talking to you. bye!")

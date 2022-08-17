import random

answers = ["Of corse!","no way!","probably!","probably not","im too tired to answer. ask again later."]
print("hi i am predicta, the computer fortune teller!")
while True:
    print("what would you like me to predict?")
    question = input()
    response = random.choice(answers)
    print(response)
    

import random

answers = [  
"Of course!",  
"I'm too tired to answer. Ask again later.",
"No way!",
"Probably!",
"Probably not."   
]   

print("Hi, I'm Predicta, the computer fortune teller!")

while True:   
    print("What would you like me to predict?")
    question = input()

    if(question == "quit"):  
        break   
    
    response = random.choice(answers)
    
    print(response)   

print("Bye!")

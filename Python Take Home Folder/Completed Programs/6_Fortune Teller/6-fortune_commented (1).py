import random

answers = [   # Create a new array, and insert potential responses below
"Of course!",   # Separate values by a ,
"I'm too tired to answer. Ask again later.",
"No way!",
"Probably!",
"Probably not."   # Do not add a , after the last element
]   # Finish initializing the array with a ]

print("Hi, I'm Predicta, the computer fortune teller!")

while True:   # Loop over the following indefinitely
    print("What would you like me to predict?")
    question = input()

    if(question == "quit"):   # Check if the user wants to quit
        break   # Break out of the loop if they do
    
    # Choose a random response from the answers array

    #response = answers[random.randint(0,4)] #same as code below but uses index
    response = random.choice(answers)
    
    print(response)   # Print the answer

print("Bye!")

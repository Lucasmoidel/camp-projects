print("Welcome to Calc-It-All!")
operation = input("Enter your operation: +, -, *, or /. ")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if (operation == "+"):
    answer = x+y
    print("The answer is", answer)

elif (operation == "-"):
    answer = x-y
    print("The answer is", answer)

elif (operation == "*"):
    answer = x*y
    print("The answer is", answer)
    
elif (operation == "/"):
    answer = x/y
    print("The answer is", answer)

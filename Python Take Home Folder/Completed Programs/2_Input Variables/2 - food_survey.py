person = input('Enter your name: ')
print('Hello', person)

food = input('What is your favorite food? ')

amount = int(input('How much '+ food + ' do you eat in a week? '))

yearly = int(amount * 52)

print('Guess what? You eat ', yearly, ' units of ', food, ' each year!')

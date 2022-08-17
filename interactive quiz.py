correct=0
print("welcometo the question game")
print("please type a, b, c, or d to the correct answer to the question")
print("how many legs do spiders have?")
print ("a: 2")
print ("b: 4")
print ("c: 6")
print ("d: 8")
answer = input()
if answer=="d":
    print("correct")
    correct=correct+1
else:
    print("wrong")
print("a spider has 8 legs.")
###############################
print("second question: what is the last name of the first U.S. president?")
print ("a: george")
print ("b: oboma")
print ("c: washington")
print ("d: bush")
answer = input()
if answer=="c":
    print("correct")
    correct=correct+1
else:
    print("wrong")
print("washington was the last name of the first U.S. president.")
print("game over! you answered " + str(correct) + " questions corectly")

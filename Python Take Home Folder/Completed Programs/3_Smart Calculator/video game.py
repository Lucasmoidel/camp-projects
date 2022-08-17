print("How many minutes a day do you play video games?")
video = int(input())
videoyear = video * 365

print("In one year, you will spend " + (str)(videoyear) + " " + "minutes playing video games.")

print(" ")
print("How many minutes a day do you do homework?")
homework = int(input())
homeworkyear = homework * 200

print("In one year, you will spend " + (str)(homeworkyear) + " " + "minutes doing homework.")
print(" ")
if (videoyear > homeworkyear):
    print("You spend " + (str)(videoyear - homeworkyear) +  " more minutes playing videogames versus homework.")
else :
    print("You spend " + (str)(homeworkyear - videoyear) +  " more minutes doing homework than playing videogames.")

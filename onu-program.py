answer = int(input("what is 2*2? "))
if answer == 4:
    correct1 = True
else:
    correct1 = False

answer = int(input("what is 10/2? "))
if answer == 5:
    correct2 = True
else:
    correct2 = False

if correct1 == True and correct2 == True :
    print("You got both answers right")
elif correct1 == True or correct2 == True :
    print("You got one answers right")
else:
    print("You got none answers right")

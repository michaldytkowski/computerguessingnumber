import random 

t1 = 1
t2 = 100
tries = 0

while True:
    randomnumber = random.randint(t1, t2)
    print("Our guess is " + str(randomnumber))
    answer = input("Write 'More', 'Less' or 'Win': ")
    if answer == "Win":
        print("Winner! You needed " + str(tries) + " tries!")
        break
    elif answer == "More":
        t1 = randomnumber
        tries =  tries + 1
    elif answer == "Less":
        t2 = randomnumber     
        tries = tries + 1 

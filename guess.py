b=6645
a=input("enter your guess: ")

while a!=b:
    
    if a == b:
        print "you guessed correctly"
    elif a - b <= 20 or a - b <= -20:
        print "HOTTTT"
        a = input("input another guess: ")
    elif a - b <= 50 and a - b > 20 or a - b <= -50 and a - b > -20 :
        print "Hot but not so hot"
        a = input("input another guess: ")
from random import randint
for _ in range (0,3):
    x = randint (0,100)
    if x < 30:
        print ("Rainy")
    elif x < 60:
        print ("Cool")
    else :
        print ("Sunny")

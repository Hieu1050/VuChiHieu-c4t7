print ("think of a number from 0 to 100")
i = 50
top = 100
bottom = 0 
print ("you're thinking of", i)
ans = int( input ("is that your num?(yes enter 1, no enter 0)    "))
j =1
while ans == 0:
    ans1 = int(input ("is your num higher than that(yes enter 1, no enter 0)     "))
    if ans1 ==1:
        bottom = i
        i = round(((i+top)/2),)
    else :
        top = i 
        i = round(((i+bottom)/2),)
    print ("you're thinking of", i)    
    ans = int(input ("is that your num?(yes enter 1, no enter 0)    "))
    j = j+1
    if top == bottom:
        print ("ur num is not real dude...")
        break
if ans == 1:
    print ("ur num is   ",i)
print ("num of guesses  ",j)
from random import shuffle
from random import randint
def scramble(word):
    word = list(word)
    shuffle(word)
    return "".join(word)
life = 3
ds = ["banana","pineapple","watermelon","pomegranate","durian","dragonfruit"]
while life > 0 :
    print ('lives:  ', life)
    org = ds[randint(0, len(ds)-1)]
    new = scramble(org)
    print ("scrambled word: ", new)
    response = input("type your answer: ")
    if org == response:
        print ("correct!")
    else :
        print ("wrong!")
        life -=1
print ("Game Over!")
Score = [1,2,3,2,9,52,34,99,12]

new = int(input ("Your score:   "))
Score.append(new)
Score =  (sorted(Score, key=int, reverse=True))
print ("High scores:")
for i in range (0,5):
    print (i+1,". ", Score[i], sep = '')
#ghép high scores vào trò tính toán:
from random import randint
import random
lvl = 10
x = 100
true_rep = 1
response = 1
life = 3
point = 0
scores = []
while True:    
    while true_rep== response or life >= 0:
        # phep toan ngau nhien
        n1 = randint(-lvl,lvl )
        n2 = randint(-lvl,lvl )
        diff = randint(- x, x )
        dau = ['+', '-', '*', '/']
        phep_toan = random.choice(dau)
        #dap an
        #chia cho 0 chon lai phep tinh:
        while phep_toan == '/' and (n2 == 0 or (n1 % n2 != 0) ):
            n2 = randint(-lvl,lvl )
        ans = ( eval (str(n1) + phep_toan + str(n2)))
        fake_ans = (ans + diff)

        print ("lives remain:   ", life)
        print ("Current score:  ", point)
        # ngau nhien dung sai (vi thuong thi sai nhieu hon han dung)
        flag = randint(0,1 )

        if flag ==1 or diff ==0:
            print (n1, phep_toan, n2, "=", ans)
            true_rep  = 1
        else :
            print (n1, phep_toan, n2, "=", fake_ans)
            true_rep = 0

        response = int (input("True or false?   (1 for TRUE, 0 for FALSE):     "))
        # 3 mạng:
        if true_rep != response:
            life -=1
            print ("WRONG!")
        else :
            print ("CORRECT!")
            point +=1
            
        # nang do kho
        lvl +=5
        print ('')   

    print ("Game over!")
    print ("")
    print ("Final score:", point)
    if point not in scores:
        scores.append (point)
    scores  =  (sorted(scores, key=int, reverse=True))
    print ("High scores:")
    
    
    if len(scores) <= 4:
        for i in range (len(scores)):
            print (i+1,". ", scores[i], sep = '') 
    else :
        for i in range (5) :
            print (i+1,". ", scores[i], sep = '') 
    
    print ("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    choice = input ("REPLAY(1) OR END(0):   ")
    if choice == '0':
        break
    point = 0
    life = 3

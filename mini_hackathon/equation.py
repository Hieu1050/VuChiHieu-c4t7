from random import randint
import random
top = -10
bottom = 10
x = 100
true_rep = 1
response = 1
life = 3
while true_rep== response or life >= 0:
    # phep toan ngau nhien
    n1 = randint(top,bottom )
    n2 = randint(top,bottom )
    diff = randint(- x, x )
    dau = ['+', '-', '*', '/']
    phep_toan = random.choice(dau)

    #dap an

    #chia cho 0 chon lai phep tinh:
    while phep_toan == '/' and n2 == 0:
        phep_toan = random.choice(dau)
        n2 = randint(top,bottom )
    ans = round( eval (str(n1) + phep_toan + str(n2)),)
    fake_ans = round ((ans + diff),)

    print ("lives remain:   ", life)
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
    # nang do kho
    top +=10
    bottom +=10
    if (x>=2):
        x -= 2
    print ('')


print ("Game over!")

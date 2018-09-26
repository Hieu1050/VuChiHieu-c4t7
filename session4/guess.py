from random import randint
x = randint (0, 100)

print (x)
y = int (input("Đoán đê     "))
i = 0
while (y!=x ) and (i < 8 ):
    if (x>y):
        y = int (input ("Tăng   "))
    else :
        y = int (input ("Giảm   "))
    i += 1
if y != x :
    print ("hết lượt r hihi")
else : print ("Giỏi")
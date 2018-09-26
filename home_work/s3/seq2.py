import math 
print ("Dãy số chính phương trong khoảng xác định. Nhập khoảng: ")
i = int (input("Từ: "))
j = int (input("Đến: "))
for k in range (i,j+1):
    k= k**2
    if k <= j+1: print (k)

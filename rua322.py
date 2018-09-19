
from turtle import*
i =80
n = int (input ("Đa giác có mấy cạnh?     "))
a = n
speed (0)
for _ in range (a):  
    for _ in range (n):
        if (n%2==0): color("red")
        else: color ("blue")
        forward (i)
        left (360/n)

    n = n-1
mainloop()


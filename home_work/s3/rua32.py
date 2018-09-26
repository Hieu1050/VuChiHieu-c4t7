
from turtle import*
i =10
n = int (input ("Đa giác có mấy cạnh?     "))
speed (0)
for _ in range (1000):  
    for _ in range (n):
        forward (i)
        left (360/n)
    for _ in range (n):
        forward (-i)
        left (360/n)
    
    left (4)
    i= i+5
mainloop()


from turtle import*
speed(0)
k=360
left (120)
for i in range(120):
    for j in range(3):
        forward (k)
        right (120)
        k= k-1
    right (3)

for i in range(120):
    for j in range(3):
        forward (k)
        right (120)
        k= k+1
    right (3)

mainloop()
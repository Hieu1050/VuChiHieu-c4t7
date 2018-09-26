from turtle import*
speed (0)
right (90)
forward (300)
right (90)
forward (300)
left (180)

j =300
for i in range(150):
    circle (j)
    j = j-2

forward (300)
left(90)
forward (600)
right(90)
forward (300)
left (180)

for k in range(150):
    circle (j)
    j= j+2

mainloop()
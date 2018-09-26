from turtle import*
speed(1000)
shape ("turtle")
pencolor("blue")

for i in range (2):
    circle(50)
    right(90)
    pencolor("yellow")

left (90)
for i in range (180):
    forward (0.85)
    left(1)
left(180)
pencolor("green")

for i in range (2):
    circle(50)
    left(90)
    pencolor("black")
right(90)
for i in range (90):
    forward (0.85)
    left(1)
left(180)
pencolor("red")
circle(50)
    


mainloop()
color =[ "blue",'red','teal']
#2
print ('our color list:')
for i in color:
    print (i)
#3
new = input ("add what?     ")
color.append (new)
print ("our new color list:")
for i in color:
    print (i)
#4
x = int (input("Enter a position:"))
while x > len(color):
    x = int (input("Error! Enter a position:"))
print ("color at position",x,":",color[x-1])



color =[ "blue",'red','teal','rainbow','gold','sand']
for z in color :
    print (z)
choice = input ("Item to delete:")
if choice in color:
    color.remove(choice)
else :
    x= int(choice)
    color.pop(x)

for y in color:
    print(y)

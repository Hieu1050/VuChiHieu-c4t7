ds = [1,12,25,36,47,84,72]
#1
z = 0 
x = int(input("Enter a num: "))
for i in range (0, len(ds)):
    if ds[i] == x:
        print("found in position", i+1) 
        x = 1
if z == 0:
    print ("num not found")
print("")



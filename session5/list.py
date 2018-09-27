#1
ds = ["apple","pen","pineapple","melon","abcxyz","ihi"]
ds[0] = "spider man"
print (ds)
#2
ds[len(ds)-1] = "dragon ball" 
print (ds)
#3
location = int(input("location? "))
while location > len(ds)-1:
    location = input ("no such location")
new = input ("new   ")
ds[location] = new
print (ds)
#4
ds.pop(1)
print (ds)
#5
if 'lol' in ds:
    ds.remove("lol")
else :
    print ('lol is not in the list!')
print (ds)
#6
xoa = int(input("delete location?   "))
while xoa > len(ds)-1:
    xoa =int( input ("no such location"))
ds.pop(xoa)
print (ds)
#7
xoa2 = str(input("delete what?  "))
if xoa2 in ds:
    ds.remove(xoa2)
else :
    print (xoa2, 'is not in the list!')
print (ds)
ds = input ("Enter a list of numbers, separated by ‘ ‘: ")
ds = ds.split(' ')
print (ds)
int_list = []
for item in ds :
    item = int(item)
    int_list.append(item)
print(int_list)
tong = 0 
for x in int_list:
    tong = tong + x 
print ("tong cach1:  ", tong)

Tong = sum (int_list)

print ("tong cach2:  ", Tong)
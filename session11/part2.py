lap = {
    'HP': 20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30
}
tong = 0

for x,y in lap.items():
    print (x,y, sep=" : ")

for i in lap:
    tong += lap[i]

print ("Num of all laptops: ",tong)
lap['FUJISU']= 15
lap['ALIENWARE']=5

for i in lap:
    tong += lap[i]

print ("Num of all laptops: ",tong)
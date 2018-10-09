lap = {
    'HP': 20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30
}
print ("Num of MACBOOKS left:", lap['MACBOOK'])
req = input("Enter laptop brand:    ")
req = req.upper()
while req not in ['HP','MACBOOK','DELL','ASUS']:
    req = input ("Brand not found, try again:   ")

print ('Num of',req, 'left:', lap[req])

lap ['TOSHIBA'] = 10
new = input ("Enter new brand:  ")
quan = int(input ("Enter quantity:  "))
lap[new] = quan
lap ['DELL'] += 10
lap ['MACBOOK'] = 2
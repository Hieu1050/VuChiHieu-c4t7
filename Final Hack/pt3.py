import requests
r = requests.get('https://jsonplaceholder.typicode.com/users', auth=('user', 'pass'))
# r.status_code
r =  (r.json())
find = input ("enter a user name: ")
x = 0
for i in r:
    if i['username'].upper()==find.upper():
        print (i)
        x = 1

if x == 0:
	print ("Username not found.")

ds = input ("Enter a list of numbers, separated by ‘,‘: ")

ds = ds.split(',')
int_list = []
for item in ds :
    item = int(item)
    int_list.append(item)
    
print ('even nums:')
for x in int_list:
    if x%2 == 0:
        print(x)

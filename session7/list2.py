ds = ["apple","pen","pineapple","melon","abcxyz","ihi"]
for i in range (3):
    new = input ("add what?")
    ds.append (new)

for j, elem in enumerate(ds):
    print (j+1,". ", elem.upper(),sep="")
print ('')
for j, elem in enumerate(ds):
    if 'e' in elem or "E" in elem:
        print (j+1,". ", elem.upper(),sep="")

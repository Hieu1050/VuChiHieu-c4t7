# choice = input("do what? enter c for create, r for read, u for update, d for delete:    ")
# while choice not in ['c','r','u','d']:
#     choice = input ("invalid")

ds = ["apple","pen","pineapple","melon","abcxyz","ihi"]
print( "current list: ", ds)
while True:
    choice = input("do what? enter c for create, r for read, u for update, d for delete:    ")
    while choice not in ['c','r','u','d']:
        choice = input ("invalid, retry:    ")
    if choice == "c":
        new = input ("add what?     ")
        ds.append (new)

    elif choice == "r":
        for j, elem in enumerate(ds):
            print (j+1,". ", elem.upper(),sep="")

    elif choice == "u":
        location = int(input("location? "))
        while location > len(ds)-1:
            location = input ("no such location, retry: ")
        new = input ("new   ")
        ds[location] = new

    else :
        xoa = int(input("delete location?   "))
        while xoa > len(ds)-1:
            xoa =int( input ("no such location"))
        ds.pop(xoa)
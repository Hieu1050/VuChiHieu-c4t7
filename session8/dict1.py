#11 12
product ={
    "name":"omachi",
    "price": 5000,
    "weigh": 100,
    "flavor": "beef",
    }
print (product)
del product["flavor"]
print (product)
del_key = input ("key to delete:    ")
del product[del_key]
print (product)


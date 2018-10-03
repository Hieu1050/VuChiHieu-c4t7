
product_list=[{
    "name":"omachi",
    "price": 5000,
    "weigh": 100,
    },

{
    "name": "chinsu",
    "price": 20000,
    "weigh": 300,
}]

p = product_list [0]
p["price"] +=3000
print (p)

product_list[1]["weigh"] += 100
print (product_list[1]["weigh"])
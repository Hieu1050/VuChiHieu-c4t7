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
product_list[0]["name"] += " xot bo ham"
print (product_list[0]["name"])

des = input("them mo ta:    ")
product_list[1]["name"] += des
print (product_list[1]["name"])
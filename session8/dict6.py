nhan_vien = [
    {"name": 'Huy',
    "role":"Waiter",
    "hours": 12,
    "salary per hour": 0.8,
    },

    {"name":'Tung' ,
    "role":"Cook",
    "hours":24,
    "salary per hour": 1.5,
    },

    {"name": 'M.Duc',
    "role":"Manager",
    "hours":20,
    "salary per hour": 2,
    },
]

print (nhan_vien[2]["salary per hour"])

nhan_vien[0]["name"] = "Huyen"
print (nhan_vien[0])

del nhan_vien[2]
for x  in nhan_vien:
    print(x)


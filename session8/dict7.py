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
tong = 0
for i in nhan_vien:
    tol_sal = round ((i['hours'])*(i['salary per hour']),2)*30
    tong += tol_sal
    print (i["name"], "earns ", tol_sal, "$ each month")

print ("total $ cho nhan vien", tong)
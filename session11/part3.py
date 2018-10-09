lap_price = {
    'HP': 600,
    'DELL':650,
    'MACBOOK':12000,
    'ASUS':400,
    'TOSHIBA':600,
    'FUJISU': 900,
    'ALIENWARE':1000,
}
lap_quan ={
    'HP': 20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
    'TOSHIBA': 10,
    'FUJISU':20,
    'ALIENWARE':50
}
comp_list = []
for key in lap_price:
    comp_list.append(key)
def not_int (a):
    try:
        int (a)
        return False 
    except  ValueError :
        return True
#kiểm tra xem nhập hợp lệ k
def invalid_check (s):
    s= s.upper()
    dk1 = 0 
    dk2 = 0 
    dk3 = 0
    list_s = s.split(":")
    if len (list_s) <2 :
        dk1 = 1
        print ("Thiếu ':' ")     
    else :
        if not_int (list_s[1]) or int (list_s[1])<=0:
            dk2 = 1
            print ("Sai số lượng sp")
        if (list_s[0] not in  comp_list):
            dk3 = 1       
            print ("Tên hãng không có trong ds hoặc có dấu cách") 
    result = dk1 + dk2 + dk3   
    return (result != 0)


 
# print ('ASUS price', lap_price['ASUS'])
# req = input ("Enter brand:")
# req = req.upper()
# print ('price:  ', lap_price[req])
# quan = int (input ("Select quantity:    "))
# tol = lap_price[req]*quan
# lap_quan[req]-=quan 
# print ("Total price:    ", tol)
tong = 0
for key in lap_price:
    gia = lap_price[key]*lap_quan[key]
    tong += gia
    print ("Tổng giá trị máy", key, ':', gia)
print ("Tổng giá trị các máy:   ", tong)


req = input ("Nhập tên hãng và số lượng sp, cách nhau bởi ':' và không có dấu cách: ")
while invalid_check(req):
    req = input ("Nhập tên hãng và số lượng sp, cách nhau bởi ':' và không có dấu cách: ")
order = req.split(':')
brand = order[0].upper()
quan = int (order[1])
price = lap_price[brand]*quan
print ("Tổng tiền:", price)


    

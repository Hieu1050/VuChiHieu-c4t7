quan =["ST",'BĐ','BTL','CG','ĐĐ','HCĐ']
dan_so = [150300,247100,333300,266800,420900,318000]
dien_tich = [117.43,9.224,43.35,12.04,9.96,10.09]
mat_do=[]
area = 0 
for i  in range (len(dan_so)):
    area = round (dan_so[i]/ dien_tich[i],2)
    mat_do.append (area)

for j  in range (len(dan_so)):
    print ("Quan", quan[j],"co mat do", mat_do[j])

tong_mat_do = sum (mat_do)
tong_quan = len(quan)
TB = round(tong_mat_do/tong_quan,2)
print ("MAT DO DAN TRUNG BINH:  ", TB)


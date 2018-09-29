quan =["ST",'BĐ','BTL','CG','ĐĐ','HCĐ']
dan_so = [150300,247100,333300,266800,420900,318000]
thap = dan_so[0]
vi_tri_thap = 0
for x in  range (len(dan_so)):
    if dan_so[x] <= thap:
        thap = dan_so[x]
        vi_tri_thap = x

print ("quan", quan[vi_tri_thap],"co it dan nhat:", thap)

cao = dan_so[0]
vi_tri_thap = 0
for j in  range (len(dan_so)):
    if dan_so[x] >= cao:
        cao = dan_so[x]
        vi_tri_cao = j


print ("quan", quan[vi_tri_cao],"co nhieu dan nhat:", cao)

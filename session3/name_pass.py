Name = input ("Name?    ")

crt_name = "Hieu1050"
crt_pass = "khongbiet"
if Name == crt_name:
    Pass = input ("Pass?    ")
    if Pass ==crt_pass:
        print ("Hello!")
    else: 
        print ("wrong password!")
else:
    print ("Wrong user name!")
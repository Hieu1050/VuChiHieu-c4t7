a = input("Do you want to convert from C or F? Enter C or F:      ")
while a != "C" and a!= "F":
    a= input("Error! Try a gain:    ")

if (a == "C"):
    c = int (input("Enter the temperature in C:  "))
    f = c*9/5 +32
    print (c, "(C)=", round(f,2), "(F)")
else :
    f = int (input("Enter the temperature in F:  "))
    c = (f-32)*5/9
    print (f, "(F)=", round(c,2), "(C)")
    
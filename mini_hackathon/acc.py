import string
def num_n_alphabet(x):
    a= x.isalpha()
    b= x.isdigit()
    if a or b :
        return False
    else :
        return True

name = (input("accout name: "))
pw = (input("password:  "))
while (not num_n_alphabet(pw)) or len(pw) <= 8:
    pw = input("invalid: ")

pw2 = (input("retype password   "))
while pw2 != pw:
    pw2 = (input("password unmatched:   "))
email = (input ("email: "))

def valid (s):
    if ("@" in s) and ("." in s):
        return True
    else :
        return False           
while not  valid(email) :
    email = input("Email invalid, try a gain    ")

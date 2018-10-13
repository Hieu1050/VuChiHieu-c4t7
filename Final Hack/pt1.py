x = int(input("Enter an int "))
print ('*'* x)
char = ['x','*']
for i in range (x):
    print(char[i%2],end = '') 
print ('')
h = int(input("Enter h "))
w = int(input("Enter w "))
x = int(input("Enter x "))
y = int(input("Enter y "))
for j in range (h):
    if j != y :
        print ("-"*w)
    else  :
        print ("-"*(x),'x','-'*(w-x-1), sep = '')

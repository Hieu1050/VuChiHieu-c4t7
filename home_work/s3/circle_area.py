import math
r= float(input("Enter the radius:   "))
s= math.pow(r,2)*math.pi
v= 4/3*math.pow(r,3)*math.pi
print ("The area of a circle with a radius of", r, "is", round(s,3), "square units.")
print ("The volume of a sphere with a radius of", r, "is", round(v,3), "cube units.")

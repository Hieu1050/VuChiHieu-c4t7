mass = float(input("Enter mass in kg:   "))
height = float(input("Enter height in cm:   "))
height = height /100
bmi = mass / (height**2)

if bmi <16 : print ("Severely underweight")
elif bmi <= 18.5 :print ("Underweight")
elif bmi < 25 :print ("Normal")
elif bmi < 30 :print ("Overweight")
else :print ("Obese")
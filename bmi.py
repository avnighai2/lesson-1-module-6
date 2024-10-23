# take weight and height as input from user
# bmi = weight/(height/100)**2
# if bmi is less than or qual to 18.4 than u are underweight 
# if bmi is less than or qual to 24.9 than u are healthy 
# if bmi is less than or qual to 29.9 than u are overweight
# if bmi is less than or qual to 34.9 than u are severly overweifght 
# if bmi is less than or qual to 39.9 than u are obese
# else print severly obese 

height = float(input("Enter height in meters:"))
weight = float(input("Enter weight in kilogrmas:"))

bmi = weight/(height/100)**2
print(f"Your bmi is {bmi}")

if bmi <= 18.4:
    print("You are underweight")
elif bmi <= 24.9:
    print("You are healthy")
elif bmi <= 29.9:
    print("You are uoverweight")
elif bmi <= 34.9:
    print("You are severly overweight")
elif bmi <= 39.9:
    print("You are obese")
else:
    print("you are severly obese")
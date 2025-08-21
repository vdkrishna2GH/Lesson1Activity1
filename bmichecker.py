# BMI checker
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print("Your BMI is: {:.2f}".format(bmi))

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25.0 <= bmi < 29.9:
    print("You are overweight.")  
elif 30.0 <= bmi < 34.9:
    print("You are in the obese class I category.")
elif 35.0 <= bmi < 39.9:
    print("You are in the obese class II category.")    
else:
    print("You are in the obese class III category.")


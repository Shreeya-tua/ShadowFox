# Take user input
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Check BMI category
if bmi >= 30:
    print("Obesity")

elif bmi >= 25 and bmi < 30:
    print("Overweight")

elif bmi >= 18.5 and bmi < 25:
    print("Normal")

else:
    print("Underweight")
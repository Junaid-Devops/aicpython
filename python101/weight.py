# Input: person's height and weight
height = int(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine the BMI category based on the calculated BMI
if bmi < 18.5:
    category = "underweight"
elif bmi >= 18.5 and bmi <= 24.9:
    category = "normal weight"
elif bmi >= 25 and bmi <= 29.9:
    category = "overweight"
elif bmi >= 30:
    category = "obese"
else:
    category = "Invalid BMI"

# Print the BMI and category
print("Your BMI is:", round(bmi, 2))
print("You are considered:", category)


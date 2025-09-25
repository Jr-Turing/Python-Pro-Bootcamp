# BMI Calculator
# BMI = weight(kg) / (height^2) in meters

# 1st input: enter height in meters
height = input("Enter height: \n")
# 2nd input: enter weight in kilograms
weight = input("Enter weight: \n")

# Convert input values
weight_as_int = int(weight)
height_as_float = float(height)

# Calculate BMI
bmi = weight_as_int / (height_as_float ** 2)

# another way to calculate BMI
# bmi = weight_as_int / height_as_float * height_as_float

# Convert to whole number
bmi_as_int = int(bmi)

print("BMI is:", bmi_as_int)
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25.0 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi, category = calculate_bmi(weight, height)
print(f"Your BMI is {bmi:.1f} and you are {category}.")
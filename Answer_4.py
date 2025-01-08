#     Create a return type function that takes weight and height of a user and return the bmi of the user.
#     Depending upon the bmi show the category that the customer belongs to.

def bmi():
    weight = int(input("Enter the weight in kgs: "))
    height = int(input("Enter the height in cms: "))
    bmi = weight / height**2 * 10000
    return bmi

bmi_value = bmi()
print()

if bmi_value < 18.5:
    print("You are Underweight with BMI ", round(bmi_value, 1))
elif 18.5 <= bmi_value <= 24.9:
    print("You are OF Normal weight with BMI ", round(bmi_value, 1))
elif 25.0 <= bmi_value <= 29.9:
    print("You are Overweight with BMI", round(bmi_value, 1))
else:
    print("You are Obese with BMI", round(bmi_value, 1))


"""Output:
Enter the weight in kgs: 97
Enter the height in cms: 183

You are Overweight with BMI 29.0"""
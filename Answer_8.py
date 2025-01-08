# Create a function that returns the quotient and remainder after dividing two numbers.

def divider():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    quotient = a//b
    remainder = a%b
    return quotient, remainder

output = divider()
print(f"The quotient and remainder post dividing the above two numbers is {output}")
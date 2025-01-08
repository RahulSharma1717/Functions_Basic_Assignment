# Create a return type function that takes principle, rate, and time from the user and then return simple interest after calculation.Afterwards Calculate amount that the user has to repay.

principal = 0

def simple_interest():
    global principal
    principal = int(input("Enter the Principal amount: "))
    rate = float(input("Enter the annual Rate of interest: "))
    time = float(input("Mention the duration of deposit in years: "))
    interest = principal * rate * time / 100
    return interest

sum = simple_interest()
total_sum = principal + sum
print()
print(f"Total sum received for depositing Rs.{principal} is {total_sum}")


"""Output:
Enter the Principal amount: 10000
Enter the annual Rate of interest: 6.25
Mention the duration of deposit in years: 3.5
Total sum received for depositing Rs.10000 is 12187.5"""
# Create a function called create_bill that takes product name,price, and qty and return the bill.

def create_bill(name, price, qty):
    print(f"Product Name: {name}, Product Price: {price}, Product_Quantity: {qty}, Total Bill: {price * qty}")

name = input("Enter Product Name: ")
price = float(input("Enter product price: "))
qty = int(input("Quantity of Product? "))

create_bill(name, price, qty)


"""Output:
Enter Product Name: RAMEN
Enter product price: 85.99
Quantity of Product? 7
Product Name: RAMEN, Product Price: 85.99, Product_Quantity: 7, Total Bill: 601.93"""
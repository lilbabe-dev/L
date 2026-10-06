#asking the user for the inputs

price = float(input("Enter the price of item: "))
quantity = int(input("Enter the quantity:"))

total = price * quantity

print(f"{quantity} item at {price:.2f} each = {total:.2f}.")
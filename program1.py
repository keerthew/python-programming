# List of items with their prices and quantities
items = [
    {"name": "Apple", "price": 0.5, "quantity": 4},
    {"name": "Banana", "price": 0.3, "quantity": 6},
    {"name": "Orange", "price": 0.8, "quantity": 3}
]

# Function to calculate total cost
def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

# Calculate and print the total bill
total_bill = calculate_total(items)
print(f"The total bill is: ${total_bill:.2f}")

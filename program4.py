def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"

def calculator():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    result = operations.get(op, lambda a, b: "Error: Invalid operator")(x, y)
    
    print("Result:", result)

calculator()

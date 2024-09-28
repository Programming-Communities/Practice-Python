import math

# Define functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def power(x, y):
    return x ** y

# New functions to enhance the calculator
def modulo(x, y):
    return x % y

def sqrt(x):
    if x < 0:
        return "Error: Negative number!"
    else:
        return math.sqrt(x)

# Main calculator function
def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulo")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid input. Please try again.")
            continue

        # For operations that need two inputs
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Please enter valid numbers!")
                continue

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result is: {power(num1, num2)}")
        elif choice == '6':
            print(f"The result is: {modulo(num1, num2)}")
        elif choice == '7':
            try:
                num = float(input("Enter number for square root: "))
                print(f"The square root is: {sqrt(num)}")
            except ValueError:
                print("Error: Please enter a valid number!")
                continue

# Run the calculator
calculator()

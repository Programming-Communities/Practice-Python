Here's a detailed explanation and solution for your Python programming assignment. Let's break it down step-by-step.

### Objective:
Create a Python program that:
1. Greets the user and collects their name and three favorite numbers.
2. Determines if the numbers are even or odd and stores this in a list of tuples.
3. Uses a `for` loop to create and print tuples containing each number and its square.
4. Calculates and prints the sum of the three numbers.
5. Checks if the sum is a prime number and notifies the user.

### Implementation:

```python
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get user information
name = input("Enter your name: ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))

# Store numbers in a list
numbers = [num1, num2, num3]

# Determine if numbers are even or odd
even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

# Print personalized greeting
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Print even or odd status of each number
for num, status in even_odd_list:
    print(f"The number {num} is {status}.")

# Create tuples of number and its square
squares = [(num, num ** 2) for num in numbers]

# Print number and its square
for num, square in squares:
    print(f"The number {num} and its square: ({num}, {square})")

# Calculate and print the sum of the numbers
sum_numbers = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {sum_numbers}")

# Check if the sum is a prime number and notify the user
if is_prime(sum_numbers):
    print(f"Wow, {sum_numbers} is a prime number!")
else:
    print(f"{sum_numbers} is not a prime number.")
```

### Explanation:

1. **Prime Number Check Function (`is_prime`)**:
   - A function to check if a number is prime. It returns `True` if the number is prime and `False` otherwise.

2. **Input Handling**:
   - The program prompts the user to enter their name and three favorite numbers. It then stores these numbers in a list.

3. **Even or Odd Determination**:
   - Uses a list comprehension to create a list of tuples where each tuple contains a number and its even/odd status.

4. **Number and Square Tuples**:
   - Uses a list comprehension to create tuples of each number and its square. These are printed out.

5. **Sum Calculation**:
   - Computes the sum of the three numbers and prints it.

6. **Prime Number Check**:
   - Uses the `is_prime` function to check if the sum is a prime number and prints an appropriate message.

### Additional Note:

If you want to ensure the code is as user-friendly as possible, consider adding error handling for invalid inputs. For example, check if the inputs are valid integers before proceeding with further calculations.

This code should cover all the requirements of your assignment. If you need any more help or have further questions, feel free to ask!
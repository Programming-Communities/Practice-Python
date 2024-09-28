# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main program
def number_exploration_tool():
    # Asking for user's name
    name = input("Enter your name: ")

    # Asking for user's favorite numbers
    numbers = []
    for i in range(1, 4):
        num = int(input(f"Enter your {i} favorite number: "))
        numbers.append(num)

    # Greeting the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    # Checking if the numbers are even or odd
    even_odd_info = []
    for num in numbers:
        if num % 2 == 0:
            even_odd_info.append((num, "even"))
            print(f"The number {num} is even.")
        else:
            even_odd_info.append((num, "odd"))
            print(f"The number {num} is odd.")

    # Printing the numbers and their squares
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num**2})")

    # Calculating the sum of the three numbers
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    # Checking if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number.")

# Run the program
if __name__ == "__main__":
    number_exploration_tool()
